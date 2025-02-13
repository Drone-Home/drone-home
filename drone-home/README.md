# drone-home
## Project Architecture

The **Drone Home** project combines GPS, IMU, and computer vision for autonomous navigation, enabling a vehicle to locate, retrieve, and recharge drones in the field. This system is designed to support industries where drones operate over large or remote areas—like agriculture and emergency response—by minimizing drone downtime and reducing reliance on fixed charging stations.

### How to run
- Run Ubuntu 24.04 on a Pi 5 and install ROS2 Jazzy
- Clone repository
- cd ros2_ws
- pip install -r requirements.txt
- sudo chmod +x source_build_run.sh
- ./source_build_run.sh
- The ros nodes will run. Run ros2 topic list to list the topics.

### System Components

1. **Vehicle Navigation & Control**
   - **Platform**: Raspberry Pi 5 running ROS2 on Ubuntu 24.04.
   - **Control**: Motor and servo control via PWM interface, with safety switches for manual override and disarming.
   - **Navigation**:
     - **GPS and IMU based navigation** for long distances.
     - **Computer Vision (OpenCV)** for precise docking with drones.
   - **PID Controller**: Controlling vehicle motion based on sensors

2. **Battery Charging System**
   - **Charging Requirements**: Initial power output of ~19W (12V * 1.6A) to support 6S LiPo batteries, with potential upgrades to ~38W.
   - **Interface**: Magnetic pins for a secure connection. Create a standard connnection that will be supported.

3. **User Interface (UI)**
   - **GUI Control Panel**:
     - Displays key metrics (battery, location, mission status).
     - Provides controls (navigate to drone, return, manual override).
     - Includes an accessible safety switch for emergency control.
   - **Interfaces**: Integrated with ROS2 and OpenCV for simlpe user interaction.

### Known Bugs:
- The Google Earth live preview vehicle orientation was off by 90 degrees during one of many tests for some reason. Resrarting fixed the issue and it has not beed repeated since.
- When running the manual joystick control at the same time as the automatic controller, the vehicle has some jitter because it is recieving controls from two nodes at once. The joystick publishes much faster so the vehicle can still be controlled but multiplexing needs to be implemented.
- When first turning on the vehicle and there is no fix yet, the GPS visualization displays an incorrect coordinate.

