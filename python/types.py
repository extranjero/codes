a = b = c = 1

a, b, c = 1, 2, "john"

#Numbers

var1 = 1
var2 = 2

del var1, var2

mystr = 'Hello world'

print mystr           # Prints complete string
print mystr[0]        # Prints first character of string 
print mystr[2:5]      # Prints characters starting from 3rd to 5th 
print mystr[2:]       # Prints characters starting from 3rd to last
print mystr * 2       # Prints string two times
print mystr + "test"  # Prints concatenated string

#Lists

mylist = ["string", 786, 'john', 70.2]
tinylist = [123, 70.2]

print mylist         # Prints complete list
print mylist[0]      # Prints first elemnt of the list
print mylist[1:3]    # Prints elements starting 2nd till 3rd
print mylist[3:]     # Prints elements starting 3d till end
print tinylist * 2   # Prints list two times
print mylist + tinylist # Prints concatenated lists

#Tuples 

mytuple = ("string", 786, 'john', 70.2)
tinytuple = (123, 70.2)

print mytuple         # Prints complete tuple
print mytuple[0]      # Prints first elemnt of the list
print mytuple[1:3]    # Prints elements starting 2nd till 3rd
print mytuple[3:]     # Prints elements starting 3d till end
print tinylist * 2    # Prints list two times
print mytuple + tinytuple # Prints concatenated lists

#Dictionaries

mydict = {}
mydict['one'] = "This is one"
mydict[2] = "This is two"

tinydict = {"name": "john", "age": 20}

print mydict['one']      # Prints value of one key
print mysidct[2]         # Prints valie of 2 key
print tinydict           # Prints conplete dictionary
print tinydict.keys()    # Prints all keys
print tinydict.values()  # Prints all values

#Data type conversation

int(x[,base]) # int
long(x[,base]) # long int
float(x) # float
complex(real[,imag]) # complex number
str(x) # string
repr(x) # expression string
eval(x) # evaluate string return object
tuple(s) # tuple
list(s) # list
set(s) # set
dict(d) # dictionary
frozenset(s) # frozen set
chr(x) # int to string
unichr(x) # int to unicode
ord(x) # string to int
hex(x) # int to hex
oct(x) # int to octal

