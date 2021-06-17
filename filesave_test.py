# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 13:24:21 2021

@author: kalle
"""
import matplotlib.pyplot as plt
import numpy as np
import os


def plotter(data):
    
    if (os.path.exists(os.path.abspath('../../')+'/git_test')):
        print("exists")
    else:
        os.mkdir(os.path.abspath('../../')+'/git_test')
    
    outFilepathDR = os.path.abspath('../../') + "/git_test/testpic.png"
    print(data)
    labels = data[0]
    rewards = data[1]
    penalties = data[2]
    
    
    fig, ax = plt.subplots()
    ax.scatter(penalties,rewards)
    ax.plot(penalties,rewards)
    
    for i, txt in enumerate(labels):
        ax.annotate("R"+ str(int(txt)), (penalties[i], rewards[i]))
    fig.savefig(outFilepathDR)
    plt.close()
    
    
def ranDataMaker():
    datasheet = np.empty(shape=(3,5))
    for i in range(0,5):
        name = (i+1)*10
        value1 = np.random.randint(name,60) * name
        value2 = np.random.randint(i,12) * name
        
        datasheet[0,i] = name
        datasheet[1,i] = value1
        datasheet[2,i] = value2
        
    return datasheet


randomdata = ranDataMaker()

plotter(randomdata)