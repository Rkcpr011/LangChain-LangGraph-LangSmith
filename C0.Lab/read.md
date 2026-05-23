What is Counter in Python?
Counter comes from collections module.
It is like a special dictionary that counts how many times each element appears in a list, string, etc.

from collections import Counter

s = "aabbc"
freq = Counter(s)
print(freq)

Counter({'a': 2, 'b': 2, 'c': 1})


Common Use Cases
A--->.keys() → gives all unique items.
print(freq.keys())   # dict_keys(['a','b','c'])

B--->.values() → gives the counts (how many times each appears).
print(freq.values()) # dict_values([2,2,1])

C-->
Another Counter on values → frequency of frequencies.
freq_count = Counter(freq.values())
print(freq_count)
Counter({2:2, 1:1})
 This means:
The frequency 2 appears twice (two letters occur 2 times each).
The frequency 1 appears once (one letter occurs 1 time).




