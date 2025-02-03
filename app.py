from flask import Flask, render_template, Response, request, jsonify
import cv2
import threading
import rclpy
from ultralytics import YOLO  # Import YOLO
from web_support import WebSupport

app = Flask(__name__)

# Initialize the webcam
camera = cv2.VideoCapture(0)

# Initialize ROS in a separate thread
rclpy.init()
ros_node = WebSupport()
def ros_spin():
    rclpy.spin(ros_node)
threading.Thread(target=ros_spin, daemon=True).start()

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

def generate_frames():
    """Capture frames from the webcam and process them with YOLO."""
    import os
    model_path = os.path.abspath("./YOLOv11_custom/yolov11_custom.pt")
    model = YOLO(model_path)  # Load YOLO model

    while True:
        # Read a frame from the webcam
        success, frame = camera.read()
        if not success:
            break
        else:
            # Perform YOLO inference on the frame
            results = model.predict(frame, conf=0.7, show_labels=True, show_conf=True, classes=[0], verbose=False)

            # Extract the processed frame
            for result in results:
                frame = result.plot()  # Draw YOLO detections on the frame

                for box in result.boxes:
                    # Publish CV box
                    ros_node.publish_cv_box(box)

            # Encode the frame as JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the processed frame
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Route to stream video feed."""
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/control', methods=['POST'])
def control():
    """Handle control actions from the web app."""
    data = request.json
    steering = data.get('steering')
    speed = data.get('speed')
    ros_node.publish_control(steering, speed)  # Publish the action to the ROS topic
    return jsonify({'status': 'success', 'action': data}), 200
    
if __name__ == '__main__':    
    app.run(debug=False, host='0.0.0.0', port=5001)
    camera.release()
    ros_node.destroy_node()
    rclpy.shutdown()