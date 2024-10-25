# drone-home
## Project Architecture

The **Drone Home** project combines GPS, IMU, and computer vision for autonomous navigation, enabling a vehicle to locate, retrieve, and recharge drones in the field. This system is designed to support industries where drones operate over large or remote areas—like agriculture and emergency response—by minimizing drone downtime and reducing reliance on fixed charging stations.

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

### Completed Work

- **Hardware**: Powered Raspberry Pi from BEC. Connected IMU using I2C GPIO and GPS using a serial USB cable. Installed Ubuntu 24.04 on SSD.

- **ROS2**: Developed a node that reads and publishes GPS data in `NavSatFix` message format and IMU data in `Pose` message format, establishing the foundation for autonomous navigation.

- **OpenCV**: Created a program that opens the camera, reads frames, and performs basic image processing operations.

- **GUI**: Implemented a Flask-based GUI with basic control elements displayed.

- **Connector**: **TODO**

Known Bugs:
The GPS works well when powering the Pi 5 from USB C. When powered by the BEC it does not want to get a fix. This is likely due to noise in the power that can be fixed by a capacitor.

