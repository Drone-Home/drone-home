from setuptools import find_packages, setup

package_name = 'drone_home'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi',
    maintainer_email='pi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'imu_publisher = drone_home.imu_publisher:main',
            'gps_publisher = drone_home.gps_publisher:main',
            'pwm_publisher = drone_home.pwm_publisher:main',
            'drive_publisher = drone_home.joy_to_ackermann:main',
            'drive_hardware = drone_home.ackermann_drive:main',
            'controller = drone_home.controller:main',
            'visualization = drone_home.markers:main'
        ],
    },
)
