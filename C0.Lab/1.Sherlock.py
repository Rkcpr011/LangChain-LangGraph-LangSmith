#!/bin/python3

import os
from collections import Counter



def isValid(s):
    freq = Counter(s)  #it will return the frequency of each charin the string.
    print(freq)  
    print(type(freq))        
    values = list(freq.values())
    print(f'frequency of each char in sequence:{values}')
   
    print(f'lenght of set of values:{len(set(values))}')
     # Case 1: all frequencies same
    if len(set(values)) == 1:     #meaning only same number of charachter present in string.
        return "YES"
    
    # Case 2: allow one removal
    freq_count = Counter(values)
    print(freq_count)
    print(f'+++++++++++++:{len(freq_count)}')
    if len(freq_count) == 2:
        f1, f2 = freq_count.keys()
        if (freq_count[f1] == 1 and (f1 - 1 == f2 or f1 == 1)):
            return "YES"
        if (freq_count[f2] == 1 and (f2 - 1 == f1 or f2 == 1)):
            return "YES"
    
    return "NO"

res=isValid("abbccccdddddeeeee")
print(res)