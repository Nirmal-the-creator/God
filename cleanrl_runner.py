import gym
import torch
import time

def run_ppo(log_callback=None, episodes=10):
    env = gym.make("CartPole-v1")
    obs = env.reset()
    for ep in range(episodes):
        total_reward = 0
        done = False
        while not done:
            action = env.action_space.sample()  # Dummy random action (replace with PPO policy)
            obs, reward, done, info = env.step(action)
            total_reward += reward
            time.sleep(0.1)  # Simulate processing
        if log_callback:
            log_callback(f"Episode {ep+1}: Reward = {total_reward}")
    env.close()
