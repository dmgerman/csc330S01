#!/usr/bin/python3

import const
import operator
import functools

lst = map (lambda x: x * x, filter(lambda x: x % 2 == 0, range(const.last)))
out = sum(lst)

print(out)

print(const.memory_used())



