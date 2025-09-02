#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='zmq_bridge_example',
            executable='jazzy_bridge',
            name='jazzy_bridge',
            output='screen',
            parameters=[],
        )
    ])
