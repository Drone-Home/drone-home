from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO  # Import YOLO

app = Flask(__name__)

# Initialize the webcam
camera = cv2.VideoCapture(0)

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
            results = model.predict(frame, conf=0.87, show_labels=True, show_conf=True, classes=[0])

            # Extract the processed frame
            for result in results:
                frame = result.plot()  # Draw YOLO detections on the frame

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)