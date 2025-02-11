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
            executable='pwm_publisher',
            name='sim',
        ),
	Node(
	    package='drone_home',
            namespace='drone_home1',
            executable='gps_publisher',
            name='sim'
        ),
        Node(
            package='drone_home',
            namespace='drone_home1',
            executable='imu_publisher',
            name='sim'
        ),
        Node(
            package='drone_home',
            namespace='drone_home1',
            executable='drive_hardware',
            name='sim'
        ),


    ])
        # Node(
        #     package='drone_home',
        #     namespace='drone_home1',
        #     executable='controller',
        #     name='sim'
        # ),
