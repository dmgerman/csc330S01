#!/usr/bin/python3

import const
import operator
import functools

sum = 0
for x in range(const.last):
    if x % 2 == 0:
        sum = sum + x * x

print(sum)




