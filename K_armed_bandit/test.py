# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:37:17 2019

@author: Anton
"""

from four_arm_class import KArmBandit
import numpy as np
from random import randrange
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


plt.style.use('seaborn-whitegrid')

def main():
    n_arms = 4
    arms = []
    df_arms = []
    np.random.seed(None)
    mus = np.random.normal(100, 50, 4)
    sigmas = np.random.normal(20, 5, 4)
    for i in range(n_arms):
        arms.append(np.random.normal(mus[i], sigmas[i],1000))
    classes = ['arm1','arm2','arm3','arm4']
    for i in range(n_arms):
        df_arms.append(pd.DataFrame({'score':arms[i], 'class':classes[i]}))
    score_data = pd.concat(df_arms)
    sns.boxplot(x='class', y='score', data=score_data)    
    
main()