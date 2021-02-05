import os
import psutil

COUNT=10000

m = 100
baseline = 12185600

def do_for_long_time0(n):
    total = 0.0
    for i in range(0,m):
        for j in range (0,m):
            total += i * j
    return total * n

def do_for_long_time(n):
    return sum ([i*j for i in range(m) for j in range(m)]) * 1.0 * n

def memory_used():
    process = psutil.Process(os.getpid())
    return (process.memory_info().rss-baseline)
