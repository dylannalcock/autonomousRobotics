# Crafting Self-Driving Autonomy

## Project Overview
"Crafting Self-Driving Autonomy" represents a journey of hands-on exploration and coding in the realm of autonomous robotics with our team of 4 members. This project delves into the intricacies of designing and programming a self-driving robot using cutting-edge technologies and frameworks.

Throughout the project, we have tackled various facets of autonomous robotics, including sensor integration, localization, path planning, and control systems. Leveraging the MuSHR rally car platform, we have gained practical experience in implementing and fine-tuning these critical components.

By the project's completion, we have achieved the following milestones:

1. Successfully integrated sensors and perception systems to gather data from the robot's environment.
2. Implemented robust localization algorithms to enable precise self-positioning.
3. Designed and optimized path planning strategies for safe and efficient navigation.
4. Developed responsive control systems to execute planned trajectories.
5. Conducted rigorous testing and debugging, ensuring the reliability of the self-driving robot.
6. Demonstrated the entire autonomous system on real hardware, validating its functionality.

This project encapsulates our journey of mastering the art and science of self-driving robot development through hands-on coding and experimentation.

## Part 1: Getting Started with Autonomous Robots

Welcome to the first part of our journey into the world of autonomous robots. In this section, we'll walk you through the key aspects of this project, which aims to familiarize us with the MuSHR platform and the software tools necessary for building a self-driving robot.

## Project Overview
The overarching goal of this project is to develop the skills and knowledge required to create a self-driving robot. To achieve this, we'll be working with the MuSHR platform and diving into the world of Robot Operating System (ROS). This first part serves as the foundation for subsequent phases.

## 1. Setting Up the Virtual Machine
**Directory: ~/dependencies_ws/**
To kick things off, we began by setting up a virtual machine environment. This step ensures that we have the necessary tools and software to work on the project. The virtual machine is configured to meet the project's requirements, and we've logged in using the provided credentials.

## 2. Getting Started with ROS
**Directories: ~/dependencies_ws/ and ~/mushr_ws/**
ROS, the Robot Operating System, is the backbone of this project. It's not an actual operating system but rather a middleware framework extensively used in robotics. Here's what we've learned about ROS:

- ROS facilitates interprocess communication in robotics platforms.
- ROS organizes code into packages, containing executables, libraries, and other resources.
- Development in ROS is structured within workspaces, allowing us to manage multiple packages efficiently.

## 3. Running the MuSHR Car in Simulation
**Directories: ~/mushr_ws/**
This part of the project allowed us to run the MuSHR simulator and visualize the robot's movements in a virtual environment. It's a crucial step as it allows for quick testing and validation without the risk of real-world mishaps.

## 4. Testing Instructions
**Directories: ~/mushr_ws/src/mushr478/**
To ensure the correctness of our code and implementations, various tests have been provided for different project tasks. Here's a summary of the testing process:

- Q1: Your First Publisher Node: Fibonacci
  - Q1.1: We implemented the Fibonacci calculation algorithm.
  - Q1.2: We interfaced with ROS, ensuring the node publishes Fibonacci numbers.
  - Q1.3: We created a launch file for easier node execution.

- Q2: Your First Subscriber: PoseListener
  - Q2.1: We calculated the Euclidean norm using standard Python for loops.
  - Q2.2: We optimized the norm calculation using NumPy for efficiency.
  - Q2.3: We initialized a subscriber for car pose data.
  - Q2.4: We processed car pose messages to extract relevant information.
  - Q2.5: We collected and visualized data, creating plots of car locations and distances.

- Q3: Advanced Indexing with NumPy
  - Q3.1: We used integer array indexing for specific tasks.
  - Q3.2: We applied Boolean array indexing to perform tasks efficiently.

Throughout the testing process, we aimed to ensure the functionality and efficiency of our code.

By completing Part 1 of this Autonomous Robots Project, we've gained valuable knowledge and practical skills that will be instrumental in building a self-driving robot in the subsequent project phases. This marks the first step on our exciting robotics journey!

# Part 2 README: MuSHR Car Localization with Particle Filter

## Overview
In this project phase, we've implemented a Particle Filter algorithm for localizing the MuSHR car. The Particle Filter is a probabilistic technique used to estimate the car's precise position and orientation within a known map based on sensor measurements and control inputs. This phase involved several key components and tasks, all aimed at improving the accuracy of the car's localization.

### Particle Filter Components
Throughout this phase, we've worked on various aspects of the Particle Filter localization:

1. **Particle Initialization**: We initiated the Particle Filter by sampling particles from a Gaussian distribution, which represents our initial belief about the car's pose. This code can be found in the `particle_initializer.py` file within the `src/localization` directory.

2. **Motion Model**: We implemented the kinematic car motion model in the `motion_model.py` file. This model predicts how the car's state changes in response to control inputs (velocity and steering angle). This code can be found in the `src/localization/motion_model.py` directory.

3. **Sensor Model**: The LIDAR sensor model was a crucial component. It calculates the likelihood of sensor measurements given the current car state and map. The sensor model incorporates different modes such as hit, short, max, and random measurements. You can find the implementation of the sensor model in the `sensor_model.py` file within the `src/localization` directory.

4. **Resampling**: To improve the accuracy of the Particle Filter, we implemented low-variance resampling in the `resampler.py` file. This process selects high-probability particles for the next iteration while discarding low-probability ones, which helps the filter converge to the true state. You can find this code in the `src/localization/resampler.py` directory.

## What We've Accomplished
Here's a summary of what we've accomplished in this project phase:

- **Workspace Setup**: We ensured that our ROS workspace and dependencies were correctly set up to work on this part of the project.

- **Parameter Tuning**: We spent time tuning parameters for both the motion model and sensor model to ensure they closely matched the actual behavior of the MuSHR car and its LIDAR unit. These parameters are located in the `config/parameters.yaml` file.

- **Particle Filter Implementation**: We successfully implemented the Particle Filter algorithm, allowing the car to estimate its pose based on sensor data and control inputs.

- **Simulation Testing**: We thoroughly tested the Particle Filter in simulation environments, using teleoperation and recorded bag files. These tests helped us evaluate the accuracy of our localization and validate our parameter tuning efforts.

- **Real-world Testing**: After verifying the performance in simulations, we transferred our code to the physical MuSHR car. We conducted real-world tests and recorded bag files while driving the car

 around the lab space.

## Relevant Directories
Recruiters and reviewers can find the relevant code and implementations in the following directories:

- **Particle Initialization**: `src/localization/particle_initializer.py`
- **Motion Model**: `src/localization/motion_model.py`
- **Sensor Model**: `src/localization/sensor_model.py`
- **Resampling**: `src/localization/resampler.py`
- **Parameter Tuning**: `config/parameters.yaml`

By examining the code in these directories, you can gain a deeper understanding of our team's contributions to this project and how we implemented the Particle Filter localization for the MuSHR car.
