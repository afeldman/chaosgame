#!/usr/bin/env python3

import random
from tkinter import *
import math
import numpy as np

canvas_width = 1000
canvas_height = 700
    
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(y-r, x-r, y+r, x+r, **kwargs)

def distance(v1, v2):
    return np.linalg.norm(v1 - v2)

point_12=np.array([canvas_height/7.0,
                   canvas_width/8.0])
point_34=np.array([canvas_height*6.0/7.0,
                   canvas_width/2.0])
point_56=np.array([canvas_height/7.0,
                   canvas_width*7.0/8.0])

dpoints = []

tmp_point = np.array([random.randint(1,canvas_width),
                      random.randint(1,canvas_height)])

dpoints.append(tmp_point)

loop_count = 100000

k=np.array([0.0,0.0])

while loop_count > 0:

    rand_ = random.randint(1,6)
    
    if ((rand_ == 1) or (rand_ == 2)):
        dist = distance(tmp_point,point_12)
        k=point_12
    if ((rand_ == 3) or (rand_ == 4)):
        dist = distance(tmp_point,point_34)
        k=point_34
    if ((rand_ == 5) or (rand_ == 6)):
        dist = distance(tmp_point,point_56)
        k=point_56
       
    #print(np.subtract(k,tmp_point))
   # print(np.divide(np.subtract(k,tmp_point),2))
   
    tmp_point = np.divide(k + tmp_point,2)
    
    dpoints.append(tmp_point)
    
    loop_count = loop_count - 1
    
master = Tk()
master.title("Chaos Game")

w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
Canvas.create_circle = _create_circle

w.create_circle(point_12[0], point_12[1], 5, fill="green",  width=1)
w.create_circle(point_34[0], point_34[1], 5, fill="green",  width=1)
w.create_circle(point_56[0], point_56[1], 5, fill="green",  width=1)

for member in dpoints:
#    print(member)
    w.create_circle(member[0], member[1], 1, fill="blue",  width=1)
    #w.show()
    
w.pack()

mainloop()



