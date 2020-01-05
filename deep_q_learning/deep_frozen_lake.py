# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 14:30:24 2020

@author: Anton
"""
import gym
import collections
import tensorflow as tf

ENV_NAME = "FrozenLake-v0"
GAMMA = 0.9
ALPHA = 0.2
TEST_EPISODES = 20

class Agent:
    def __init__(self):
        self.env = gym.make(ENV_NAME)
        self.state = self.env.reset()
        self.values = collections.defaultdict(float)
        
    def sample_env(self):
        action = self.env.action_space.sample()
        old_state = self.state
        new_state, reward, done, _ = self.env.step(action)
        self.state = self.env.reset() if done else new_state
        return (old_state, action, reward, new_state)
    
    def best_value_action(self, state):
        best_action, best_value = None, None
        for action in range(self.env.action_space.n):
            action_value = self.values.get[(state, action)]
            if best_value is None or best_value < action_value:
                best_value = action_value
                best_action = action
        return best_value, best_action
    
    def value_update(self, s, a, r, next_s):
        
    
    
def main():
    %load_ext tensorboard
    
main()
