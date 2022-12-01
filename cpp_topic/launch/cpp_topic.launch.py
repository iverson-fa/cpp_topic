from launch import LaunchDescription
from launch_ros.actions import Node



def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cpp_topic',
            namespace='test02',
            executable='talker_str',
            name='node01'
        ),
        Node(
            package='cpp_topic',
            namespace='test01',
            executable='talker_str',
            name='node02'
        ),
        Node(
            package='cpp_topic',
            namespace='test01',
            executable='listener_str',
            name='node03'
        )
    ])