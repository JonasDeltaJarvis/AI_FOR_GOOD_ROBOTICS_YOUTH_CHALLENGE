# AI_FOR_GOOD_ROBOTICS_YOUTH_CHALLENGE
Autonomous agricultural robot built with Raspberry Pi and Python for the Robotics for Good Youth Challenge, featuring mecanum mobility, robotic arm manipulation, and early-stage AI integration.

# CruciBot – Autonomous Agricultural Robot

> Built for the Robotics for Good Youth Challenge 2025–2026  
> Team: **Crucible Lusaka**

---

## Overview

**CruciBot** is an autonomous agricultural robot designed to simulate real-world **precision farming tasks**, including:

- Seed planting
- Selective irrigation triggering
- Fruit harvesting and sorting

This project was developed for the **Robotics for Good Youth Challenge**, which focuses on solving global agricultural challenges through robotics and innovation.

The robot operates fully autonomously within a timed environment, mimicking real-world constraints in modern farming systems.

---

## Key Features

- **Holonomic Movement** using mecanum wheels (multi-directional navigation)
- **Robotic Arm Manipulation** for picking and sorting objects
- **Raspberry Pi Powered** embedded system
- **Autonomous Execution** (no human control during operation)

---

## System Architecture

### Hardware Components
- Raspberry Pi (main controller)
- Mecanum wheel drive system
- Servo-based robotic arm

### 💻 Software Stack
- Python
- GPIO control libraries

---

## How It Works

1. The robot starts in a defined zone and is activated autonomously.
2. It navigates the field using **pre-programmed time-based movement**.
3. The robotic arm:
   - Picks fruits 
   - Sorts them into correct zones
4. The robot interacts with elements such as:
   - Seeds (planting simulation)
   - Irrigation mechanism (trigger-based)

---

## Engineering Challenges & Lessons Learned

One of the most important insights from this project was the limitation of **time-based control systems**.

### Problem:
- The robot relied entirely on **timed movements**
- Battery voltage fluctuations caused:
  - Movement inconsistencies
  - Reduced accuracy
  - Task failures during competition

### Key Lesson:
> Reliable robotics systems must use **sensor feedback and real-time decision-making**, not just pre-programmed timing.

This experience directly shaped our understanding of **control systems, embedded reliability, and AI integration**.

---

## Future Improvements

We plan to significantly upgrade CruciBot into a **fully intelligent autonomous system**:

- Replace time-based control with **sensor-driven navigation**
- Implement **computer vision (OpenCV)** for:
  - Object detection (fruits, plots)
  - Decision-making
- Integrate **AI/ML models** for adaptive behavior
- Add **power management optimization**
- Improve localization and movement accuracy

---

---

## My Contribution

I was responsible for:

- Programming the robot (Python) together with others.
- Hardware integration and wiring
- System design and testing

This project reflects my strong interest in **Mechatronics and AI-embedded systems**.

---

## Real-World Impact

CruciBot represents a step toward:

- Smart farming systems
- Efficient resource usage (water, seeds)
- Automation in agriculture
- Increased productivity in low-resource environments

---

## Conclusion

Although the system faced limitations during competition, it provided a **critical foundation in robotics, embedded systems, and AI integration**.

> This project marks the beginning of building intelligent, real-world robotic systems.

---

## License

MIT License
