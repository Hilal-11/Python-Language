import math
# mathh predefine functions
# The min() and max() functions can be used to find the lowest or highest value in an iterable

max_val = max(10 , 20  , 40)
min_val = min(90, 12 , 21)

print(max_val)
print(min_val)

# The abs() function returns the absolute (positive) value of the specified number
abs_val = abs(-88.44)
print(abs_val)

# The pow(x, y) function returns the value of x to the power of y (xy)

n = 4
m = 4
pow_val = pow(n , m)
print(pow_val) 


# math.ceil(x)	 
# math.floor(x)	
# math.fabs(x)
# math.gcd(x, y)

print(math.ceil(10.4))
print(math.ceil(10.5))

print(math.floor(10.4))
print(math.floor(10.6))

print(math.gcd(12 , 24))



# math.sqrt(x)	
# math.pow(x, y)	
# math.log(x, base)	
# math.log10(x)

print(math.sqrt(25))
print(math.pow(2 , 6))
print(math.log(10 , 2))


# math.isfinite(x)	
# math.isinf(x)	
# math.isnan(x)

print(math.isfinite(10))
print(math.isinf(2))