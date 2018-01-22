# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 16:33:32 2018

@author: d.voskresenskiy
"""
blen = 22
num = 3
start = (num-1)*9
stop = blen if blen <= num*9 else num*9
print(str(start//9+1-num) + " " + str(stop%9-1))