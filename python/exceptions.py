try:
    fh = open("testfile", "r")
except IOError:
    print "Error: cant find file or read data"
else:
    print "Written content in the file succesfully"
    fh.close()


#Exception with no Exceptions
try: 
    fl = open("anotherfile", "r")
    try:
        fl.write("data to file")
    # finally block executes at the end of try except blocks
    finally: 
        fl.close()
except:
    print "Error"

#Custom errors and raising error
class LevelError(RuntimeError):
    def __init__(self, arg):
        self.args = arg
#Function with raise error
def someFunc(level):
    if level < 1:
        raise LevelError("Bad level")

try: 
    someFunc(-1)
except LevelError, e:
    print "Level error", e
else:
    print "Everything is fine"
