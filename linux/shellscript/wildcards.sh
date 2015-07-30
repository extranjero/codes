#Wildcards

# * any string or group of characters

ls * # all files
ls a* # all files starting with a
ls a.* # all files with extension .c
ls ut*.c # all files starting with ut and with extension .c

# ? any single character

ls ? # all files witch name length is one character
ls fo? # all files starting with fo and one more chareacter

# [...] any of encolosed characters

ls [abc]* # all files wich names starting with a,b or c
ls [a-c]* # all files wich names starting with a to c
ls [!a-o]* # all files wich names not starting with a to c
ls [^a-o]* # all files wich names not starting with a to c




