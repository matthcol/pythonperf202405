def bazar(a, b, *args,  c=0, d=False, l=None, **kwargs):
    """a function to demonstrate all posibilities to declare arguments

    parameters:
    - a:
    - b:
    ...
    - kwargs: extra args
       * color
       * meteo
       * topic
       NB: in the future, more posibilities 
    """
    for arg in a, b, args, c, d, l, kwargs:
        print(f"arg = {arg}; type={type(arg)}")
    # handle args
    print('args:')
    for arg in args:
        print(f'\t- {arg}')
    # handle kwargs
    print('kwargs:')
    for k, v in kwargs.items():
        print(f'\t- {k}={v}')
        # TODO: if k ?
  
def run(*args, **kwargs):
    print("start running")
    bazar(*args, **kwargs)
    print("end running")
        
if __name__ == '__main__':
    bazar(1, 2, 3, 4, c=4)
    values = [1, 2, 3, 4]
    named_values = { "c": 5, "color": "green"}
    print()
    run(0, *values, l=[1,2,3], **named_values)