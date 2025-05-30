# arc_rl_interface

ROS package + RL training code to control ARC Pro autonomous cars using reinforcement learning with Voronoi-based state discretization.

## Structure
- `src/arc_rl_interface/`: ROS package
- `scripts/`: PPO training code
- `data/`: Voronoi map data

## Usage
Clone into your ROS workspace `src/` directory, rebuild with `catkin_make`, and train using provided PPO scripts.
