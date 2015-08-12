#Creating lists
list1 = ['python', 'golang','c++']
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

#Accessing elements
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

#Updating
list1[1] = "javascript"
print "Updated list1 ", list1

#Deleting
del list1[2]
print "Deleted list1 ", list1

#Length of list
print "Len: ", len(list1)

#Concatenation
print "Concatenated ", [1, 2, 3] + [4, 5, 6]

#Repetition
print "Repetition", ["Hi", "hello"] * 3

#Membership
print "Membership ", 3 in [1, 2, 3]

#Iteration
for x in list1: print "Lang: ", x

#List funcs
cmp(list1, list2) #compare
len(list3) #length
max(list2) #max element of list
min(list2) #min element of list
list(list1) #convert tuple to list

#List methods
list1.append("java") # append element to list
list1.count("java") # count how many times obj occurs in list
list1.extend(list2) # append seq to list
list1.index("index") # index of key
list1.insert(0, "c") # insert element to index
list1.pop(1) # remove last element and return it
list1.remove("c") # remove obj from list
list1.reverse() # reverse elements of list
list1.sort() # sort elements of list use func for sort if given
