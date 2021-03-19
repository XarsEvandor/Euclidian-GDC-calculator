#!/usr/bin/env python
# coding: utf-8

# In[62]:
import math

x = 100001
y = 1001
conf = math.gcd(x,y)

while y != 0:
    print(str(x) + " = " + str(y) + " * " + str(x//y) + " + " + str(x%y))
    r = x%y
    x = y
    y = r

print("GCD --> " + str(x))
print("Confirmation --> " + str(conf))

