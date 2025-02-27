# Modifies base ros pytorch image

# Start from the base image
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

# Install nano
RUN apt-get update && apt-get install -y nano
RUN apt install tmux

# Install i2c detection tool
RUN apt-get install -y i2c-tools 

## Adafruit
# Clone fixed repo - repo already in git folder
#RUN git clone https://github.com/Dominikk7/Adafruit_Python_PlatformDetect /workspaces/isaac_ros-dev/git/Adafruit_Python_PlatformDetect

# Install and patch platform detect
RUN pip3 install Adafruit-PlatformDetect
COPY git/Adafruit_Python/adafruit_platformdetect/constants/boards.py /usr/local/lib/python3.10/dist-packages/adafruit_platformdetect/constants/boards.py 

# Servo board controller, motor, IMU
RUN pip3 install adafruit-circuitpython-pca9685
RUN pip3 install adafruit-circuitpython-motor
RUN pip3 install adafruit-circuitpython-bno055
RUN pip3 install adafruit-circuitpython-gps

## NVIDIA GPIO
# Clone the repository - repo already in git folder
#RUN git clone https://github.com/NVIDIA/jetson-gpio /workspaces/isaac_ros-dev/git/jetson-gpio

# Install the Python package
COPY git/jetson-gpio /home/admin/git/jetson-gpio
RUN cd /home/admin/git/jetson-gpio && python3 setup.py install

# ROS dependencies
RUN apt-get install -y ros-humble-ackermann-msgs

# Web server interface
RUN pip3 install --ignore-installed flask
RUN apt install v4l-utils

# YOLOv11 CV
RUN pip install ultralytics

# ROS source fix for opening new windows
RUN echo "source /opt/ros/humble/install/setup.bash" >> ~/.bashrc
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

# Fix permissions
#RUN chmod 777 -R /home/
#RUN chmod +777 /dev/i2c-7
#RUN chmod +777 /dev/gpiochip0
#RUN chmod +777 /dev/ttyUSB0

#
# PyCUDA
#
#ENV PATH="/usr/local/cuda/bin:${PATH}"
#ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"
#RUN echo "$PATH" && echo "$LD_LIBRARY_PATH"

#RUN pip3 install pycuda six --verbose
