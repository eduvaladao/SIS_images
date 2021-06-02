"""
Funções importantes do pêndulo duplo

Autor: Eduardo da Costa Valadão - eduardovaladao98@gmail.com
""" 
import numpy as np

def pendulum_x1(theta1, l1, i):
    x1 = l1*np.sin(theta1[i])
    return x1 

def pendulum_y1(theta1, l1, i):
    y1 = - l1*np.cos(theta1[i])
    return y1 

def pendulum_x2(theta2, l2, x1, i):
    x2 = x1[i] + l2*np.sin(theta2[i])
    return x2

def pendulum_y2(theta2, l2, y1, i):
    y2 = y1[i] - l2*np.cos(theta2[i])
    return y2 
