# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 14:22:46 2019
Cross-entropy algorithm from RL hands on book.
The algorithm is working. In order the animation is more smooth
time.sleep(0.1) is working. Because of that the program can't stop
and runs infinitely. Commenting time.sleep will correct that problem
@author: Anton
"""
from keras.models import Sequential
from keras.losses import sparse_categorical_crossentropy
from keras import backend as K
from keras.models import Model
from keras.layers import Dense, Dropout
from keras.models import load_model
import numpy as np
import gym
import random
import time


def gather_data(env):
    min_score = 50
    min_steps = 500
    trainX, trainY = [], []
    for i in range(10000): #make 1000 episodes
        obs = env.reset()
        #print(obs)
        score = 0
        sampleX, sampleY = [],[] # data of one episode
        for step in range(min_steps):
            action = np.random.randint(0,2)
            hot_action = np.zeros(2)
            hot_action[action] = 1
            sampleX.append(obs)
            sampleY.append(hot_action)
            
            obs, reward, done, info = env.step(action)
            score += reward
            if done:
                break
        if score > min_score:
            trainX += sampleX
            trainY += sampleY
    return np.array(trainX), np.array(trainY)
    
def create_model():
    model = Sequential()
    model.add(Dense(128, input_shape=(4,), activation='relu'))
    model.add(Dropout(0.5))
    
    model.add(Dense(256,activation='relu'))
    model.add(Dropout(0.5))
    
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    
    model.add(Dense(2,activation='softmax'))
    
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    return model
    

        
def main():
    env = gym.make('CartPole-v0')
    #trainX, trainY = gather_data(env)
    #model = create_model()
    #model.fit(trainX, trainY, epochs=20)
    #model.save('ce_fstmodel')
    model = load_model('ce_fstmodel.h5y')
    done = False
    count = 0
    while not done:# or count != 10000:
        env.render()
        obs = env.reset()
        action=np.argmax(model.predict(obs.reshape(1,4)))
        obs = env.step(action)
        #time.sleep(0.1) # Kernel dies because of that
        count += 1
    env.close()
    
    
    
main()