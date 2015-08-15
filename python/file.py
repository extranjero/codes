#Reading files u can using open() func

#file object = open(file_name [, access mode][,buffering])
# file_name: path to file
# access_code: in wich mode file shld be opened 
# buffering: 0 for no buffering

## Modes
#r	Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
#rb	Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
#r+	Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
#rb+	Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.
#w	Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
#wb	Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
#w+	Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
#wb+	Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
#a	Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
#ab	Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
#a+	Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
#ab+	Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

fo = open("base.py", "a+")
print "Name of the file: ", fo.name
print "Closed or not: ", fo.closed
print "Opening mode: ", fo.mode
print "Softspace flag: ", fo.softspace

fo.write("print 'Hello world!'")

print "File position: ", fo.tell()

st = fo.read(100)

print "File content: ", st

fo.close()
