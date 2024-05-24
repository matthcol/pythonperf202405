from concurrent.futures import ThreadPoolExecutor
from functools import wraps

def debug(func):
    @wraps(func)
    def debug_wrapper(*args, **kwargs):
        print(f"function {func.__name__} called with args: {args} and kwargs {kwargs}")
        res = func(*args, **kwargs)
        print(f"result: {res}")
        return res
    return debug_wrapper

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

@debug
def fibo_wrapper(n):
    return fibo(n)
    
    
def main():
    with ThreadPoolExecutor(4) as poolExecutor:
        print(poolExecutor._max_workers)
        futures = []
        for n in 5, 10, 15, 20, 25, 30:
            futures.append(poolExecutor.submit(fibo_wrapper, n))
        print("Jobs started:", [future.running() for future in futures ])
        results = [ future.result() for future in futures ]
        print(results)
    # exit cm: poolExecutor.shutdown()
    # - wait all threads to be terminated
    
main()
    