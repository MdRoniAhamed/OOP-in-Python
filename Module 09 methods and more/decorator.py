import math,time
def timer(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        print("Start")
        func(*args, **kwargs)
        t2 = time.time()
        print(f'Time different: {t2-t1}')
    return inner

@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f'factorial {n} result: {result}')

# timer(get_factorial)()
get_factorial(2000)
    
