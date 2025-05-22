# E-puck2-from-Physical-to-Simulation

## Workflow Overview

1. **Train Deep RL Model in Isaac Sim**
   - Use NVIDIA Isaac Sim to train your Deep RL agent controlling a simulated e-puck robot.
   - The agent learns policies for navigation, obstacle avoidance, or other tasks.

2. **Export the Trained Model**
   - Save the trained neural network weights (e.g., PyTorch `.pt` file or ONNX format).

3. **Set Up Real-Time Communication**
   - Establish communication between your control system (running the trained model) and the physical e-puck 2 robot.
   - Use Bluetooth, Wi-Fi, or USB serial to send control commands (motor speeds, directions).

4. **Deploy the Model for Inference**
   - Run the trained model on a device connected to the e-puck (e.g., a laptop, Raspberry Pi).
   - The device receives sensor data from the e-puck, preprocesses it, feeds it to the model, and sends back control commands.

5. **Sensor Data Mapping**
   - Map real e-puck sensor data (e.g., proximity sensors, camera) to the input format expected by the model.
   - Handle differences between simulation and reality (domain gap).

6. **Control Loop**
   - Continuously:
     - Read sensors from e-puck.
     - Preprocess and input to the RL model.
     - Get action outputs (e.g., wheel velocities).
     - Send commands to e-puck actuators.

---

## Key Considerations

- **Sim-to-Real Transfer**
  - Use domain randomization during training to improve robustness.
  - Calibrate sensors and actuators to reduce discrepancies.

- **Communication Protocol**
  - Use e-puck SDK or custom serial/Bluetooth commands.
  - Ensure low-latency and reliable data exchange.

- **Hardware Setup**
  - The inference device must be able to communicate with e-puck and run the model efficiently.

- **Safety**
  - Implement emergency stop and safety checks.

---

## Example Tools & Libraries

- **Isaac Sim**: For training and simulation.
- **PyTorch/TensorFlow**: For model export and inference.
- **e-puck SDK**: For communication with the robot.
- **Python libraries**: `pyserial`, `bluepy` for serial/Bluetooth communication.
- **ROS (optional)**: For middleware integration.