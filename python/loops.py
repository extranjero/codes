## While loops
count = 0

while (count < 9):
	print "Current count is ", count
	count += 1
else: # python supports else statements after while 
	print "Loop finished ", count

## For loops
for letter in 'Python':
	print 'Current letter', letter

fruits = ['banana', 'apple', 'mango']

for index in range(len(fruits)):
	print 'Current fruit: ', fruits[index]
else:
	print 'Loop finished' 

for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print 'Current Letter :', letter
  
var = 10                    # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 5:
      break

print "Good bye!"

for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print 'Current Letter :', letter

for letter in 'Python': 
   if letter == 'h':
      pass
      print 'This is pass block'
   print 'Current Letter :', letter

print "Good bye!"
