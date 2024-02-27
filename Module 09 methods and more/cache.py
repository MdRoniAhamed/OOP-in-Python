import time
from functools import cache

# 1 , 1, 2, 3, 5, 8, 13, 21
@cache
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

s = time.time()
for i in range(900):
    print(i, fib(i))

e = time.time()

mili_seconds = (e-s) * 1000

print('time took', mili_seconds)