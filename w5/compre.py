#!/usr/bin/python3

import const

lst  = [ x * x for x in range(const.last) if x % 2 == 0]

out = sum(lst)

print(out)

