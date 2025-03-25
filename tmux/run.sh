#!/bin/bash

SESSION_NAME="web"
SESSION_NAME_ROS="ros"

# Check if the session already exists
tmux has-session -t $SESSION_NAME_ROS 2>/dev/null

if [ $? != 0 ]; then
    # Create a new detached tmux session
    tmux new-session -d -s $SESSION_NAME_ROS
    
    # Run commands inside the tmux session
    tmux send-keys -t $SESSION_NAME_ROS "ls" C-m
    tmux send-keys -t $SESSION_NAME_ROS "tmux source .tmux.conf" C-m # enable scrolling
    tmux send-keys -t $SESSION_NAME_ROS "cd ../drone-home/ros2_ws" C-m # go to ros directory
    tmux send-keys -t $SESSION_NAME_ROS "./source_build_run.sh" C-m # start ros nodes
fi

echo "Tmux session '$SESSION_NAME_ROS' started. tmux a -t $SESSION_NAME_ROS"

# Wait for ros node to start to avoid lag
sleep 3

# Check if the session already exists
tmux has-session -t $SESSION_NAME 2>/dev/null

if [ $? != 0 ]; then
    # Create a new detached tmux session
    tmux new-session -d -s $SESSION_NAME
    
    # Run commands inside the tmux session
    tmux send-keys -t $SESSION_NAME "ls" C-m
    tmux send-keys -t $SESSION_NAME "tmux source .tmux.conf" C-m # enable scrolling
    tmux send-keys -t $SESSION_NAME "cd ../python_tests/RCFLASK" C-m # go to web directory
    tmux send-keys -t $SESSION_NAME "./run.sh" C-m # start web server
fi

echo "Tmux session '$SESSION_NAME' started. tmux a -t $SESSION_NAME"

