#!/bin/bash
LOCAL_DEV_DIR="/home/jet/ros2ws/"           # mounted inside of the container as a volume
INTERNAL_PATH="/workspaces/drone_home-dev"  # working directory inside container
CONTAINER_NAME="combined_test2:l4t-r36.4.3" # created by running: CUDA_VERSION=12.6 jetson-containers build --name=combined_test2 pytorch transformers ros:humble-desktop --verbose

jetson-containers run \
    --workdir $INTERNAL_PATH \
    -v $DEV_DIR:$INTERNAL_PATH \
    $CONTAINER_NAME  

#docker run -it --rm \
#    --privileged \
#    --network host \
#    --ipc=host \
#    --runtime nvidia \
#    --entrypoint /usr/local/bin/scripts/workspace-entrypoint.sh \
#    --workdir /workspaces/isaac_ros-dev \
#    combined_test2:l4t-r36.4.3 \
#    /bin/bash

    
