# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:34:01 2024

@author: Meshewa
"""

#dictionary
Lookup={
"ID":101,
"Firstname":"Daniel-Caleb",
"Lastname":"Cheruiyot"
}
x=Lookup.values()
print(x)


#Dictionary to store five counties then display them(keys and values)
Y={"C1":"Mombasa","C2":"Kilifi","C3":"Taita taveta","C4":"Lamu","C5":"Kericho"}
x=Y.values()
print(x)
print("\nDisplay pairs")
for i in Y.items():
    print(i)
