#Dictionary
dict1 = {'Name': 'Zara', 'Age': 7}

print "dict['Name']: ", dict1['Name']
print "dict['Age']: ", dict1['Age']

#Updating

dict1['Age'] = 8; # update existing entry
dict1['School'] = "DPS School"; # Add new entry

print "After update", dict1

#Dictionary functions
cmp(dict1, dict2) #comparing
len(dict1) # length
str(dict1) # convert to string
type(dict1) # type of dict1

#Dictionary methods
dict1.clear() # Delete all elements of dictionary
dict1.copy() # returns shallow copy of dictionary
dict1.fromkeys() # create new dictionary with keys seq and values set to value
dict1.get("Gender", default="Woman") # return key, if not exist return default
dict1.has_key("key") # true if key exists and false if not exist
dict1.items() # returns list of dicts key value tuple pairs
dict1.keys() # return list of dictionary keys
dict1.setdefault("Gender", default="Man") # set key if not exist defualt
dict1.update(dict2) # add dict2 key value pairs to dict
dict1.values() # return list of values of dictionary

