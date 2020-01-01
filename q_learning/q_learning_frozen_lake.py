# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 13:22:00 2020

@author: Anton
"""
import gym

ENV_NAME = "FrozenLake-v0"
GAMMA = 0.9
TEST_EPISODES = 20

class Agent:
    def __init__(self):
        self.env = gym.make(ENV_NAME)
        self.state = self.env.reset()
        self.rewards = {}
        self.transits = {}
        self.values = {}
        
    def play_n_random_steps(self,count):
        for i in range(count):
            action = self.env.action_space.sample()
            new_state, reward, done, _ = self.env.step(action)
            reward_key = str(self.state)+str(action)+str(new_state)
            if reward_key not in self.rewards:
                self.rewards[reward_key] = reward
            
            transit_key = str(self.state)+str(action)
            if transit_key not in self.transits:
                self.transits[transit_key] = {new_state : 1}
            else:
                if new_state in self.transits[transit_key]:
                    self.transits[transit_key][new_state] += 1
                else:
                    self.transits[transit_key][new_state] = 1
            
            self.state = self.env.reset() if done else new_state
            
    def calc_action_value(self, state, action):
        state_val = str(state) + str(action) # get key for the pair (action, state)
        vals = self.transits[state_val] # get target_state and their counters
        total = sum([t for t in vals.values()]) # get sum of all counters
        qsa = 0 # accumulating action values
        for tgstate, count in vals.items():
            reward_key = str(state)+str(action)+str(tgstate) # get key for reward table
            qsa += (count/total)*(self.rewards[reward_key] + GAMMA*self.values(tgstate))
        return qsa
            
            
agnt = Agent()
agnt.play_n_random_steps(100)
test = agnt.calc_action_value(1,0)
print(test)