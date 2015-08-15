#Crating classes

class Employee:
    'Employee doc'
    #static variable
    quantity = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.quantity += 1

    def count(self):
        print "Total employee %d" % Employee.quantity

    def show(self):
        print "Name %s salary %d" % (self.name, self.salary)

emp1 = Employee("Abdullo", 400)
emp2 = Employee("Iskander", 500)

emp1.count()
emp1.show()
emp2.show()

emp1.age = 20
emp1.age = 21

print "Age: ", emp1.age

del emp1.age

#Obj manipulating methods
print "age: ", getattr(emp1, "age", "Not found")
print "name: ", getattr(emp1, "name", "Not found")
print "salary: ", hasattr(emp1, "salary")

setattr(emp1, "age", 21)
print "age: ", getattr(emp1, "age", "Not found")

# Bultin methods
print "__dict__", emp1.__dict__
print "__doc__", emp1.__doc__
print "__module__", emp1.__module__


## Inheritance

class Human: 
    __private = "" #protected properties
    def __init__(self,name):
        self.__private = "this is prvate key"
        self.name = name
    def say(self):
        print "My name is %s && private %s" % (self.name, self.__private)

class Person(Human):
    #method overriding
    def say(self):
        print "Yo dude, ma name is %s" % self.name 
    def greet(self):
        print "Hello how are u ?"


person = Person("Abdullo")

person.say()
person.greet()

print "Person is subclasss of Human ? : ", issubclass(Person, Human)
print "person is instance of Person ? : ", isinstance(person, Person)


class Overrride:
    # method will be called in initialization of instane of class (object creation)
    # Ex: obj = Override("some")
    def __init__(self, some):
        self.some = some

    # when destructor is called
    # Ex : del obj
    def __del__(self):
        del self.some
    # Ex: call repr(obj)
    def __repr__(self):
        return "Obj: " + self.some
    # Ex str(obj)
    def __str__(self):
        return "Some : " + self.some
    # Ex: cmp(obj,x)
    def __cmp__(self, x):
        return self == x


