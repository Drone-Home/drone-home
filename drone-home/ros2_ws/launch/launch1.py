from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='drone_home',
            namespace='drone_home1',
            executable='controller', # drive_publisher
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
            executable='drive_publisher',
            name='sim'
        ),
        Node(
            package='drone_home',
            namespace='drone_home1',
            executable='drive_hardware',
            name='sim'
        ),
        Node(
            package='drone_home',
            namespace='drone_home1',
            executable='visualization',
            name='sim'
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            namespace='drone_home1',
            output='screen',
            arguments=['0', '0', '0', '0', '0', '0', '1', 'map', 'imu_frame']
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            namespace='drone_home1',
            output='screen',
            arguments=['0', '0', '0', '0', '0', '0', '1', 'map', 'gps_sensor']
        ),


    ])
        # Node(
        #     package='drone_home',
        #     namespace='drone_home1',
        #     executable='controller',
        #     name='sim'
        # ),