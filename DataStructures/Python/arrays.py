# from array import array

from typing import List


l: List = ["a",'b','c','d']

l.append("a")
l.extend([0,1,2,4,5,])
l.insert(5,'e')

print(l.pop(0))
print(l)
