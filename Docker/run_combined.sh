#!/bin/bash

# Uses base image and runs command to modify it with the Dockerfile in the /home/jet/ros2ws/Dockerfile directory
# Runs the image
# Attaches if already running

LOCAL_DEV_DIR="/home/jet/ros2ws/"           # mounted inside of the container as a volume
INTERNAL_PATH="/workspaces/drone_home-dev"  # working directory inside container

BASE_CONTAINER_NAME="combined_test2:l4t-r36.4.3" # created by running: CUDA_VERSION=12.6 jetson-containers build --name=combined_test2 pytorch transformers ros:humble-desktop --verbose
BASE_CONTAINER_ID="combined_test2"               # container name for checking if its running

MODIFIED_CONTAINER_NAME="drone_home:latest"
MODIFIED_CONTAINER_ID="drone_home"

# Check if the container is already running
if docker ps -q -f name=$MODIFIED_CONTAINER_ID | grep -q .; then
    echo "Attaching to existing container..."
    docker exec -it $MODIFIED_CONTAINER_ID bash
else
    # Update base image with Dockerfile to install dependencies for project
    docker build -t $MODIFIED_CONTAINER_NAME "${LOCAL_DEV_DIR}Docker" --build-arg BASE_IMAGE="$BASE_CONTAINER_NAME" --debug        

    # First time run in detached mode to run in background
    echo "Starting new container..."
    jetson-containers run -d \
        --privileged \
        -v /dev:/dev \
        --workdir $INTERNAL_PATH \
        --name $MODIFIED_CONTAINER_ID \
        -v $LOCAL_DEV_DIR:$INTERNAL_PATH \
        $MODIFIED_CONTAINER_NAME /bin/bash -c "cd /workspaces/drone_home-dev/tmux/ && ./run.sh && bash" # Auto run tmux scripts
        #-c "tmux/run.sh && bash"
    
fi
    
