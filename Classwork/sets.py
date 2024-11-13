# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:17:18 2024

@author: Meshewa
"""

set1={1,2,3,5,10,8}
set2={"w", "e", "f"}
print("Set1=",set1)
set1.update(["g","h"])
print("Set2=",set2)
set2.update([4,7])
set1.add(11)
set2.add("k")
print("Set1=",set1)
print("Set2=",set2)
set1.discard(5)
set2.remove("e")
print(len(set2))
print(set1.union(set2))