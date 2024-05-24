from concurrent.futures import ProcessPoolExecutor, as_completed

# NB: the function to be executed in // must be at the top level (__main__ module)
# main app must be included in a if __name__ == '__main__' block

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibo_wrapper(n):
    return fibo(n)

def main_submit():
    print("Start")
    with ProcessPoolExecutor() as poolExecutor:
        args = reversed(range(5, 31, 5))
        jobs = [ poolExecutor.submit(fibo, arg) for arg in args ]
        print(jobs)
        for job in jobs:
            result = job.result()
            print(f"main: fibo={result}")
    print("Done", end='\n\n')

def main_map():
    print("Start")
    with ProcessPoolExecutor() as poolExecutor:
        args = list(reversed(range(5, 31, 5)))
        for n, result in zip(args, poolExecutor.map(fibo_wrapper, args)):
            print(f"main: n={n}, fibo={result}")
    print("Done", end='\n\n')
    
def main_ascompleted():
    print("Start")
    with ProcessPoolExecutor() as poolExecutor:
        args = reversed(range(5, 31, 5))
        job_arg_dict = {
            poolExecutor.submit(fibo, arg): arg
            for arg in args 
        }
        print(job_arg_dict.keys())
        for job in as_completed(job_arg_dict): # iter on keys i.e. future jobs
            arg = job_arg_dict[job]
            result = job.result() # result is ready
            print(f"main: n={arg}, fibo={result}")
    print("Done", end='\n\n')

# main_map()
if __name__ == '__main__':
    main_map()
    main_submit()
    main_ascompleted()