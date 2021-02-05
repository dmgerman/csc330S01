#!/usr/bin/python3

from multiprocessing import Pool
import operator
import functools
import dmg


if __name__ == '__main__':
    with Pool(8) as p:
        lst = p.map(dmg.do_for_long_time, range(dmg.COUNT))
        result = functools.reduce(operator.add, lst, 0)
        print(result, "Memory: ", dmg.memory_used())  # in bytes 
    


