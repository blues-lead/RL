# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:37:17 2019

@author: Anton
"""

from four_arm_class import KArmBandit
import numpy as np
from random import randrange

def main():
    bandit = KArmBandit(4)
    mus = np.array(([1,2,1,1]))
    sigmas = np.array(([0.5,1.5,2.0,1.01]))
    #test = bandit.generate_rewards(mus,sigmas)
    mu_rewards = [0]*4
    #IMPLEMENT select arm in the class
    
main()