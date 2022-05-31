#!/usr/bin/env python
# -*- coding:utf-8 -*-

""""""
from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='this_package_name',
            namespace='',
            executable='node_name',
            name='node_name'
            #     remappings=[
            #         ('/original_topic_name', '/remapped_topic_name'),
            #     ]
        )
    ])
