from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
    Node(
            package='drone_home',
            namespace='drone_home1',
            executable='cv_controller',
            name='sim',
        ),
    Node(
            package='drone_home',
            namespace='drone_home1',
            executable='controller',
            name='controller',
        ),
	Node(
            package='drone_home',
            namespace='drone_home1',
            executable='pwm_publisher',
            name='pwm_publisher',
        ),
	Node(
	    package='drone_home',
            namespace='drone_home1',
            executable='gps_publisher',
            name='gps_publisher'
        ),
        Node(
            package='drone_home',
            namespace='drone_home1',
            executable='imu_publisher',
            name='imu_publisher'
        ),
        Node(
            package='drone_home',
            namespace='drone_home1',
            executable='drive_hardware',
            name='drive_hardware'
        ),


    ])
        # Node(
        #     package='drone_home',
        #     namespace='drone_home1',
        #     executable='controller',
        #     name='sim'
        # ),
