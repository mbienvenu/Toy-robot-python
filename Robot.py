# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 12:37:06 2018

@author: cecil
"""

import numpy as np
import pandas as pd

class Robot():
    def __init__(self,x,y,dir):
        self.x = x 
        self.y = y
        self.dir = dir 
        
    def place(self,x,y,dir):
        self.x = x 
        self.y = y
        self.dir = dir 
    
    def move(self):
        pass
    
    def left(self):
        pass
    
    def right(self):
        pass
    
    def report(self):
        print(self.x,self.y,self.dir)
        return {'x':self.x, 'y':self.y, 'dir': self.dir}
 


robot = Robot(0,0,'NORTH')
current_position = robot.report()
robot.move()
robot.left()
robot.right()
robot.place(0,1,'north')






