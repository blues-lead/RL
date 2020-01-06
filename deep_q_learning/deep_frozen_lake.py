# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 14:30:24 2020

@author: Anton
"""
import gym
import collections
import tensorflow as tf
from datetime import datetime

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
            action_value = self.values[(state, action)]
            if best_value is None or best_value < action_value:
                best_value = action_value
                best_action = action
        return best_value, best_action
    
    def value_update(self, s, a, r, next_s):
        best_v, _ = self.best_value_action(next_s)
        l_part = (1-ALPHA)*self.values[(s,a)]
        r_part = ALPHA*(r + GAMMA*best_v)
        self.values[(s,a)] = l_part + r_part
        
    def play_episode(self, env):
        state = env.reset()
        total_reward = 0.0
        done = False
        for i in range(TEST_EPISODES):
            _,action = self.best_value_action(state)
            new_state, reward, done, _ = env.step(action)
            total_reward += reward
            state = new_state
            if done:
                break
        return total_reward
        
        
    
    
def main():
    now = datetime.now()
    logdir = "./logs/" + now.strftime("%Y%m%d-%H%M%S") + "/"
    writer = tf.summary.FileWriter(logdir)
    env = gym.make(ENV_NAME)
    agnt = Agent()
    iteration = 0
    best_reward = 0.0
    while True:
        iteration += 1
        summary = tf.Summary()
        reward = 0.0
        os, a ,r, ns = agnt.sample_env()
        agnt.value_update(os, a, r, ns)
        for i in range(TEST_EPISODES):
            reward += agnt.play_episode(env)
        reward /= TEST_EPISODES
        if reward > best_reward:
            best_reward = reward
            print("Gained best reward:", best_reward)
        summary.value.add(tag='reward', simple_value = reward)
        writer.add_summary(summary, iteration)
        if best_reward > 0.9:
            break
    
main()
