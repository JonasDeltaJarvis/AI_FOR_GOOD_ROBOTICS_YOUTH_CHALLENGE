# Mecanum Wheel Autonomous Robot Mission

# Import necessary libraries
import time
import numpy as np

class MecanumRobot:
    def __init__(self):
        self.position = np.array([0, 0, 0])  # x, y, theta
        self.speed = 0.0

    def move_forward(self, distance):
        # Update the position to simulate forward movement
        self.position[0] += distance * np.cos(self.position[2])
        self.position[1] += distance * np.sin(self.position[2])

    def turn(self, angle):
        # Update heading (theta)
        self.position[2] += angle

    def get_position(self):
        return self.position

# Example mission function

def execute_mission():
    robot = MecanumRobot()

    # Move forward 5 units
    robot.move_forward(5)
    print(f'Current Position: {robot.get_position()}')

    # Turn 90 degrees
    robot.turn(np.pi / 2)
    print(f'Current Position after turning: {robot.get_position()}')

    # Move forward 3 units after turning
    robot.move_forward(3)
    print(f'Final Position: {robot.get_position()}')

if __name__ == '__main__':
    execute_mission()