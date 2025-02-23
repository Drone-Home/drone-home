# drone-home
## Project Architecture

The **Drone Home** project combines GPS, IMU, and computer vision for manual and autonomous navigation, enabling a vehicle to locate, and recharge drones in the field. This system is designed to support industries where drones operate over large or remote areas—like agriculture and emergency response—by minimizing drone downtime and reducing reliance on fixed charging stations.

### How to set up on new system
- Run Ubuntu 22.04 on a Nvidia Jetson Nano Super (M.2 SSD method)
- Install docker
- Install jetson-containers (https://github.com/dusty-nv/jetson-containers)
- Build container that contains ros2-humble and pytorch by running:  
  ```CUDA_VERSION=12.6 jetson-containers build --name=combined_test2 pytorch transformers ros:humble-desktop --verbose```
- Clone this repository
  ```git clone https://github.com/Drone-Home/drone-home/```  
  ```cd ros2_ws/Docker```
- Set executable permissions for the script:  
  ```sudo chmod +x run_combined.sh```
- Run the script:  
  ```./run_combined.sh```
- The docker container will start up and will set up the system and install all required libraries and dependencies for the project.

### How to run
- Once the container is running, start the website and ROS systems by running:  
  ```./tmux/run.sh```
- The website will be running in a tmux session named `"web"` and ROS2 will be running in a session named `"ros"`
- The website will run on the Jetson on port 5001
- To see the web background process terminal:  
  ```tmux a -t web```
- To see the ROS background process terminal:  
  ```tmux a -t ros```

### System Components

1. **Vehicle Navigation & Control**
   - **Platform**: Jetson Nano Super running ROS2 on Ubuntu 22.04.
   - **Control**: Motor and servo control via PWM interface, with safety switches for manual override and disarming.
   - **Navigation**:
     - **GPS and IMU based navigation** for long distances.
     - **Computer Vision (OpenCV)** for precise docking with drones.
   - **PID Controller**: Controlling vehicle motion based on sensors.

2. **Battery Charging System**
   - **Charging Requirements**: Initial power output of 5V 2A.
   - **Interface**: Magnetic pins for a secure connection. Create a standard connection that will be supported.

3. **User Interface (UI)**
   - **GUI Control Panel**:
     - Displays key metrics (battery, location, mission status).
     - Provides controls (navigate to drone, return, manual override).
     - Includes an accessible safety switch for emergency control.
   - **Interfaces**: Integrated with ROS2 and OpenCV for simple user interaction.

### Known Bugs:
- Map does not automatically resize when moving the point out of view (user can still move the map to see it).
- Switching modes and updating target coordinate works and has feedback, but it is not logged in the Command Log.
- Probe servos are flimsy and fall into resonance sometimes. Will be replaced in version 2 with larger metal gear servos.
- Probe is not visible on the camera, making it difficult to remotely view. A second camera will be added for close charger view, or the current camera will be repositioned.
