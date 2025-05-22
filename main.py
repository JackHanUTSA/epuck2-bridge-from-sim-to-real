import torch
import serial
import time
import struct

# Load the trained RL model
model = torch.load('model.pt')
model.eval()

# Open serial connection to e-puck (adjust port and baudrate)
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

def read_sensors():
    """
    Read sensor data from e-puck.
    This is a placeholder: implement according to your e-puck protocol.
    For example, read 8 proximity sensor values as floats.
    """
    ser.write(b'READ_SENSORS\n')  # Command to request sensor data
    line = ser.readline().decode().strip()
    # Example response: "0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8"
    sensor_values = list(map(float, line.split(',')))
    return sensor_values

def send_motor_commands(left_speed, right_speed):
    """
    Send motor speed commands to e-puck.
    Assume speeds are floats between -1.0 and 1.0.
    Convert to int range -100 to 100 for example.
    """
    left_int = int(left_speed * 100)
    right_int = int(right_speed * 100)
    # Pack two signed bytes and send
    cmd = struct.pack('bb', left_int, right_int)
    ser.write(b'MOTOR' + cmd + b'\n')

def preprocess_sensors(sensor_values):
    """
    Convert sensor data to tensor input for the model.
    """
    return torch.tensor(sensor_values, dtype=torch.float32).unsqueeze(0)  # batch size 1

try:
    while True:
        sensors = read_sensors()
        input_tensor = preprocess_sensors(sensors)
        
        with torch.no_grad():
            action = model(input_tensor)  # model outputs tensor with motor commands
        
        # Assuming model outputs two values: left and right wheel speeds
        left_speed, right_speed = action.squeeze().tolist()
        
        send_motor_commands(left_speed, right_speed)
        
        time.sleep(0.1)  # control loop delay

except KeyboardInterrupt:
    print("Stopping control loop")
    ser.close()