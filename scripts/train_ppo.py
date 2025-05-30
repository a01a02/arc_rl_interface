from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from environment.arc_env import ArcEnv

def main():
    env = ArcEnv(use_ros=False) # Training in sim
    check_env(env)

    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=200_000)

    model.save("models/ppo_arc")
    print("Training complete and model saved.")

if __name__ == "__main__":
    main()

