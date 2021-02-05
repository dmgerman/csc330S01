#!/usr/bin/python3

import functools
import operator
import os
import psutil
import dmg

if __name__ == '__main__':
    print("Memory: ", dmg.memory_used())  # in bytes 

