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
        if self.dir == 'NORTH':
            if self.y in range(0,4):
                self.y += 1
            else:
                print("Robot will fall off the table on this move")
        elif self.dir == 'SOUTH':
            if self.y in range(1,5):
                self.y -= 1
            else:
                print("Robot will fall off the table on this move")
        elif self.dir == 'EAST':
            if self.x in range(0,4):
                self.x += 1
            else:
                print("Robot will fall off the table on this move")
        elif self.dir == 'WEST':
            if self.x in range(1,5):
                self.x -= 1
            else:
                print("Robot will fall off the table on this move")
   
    def left(self):
        if self.dir == 'NORTH':
            self.dir = 'WEST'
        elif self.dir == 'SOUTH':
            self.dir = 'EAST'
        elif self.dir == 'WEST':
            self.dir = 'SOUTH'
        elif self.dir == 'EAST':
            self.dir = 'NORTH'
    
    def right(self):
         if self.dir == 'NORTH':
            self.dir = 'EAST'
         elif self.dir == 'SOUTH':
            self.dir = 'WEST'
         elif self.dir == 'WEST':
            self.dir = 'NORTH'
         elif self.dir == 'EAST':
            self.dir = 'SOUTH'
    
    def report(self):
        print(self.x,self.y,self.dir)
        return {'x':self.x, 'y':self.y, 'dir': self.dir}
 
robot = Robot(0,0,'NORTH')
current_position = robot.report()
robot.move()
current_position = robot.report()
robot.left()
current_position = robot.report()
robot.move()
current_position = robot.report()
robot.right()
current_position = robot.report()
robot.move()
current_position = robot.report()

robot.place(2,2,'WEST')
current_position = robot.report()
robot.right()
current_position = robot.report()






