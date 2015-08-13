'''
Functions 
def functionname (parametres):
    function_suite
    return [expression]
'''

def printme(str):
    "This prints a passed string into this function"
    print str

printme("Hello world")

# Function definition is here
# All arguments in python are passed by reference
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist

#Keyword argumnets

def printperson (name, age = 18):
    print "Name: %s, Age: %d" % (name, age)

# Calling by keyword
printperson(name="Abdullo", age=21)

#Deault arguments
printperson("Iskander")
printperson(name = "Iskander")

#Variable length arguments
def printall(arg1, *others):
    print "Firts %s, others %s" % (arg1, others)

printall("FIrst", 2, 3, 4)

#Lambda functions
sum = lambda arg1, arg2: arg1 + arg2

print "Sum of 10 + 20 = %d" % sum(10,20)

#Return 

def divide(a, b):
    return a / b

print "Divide 20 / 10 = %d" % divide(20, 10)
