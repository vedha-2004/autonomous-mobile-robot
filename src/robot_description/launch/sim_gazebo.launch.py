from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([

        ExecuteProcess(
            cmd=[
                'gz', 'sim',
                '-r',
                '/home/vedha/autonomous_ws/src/robot_description/worlds/empty.world'
            ],
            output='screen'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'robot_description': open(
                    '/home/vedha/autonomous_ws/src/robot_description/urdf/robot.urdf.xacro'
                ).read()
            }]
        ),

        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-name', 'mobile_robot',
                '-topic', 'robot_description'
            ],
            output='screen'
        )
    ])

