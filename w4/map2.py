#!/usr/bin/python3

import functools
import operator
import dmg


if __name__ == '__main__':
    

    lst = map(dmg.do_for_long_time, range(dmg.COUNT))

    result = functools.reduce(lambda x,y : x + y, lst, 0)
    
    print(result, "Memory: ", dmg.memory_used())  # in bytes 

