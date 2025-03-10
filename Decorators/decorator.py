import time
def timer(fx) :
    def wrapper(*args , **kwargs) :
        start = time.time()
        result = fx(*args , **kwargs)
        end = time.time()
        print(f"{fx.__name__} runs in {end-start}")
        return result
    return wrapper

@timer
def example_function(n) :
    time.sleep(n)
    
example_function(2)   

@timer
def find_factorial(n):
    time.sleep(n)
find_factorial(4)     