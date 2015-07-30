# Comment

name=Abdullo

#variable
echo "My name is $name"

#executes expression
expr 1* 4

#use backquote for executing commands
echo "Today is `date`"

#for getting execution status of command use $? sign
ls
echo $?

#read user input
read fname

#more than one command on one line
echo "Hello $fname"; date
