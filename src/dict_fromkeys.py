'''
Created on Jul 2, 2014

@author: viejoemer

HowTo use dict.fromkeys in Python?

¿Cómo utilizar dict.fromkeys en Python?

The method fromkeys() creates a new dictionary with 
keys from seq and values set to value.
'''

#This is the tuple of values which would be used for dictionary keys preparation.
seq = ("one", "two", "three")

#Using fromkeys method from dict (keys)
d = dict.fromkeys(seq)
print(d)

#Using fromkeys method from dict (keys, values)
d = dict.fromkeys(seq,10)
print(d)