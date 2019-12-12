# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:28:16 2019

@author: Anton
"""
import numpy as np

class KArmBandit:
    def __init__(self, arms):
        self.narms = 0
        if arms > 0:
            self.narms = arms
        else:
            print("Error arms!")
            return
        self.rewards = [0]*self.narms
        
    def generate_rewards(self, mus, sigmas):
        if len(mus) != len(sigmas):
            print("Error size of mus and sigmas!")
            return []
        i = 0
        for m,s in zip(mus,sigmas):
            self.rewards[i] = np.random.normal(m,s)
            i += 1
        return self.rewards
        
        
        