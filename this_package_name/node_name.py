#!/usr/bin/env python
# -*- coding:utf-8 -*-
""""""

import sys

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class NodeName(Node):
    """"""

    def __init__(self, node_name: str) -> None:
        """Constructor."""
        super().__init__(node_name=node_name)
        # self.__publisher = self.create_publisher(MessageType, 'topic_name', 10)
        # self.create_subscription(MessageType, 'topic_name', self.__callback, 10)
        # self.timer = self.create_timer(1.0, self.__main_loop)

    def __main_loop(self) -> None:
        """Main loop executed every 1 second."""
        pass

    def __callback(self, msg: MessageType) -> None:
        """Callback function."""
        pass

    def __del__(self) -> None:
        """Destructor."""
        pass


def main():
    """Main node."""
    rclpy.init()
    try:
        node = NodeName('node_name')
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        sys.exit(1)
    finally:
        rclpy.try_shutdown()
        node.destroy_node()


if __name__ == '__main__':
    main()
