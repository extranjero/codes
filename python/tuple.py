#Creating tuples
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";

#Accessessing values of tuples
print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]

#Tuple is a immutable list
# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print tup3
