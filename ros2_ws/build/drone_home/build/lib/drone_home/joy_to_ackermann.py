import rclpy
import math
from rclpy.node import Node

#from std_msgs.msg import String
from ackermann_msgs.msg import AckermannDriveStamped
from sensor_msgs.msg import Joy

class cdcJoySubscriber(Node):

    def __init__(self):
        super().__init__('joy_to_ackerman') # my_pub_sub
        self.subscription = self.create_subscription(
            Joy,
            '/joy', # not in namespace from remote
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'vehicle/drive', 10)
        self.subscription  # prevent unused variable warning


    def listener_callback(self, msg):
        # Speed divider
        slowdown = 2

        # Send ackermann from joy with conversion
        out_msg = AckermannDriveStamped()

        # Steering (left x) (1=left, -1=right) -> pi/4 to -pi/4
        out_msg.drive.steering_angle = -msg.axes[0] * (math.pi / 4)

        # For controller
        if(msg.axes[1] > .05):
            out_msg.drive.speed = (msg.axes[1]) * -1 * (math.pi / 4)
        # Forwards (right trigger) (1=unpressed, -1=pressed) -> 0 to 2
        else:
            out_msg.drive.speed = (msg.axes[1]) * -1 * (math.pi / 4)


        '''
        # For joystick
        # Reverse (left trigger) (1=unpressed, -1=pressed) -> 0 to -2
        if(msg.axes[2] < .95):
            out_msg.drive.speed = (msg.axes[2] - 1)/2 * -1 * (math.pi / 4)
        # Forwards (right trigger) (1=unpressed, -1=pressed) -> 0 to 2
        else:
            out_msg.drive.speed = (msg.axes[5] - 1)/2 * 1 * (math.pi / 4)
        '''

        # Press B -> divide speed
        if(msg.buttons[1]):
            if(out_msg.drive.speed != 0):
                out_msg.drive.speed /= slowdown
                
        
        # Hold B to print drive 
        if(msg.buttons[1]):
            self.get_logger().info(f'Sent: {out_msg.drive.steering_angle}, {out_msg.drive.speed}')
            self.publisher_.publish(out_msg)
            

def main(args=None):
    rclpy.init(args=args)

    joy_subscriber = cdcJoySubscriber()

    rclpy.spin(joy_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    joy_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()