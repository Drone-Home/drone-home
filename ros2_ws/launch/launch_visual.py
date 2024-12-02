from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='drone_home',
            namespace='drone_home1',
            executable='visualization',
            name='sim'
        ),


    ])
        # Node(
        #     package='drone_home',
        #     namespace='drone_home1',
        #     executable='controller',
        #     name='sim'
        # ),