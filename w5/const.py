#!/usr/bin/python
import os
import psutil

last = 50000000

def memory_used():
    process = psutil.Process(os.getpid())
    print ("Memory used: {:.2f} megs".format(process.memory_info().rss/1e6))
    print("For size ", 50000000/1000000, " M")


import atexit

#atexit.register(memory_used)
