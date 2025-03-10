import time



# def cache(func):
#     cache_value = {}
#     print(cache_value)
#     def wrapper(*args) :
#         result = func(*args)
#         cache_value[args] = result
#         return result
#     return wrapper
    

# @cache
# def long_runner(x , y) :
#     time.sleep(4)
#     return x + y

# print(long_runner(10 , 11))
# print(long_runner(10 , 11))





def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args) :
        if args in cache_value :
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper
    

@cache
def long_runner(x , y) :
    time.sleep(4)
    return x + y

print(long_runner(10 , 11))
print(long_runner(10 , 11))
