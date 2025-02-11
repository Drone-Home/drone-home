# Get current timestamp
timestamp=$(date +'%Y-%m-%d_%H-%M-%S')

# Define the log file name with timestamp
log_file="logs/output_$timestamp.log"

source install/local_setup.bash
colcon build && ros2 launch launch/jetson_launch.py | tee "$log_file" &
ros2_pid=$!

cd ~
python3 -m http.server > /dev/null 2>&1 &
python_pid=$!


trap "kill $python_pid; exit" INT

wait $ros2_pid
wait $python_pid
