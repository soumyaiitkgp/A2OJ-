# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:19 2019

@author: Predator
"""
n = int(input())
m= []
a,b,c = 0,0,0

for i in range(n):
    t = int(input())
    num = input().split()
    ct = 0
    for j in range(t):
        p = num[j]
        if p[0] != chr(35):
            ct = 1
            x = j
            a = num[0:x]
            b = num[x]
            c = num[x+1:t]
            a_string = ' '.join(a)
            c_string = ' '.join(c)
            if c == []:
                x = b + ' ' + a_string
            else:
                x = c_string + ' ' + b + ' ' + a_string
 
        elif ct == 0:
            x = ' '.join(num)
    m.append(x)
    
for i in range(n):
    print(m[i])