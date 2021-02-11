#!/usr/bin/python3

import const

lst = []
for x in range(const.last):
    if x % 2 == 0: 
        lst.append(x*x)

out = sum(lst)

print(out)


