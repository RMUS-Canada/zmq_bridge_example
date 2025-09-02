from setuptools import find_packages, setup

package_name = 'zmq_bridge_example'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/jazzy_bridge.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    description='A ROS2 package that bridges data between ROS2 Jazzy and Humble using ZMQ',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'jazzy_bridge = zmq_bridge_example.jazzy_bridge:main',
        ],
    },
)
