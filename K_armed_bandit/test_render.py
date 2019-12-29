# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 14:22:46 2019

@author: Anton
"""

import gym
env = gym.make('CartPole-v0')
env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
env.close()