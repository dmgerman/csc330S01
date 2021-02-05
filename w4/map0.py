#!/usr/bin/python3

import dmg

if __name__ == '__main__':
    result = 0
    for i in range(dmg.COUNT):
        result += dmg.do_for_long_time(i)

    print(result, "Memory: ", dmg.memory_used())  # in bytes 
