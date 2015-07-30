# command | commmand 
# with this sign you can pass result of one command to next command

ls | more

# filterng 
# write content of hotel.txt starting 30 line till last 20 lines
tail +20 < hotel.txt | head -n30 > hlist

#to run command background use & at the end of command
ls / -R | wc -l &
