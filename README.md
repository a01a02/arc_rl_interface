# ARC RL Interface

This repository contains:

- `arc_rl_interface/`: ROS package for ARC Pro car reinforcement learning interface
- `scripts/`: PPO training and evaluation scripts
- `data/`: Voronoi map data or other environment files

---

## Project Overview

This project implements reinforcement learning control for ARC Pro robots using:

- Gymnasium + Stable-Baselines3 PPO
- ROS Noetic for real-time control
- Voronoi-based state discretization

---

## Cloning & Build Instructions

### Clone inside your ROS workspace `src/` folder:

```bash
cd ~/arc_rl_ws/src
git clone git@github.com:a01a02/arc_rl_interface.git
cd ~/arc_rl_ws
catkin_make
source devel/setup.bash
