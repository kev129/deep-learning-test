import gym
import random

env = gym.make('CartPole-v0')
states = env.observation_space.shape[0]
actions = env.action_space.n
