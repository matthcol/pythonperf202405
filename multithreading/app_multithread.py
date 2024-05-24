from concurrent.futures import ThreadPoolExecutor, as_completed
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
    
    
def main_submit():
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

def main_map():
    with ThreadPoolExecutor(4) as poolExecutor:
        print(poolExecutor._max_workers)
        args = range(5, 31, 5)
        # NB: map is lazy to collect results
        # NB: results are collected with the call order
        # results = list(poolExecutor.map(fibo_wrapper, args))
        # print(results)
        for result in poolExecutor.map(fibo_wrapper, reversed(args)):
            print("main: result:", result)
            
def main_as_completed():
    with ThreadPoolExecutor(4) as poolExecutor:
        print(poolExecutor._max_workers)
        args = reversed(range(5, 31, 5))
        jobs_n = { 
            poolExecutor.submit(fibo_wrapper, n): n
            for n in args    
        }
        print("Jobs started:", [future.running() for future in jobs_n ])
        for job in as_completed(jobs_n):
            n = jobs_n[job]
            result = job.result()
            print(f"main: n={n}, fibo={result}")
    
# main_submit()
# main_map()
main_as_completed()
    