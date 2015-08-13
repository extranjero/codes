import time
import calendar

tm = time.time() # get time in timestamp
lt = time.localtime(tm)  # getting localtime
fm = time.asctime(lt)  # getting formatted time

print "Time ",  fm



