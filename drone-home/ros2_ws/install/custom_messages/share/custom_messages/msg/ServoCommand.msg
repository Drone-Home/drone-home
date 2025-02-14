# List of servo IDs
int32[] servo_ids

# List of corresponding positions
float32[] positions

# For this project ServoCommand is used for the two charger servos. The message is a range from -1 to 1 that
# gets mapped into the real min and max range in servo_jetson.
