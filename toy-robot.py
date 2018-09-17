# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 01:22:38 2018

@author: cecil
"""


import numpy as np
import pandas as pd
import sys
import os

class Robot():
    def __init__(self):
        pass
        
    def place(self,x,y,dir):
        if x in range(0,5) and y in range(0,5):        
            self.x = x 
            self.y = y
            self.dir = dir 
        else:
            print("Robot is not placed in the right bounds of the table")
    
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
        print(self.x,',',self.y,',',self.dir)
        return {'x':self.x, 'y':self.y, 'dir': self.dir}
    


def main():  
   filepath = sys.argv[1]
   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
   robot = Robot()
   with open(filepath) as fp:
       for line in enumerate(fp):
           if line[1].rstrip() == 'REPORT':
               current_position = robot.report()
           elif line[1].rstrip() == 'MOVE':
               robot.move()
           elif line[1].rstrip() == 'RIGHT':
               robot.right()
           elif line[1].rstrip() == 'LEFT':
               robot.left()
           elif line[1].rstrip().split(' ')[0] == 'PLACE':
               placebot = line[1].rstrip().split(' ')[1]
               robot.place(int(placebot.split(',')[0]),int(placebot.split(',')[1]),
                           placebot.split(',')[2])

if __name__ == '__main__':  
   main()
