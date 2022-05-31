#!/usr/bin/env python
# -*- coding:utf-8 -*-

from glob import glob

from setuptools import setup

package_name = 'this_package_name'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, glob('launch/*_launch.py')),
        ('share/' + package_name + '/imgs/', glob('imgs/*.png')),
    ],
    py_modules=[
        # f'{package_name}.lib.battery_data',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='TODO:',
    maintainer_email='TODO:',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_name = this_package_name.node_name:main',
        ]
    },
)
