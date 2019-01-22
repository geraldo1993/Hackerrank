#!/bin/python

import sys




time = raw_input().strip()
(h, m, rest) = time.split(':')

m = int(m)
h = int(h)

if rest.find('PM') != -1:
    timeFormat = "PM"
    if h >= 1 and h <= 11:
        h += 12
else:
    timeFormat = "AM"
    if h == 12:
        h = 0
        
rest = rest.replace(timeFormat, '')
h = '{:02}'.format(h)
m = '{:02}'.format(m)

time_convesion = str(h) + ":" + str(m) + ":" + rest
print(time_convesion)






# Had to come back again for this question for my Advanced algorithm class and came up with another solution.

# to make my job easier I just imported the datetime function that is already build in python
from datetime import datetime

 # here I am creating a function to implement the convertions.
def convertTime(military_time): #converTime is the function name and military name is the paramenter (or the input of that function)

    # Here we are convertion the regular time to a military time or 24 h format. I used strtime which is The strftime() function formats the broken-down time tm according to the format specification format and places the result in the character array s of size max.  The broken-down time structure tm is defined in <time.h>. 
    return datetime.strptime(military_time, '%I:%M:%S%p').strftime('%H:%M:%S')
 
 
if __name__ == '__main__':
    military_time = raw_input() # here i am asking the user to give a time which it will be grabbed as in input to my function.

    # and last we are just printing the function we just created.
    print convertTime(military_time)
