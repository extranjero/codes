int1 = 1
int2 = 10

del int1, int2

## Numeric types
# python suppports 4 numeric types
# int (signed integers) Ex: 10
# long (long integers) Ex: 51924361L
# float (floating point real values) Ex: 0.0
# complex (complex numbers) Ex: 3.14j

## Number type conversions

int(0.0)
long(10)
float(105)
complex(10.1)

## Math functions
abs(x) # The absolute value of x: the (positive) distance between x and zero
ceil(x) # The ceiling of x: the smallest integer not less than x
cmp(x,y) # -1 if x < y, 0 if x == y, or 1 if x > y
exp(x) # The exponental of x
fabs(x) # The absolute value of x
floor(x) # The floor of x: the largest integer not greater than x
log(x) # The natural logarithm of x, for x>0
log10(x) # The base 10 logarithm of x for x>0
max(x1,x2,x3) # The largest of arguments
min(x1,x2,x3) # The smallest of arguments
modf(x) # The fractional and integer parts of x in a two-item tuple. Both parts have the same sign as x. The integer part is returned as a float.
pow(x,y) # The value x**y
round(x,n) # x rounded to n digits from the decimal point
sqrt(x) # The square root of x for x > 0
