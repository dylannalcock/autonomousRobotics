# Part 1: Getting Started with Autonomous Robots

Welcome to the first part of my journey into the world of autonomous robots. In this section, I'll walk you through the key aspects of this project, which aims to familiarize me with the MuSHR platform and the software tools necessary for building a self-driving robot.

## Project Overview
The overarching goal of this project is to develop the skills and knowledge required to create a self-driving robot. To achieve this, I'll be working with the MuSHR platform and diving into the world of Robot Operating System (ROS). This first part serves as the foundation for subsequent phases.

## 1. Setting Up the Virtual Machine
To kick things off, I began by setting up a virtual machine environment. This step ensures that I have the necessary tools and software to work on the project. The virtual machine is configured to meet the project's requirements, and I've logged in using the provided credentials.

## 2. Getting Started with ROS
ROS, the Robot Operating System, is the backbone of this project. It's not an actual operating system but rather a middleware framework extensively used in robotics. Here's what I've learned about ROS:

- ROS facilitates interprocess communication in robotics platforms.
- ROS organizes code into packages, containing executables, libraries, and other resources.
- Development in ROS is structured within workspaces, allowing me to manage multiple packages efficiently.

## 3. Running the MuSHR Car in Simulation
This part of the project allowed me to run the MuSHR simulator and visualize the robot's movements in a virtual environment. It's a crucial step as it allows for quick testing and validation without the risk of real-world mishaps.

## 4. Testing Instructions
To ensure the correctness of my code and implementations, various tests have been provided for different project tasks. Here's a summary of the testing process:

- Q1: Your First Publisher Node: Fibonacci
  - Q1.1: I implemented the Fibonacci calculation algorithm.
  - Q1.2: I interfaced with ROS, ensuring the node publishes Fibonacci numbers.
  - Q1.3: I created a launch file for easier node execution.

- Q2: Your First Subscriber: PoseListener
  - Q2.1: I calculated the Euclidean norm using standard Python for loops.
  - Q2.2: I optimized the norm calculation using NumPy for efficiency.
  - Q2.3: I initialized a subscriber for car pose data.
  - Q2.4: I processed car pose messages to extract relevant information.
  - Q2.5: I collected and visualized data, creating plots of car locations and distances.

- Q3: Advanced Indexing with NumPy
  - Q3.1: I used integer array indexing for specific tasks.
  - Q3.2: I applied Boolean array indexing to perform tasks efficiently.

Throughout the testing process, I aimed to ensure the functionality and efficiency of my code.

By completing Part 1 of this Autonomous Robots Project, I've gained valuable knowledge and practical skills that will be instrumental in building a self-driving robot in the subsequent project phases. This marks the first step on my exciting robotics journey!
