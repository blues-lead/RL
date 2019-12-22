# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:28:16 2019

@author: Anton
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import randrange
import seaborn as sns
plt.style.use('seaborn-whitegrid')

class KArmBandit:
    def __init__(self, arms=10):
        if arms > 0:
            self.narms = arms
        else:
            print("Error arms!")
            return
        self.q_table = np.zeros((1,self.narms))
        self.mus = []
        self.sigmas = []
        self.slots = []
        self.classes = ['arm'+str(n) for n in range(self.narms)]
        self.score_data = 0
        
    def generate_data(self, mus, sigmas, quantity):
        df_arms = []
        np.random.seed(None)
        for i in range(self.narms):
            self.slots.append(mus[i],sigmas[i],quantity)
        for i in range(self.narms):
            df_arms.append(pd.DataFrame({'score':self.slots[i], 'class':self.classes[i]}))
        self.score_data = pd.concat(df_arms)
        
    def show_boxplot(self):
        sns.boxplot(x='class', y='score', data=self.score_data)
        
        
        
        
        
        