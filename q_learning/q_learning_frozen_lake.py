# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 13:22:00 2020

@author: Anton
"""
import gym
import collections
import time
import tensorflow as tf
from datetime import datetime


ENV_NAME = "FrozenLake-v0"
GAMMA = 0.9
TEST_EPISODES = 20

class Agent:
    def __init__(self):
        self.env = gym.make(ENV_NAME)
        self.state = self.env.reset()
        self.rewards = collections.defaultdict(float)
        self.transits = collections.defaultdict(collections.Counter)
        self.values = collections.defaultdict(float)
        
    def play_n_random_steps(self,count):
        for i in range(count):
            action = self.env.action_space.sample()
            new_state, reward, done, _ = self.env.step(action)
            reward_key = (self.state, action, new_state)
            #if reward_key not in self.rewards:
            self.rewards[reward_key] = reward
            
            self.transits[(self.state, action)][new_state] += 1
            
            self.state = self.env.reset() if done else new_state
       #print(sorted(self.transits.keys()))
            
    def calc_action_value(self, state, action):
        #state_val = str(state) + ":" + str(action) # get key for the pair (action, state)
        vals = self.transits[(state, action)] # get target_state and their counters
        total = sum(vals.values()) # get sum of all counters
        qsa = 0 # accumulating action values
        #print("values are:", self.values)
        for tgstate, count in vals.items():
            #reward_key = str(state)+str(action)+str(tgstate) # get key for reward table
            reward = self.rewards[(state,action,tgstate)]
            qsa += (count/total)*(reward + GAMMA*self.values[tgstate])
        return qsa
    
    def select_action(self, state):
        best_action, best_value = None, None
        for action in range(self.env.action_space.n):
            action_value = self.calc_action_value(state, action)
            if best_value is None or best_value < action_value:
                best_value = action_value
                best_action = action
        return best_action
    
    def play_episode(self,env):
        total_reward = 0.0
        state = env.reset()
        while True:
            #env.render()
            #time.sleep(1)
            action = self.select_action(state)
            new_state, reward, done, _ = env.step(action)
            #reward_key = str(state)+str(action)+str(new_state)
            self.rewards[(state, action, new_state)] = reward
            #trans_key = str(state) + str(action)
            self.transits[(state, action)][new_state] += 1
            total_reward += reward
            if done:
                break
            state = new_state
        return total_reward
    
    def play_final_episode(self, env):
        total_reward = 0.0
        state = env.reset()
        done = False
        while not done:
            env.render()
            time.sleep(1)
            action = self.select_action(state)
            new_state, reward, done, _ = env.step(action)
            total_reward += reward
            state = new_state
    
    def value_iteration(self):
        for state in range(self.env.observation_space.n):
            state_values = [self.calc_action_value(state, action)
                            for action in range(self.env.action_space.n)]
            self.values[state] = max(state_values)
        

now = datetime.now()
logdir = "./logs/" + now.strftime("%Y%m%d-%H%M%S") + "/"  

if tf.gfile.Exists(logdir):
   tf.gfile.DeleteRecursively(logdir) 

writer = tf.summary.FileWriter(logdir)
writer.flush()
          
test_env = gym.make(ENV_NAME)            
agnt = Agent()
best_reward = 0
iteration = 0
while True:
    summary = tf.Summary()

    iteration += 1
    agnt.play_n_random_steps(100)
    agnt.value_iteration()
    reward = 0.0
    for _ in range(TEST_EPISODES):
        reward += agnt.play_episode(test_env)
    reward /= TEST_EPISODES
    if reward > best_reward:
        print("At iteration", iteration, "reward gained is", reward)
        best_reward = reward
    if best_reward >= 0.9:
        print("Problem solved!")
        break
    summary.value.add(tag='reward', simple_value = reward)
    writer.add_summary(summary, iteration)
writer.flush()
agnt.play_final_episode(test_env)
