#!/bin/python3

import math
import os
import random
import re
import sys

def minimumBribes(q):
    bribe=0
    for i in range(len(q)):
        if q[i]-(i+1)>2:
            print("Too chaotic")
            return
            
        for j in range(max(0,q[i]-2),i):
            if q[j]>q[i]:
                bribe=bribe+1
                
    print(bribe)        


    res=minimumBribes(q)
    print(res)
