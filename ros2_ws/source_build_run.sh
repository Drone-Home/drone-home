# Get current timestamp
timestamp=$(date +'%Y-%m-%d_%H-%M-%S')

# Define the log file name with timestamp
log_file="logs/output_$timestamp.log"

source install/local_setup.bash
colcon build && ros2 launch launch/launch1.py | tee "$log_file"