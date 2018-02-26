# To find the value of PI

import random
import math
sq_side=2
sq_area=(sq_side)**2
a=0
flag=0
while a < 100:
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    a=a+1
    print "The coordinate is (" ,x ,"," ,y, ")"
    y2=math.sqrt(1-(x*x));
    if (y2>y):
        flag=flag+1
        print "Flag=", flag
    else:
        continue
    
print flag
print sq_area
print a
pi_val=sq_area*float(flag/float(a))
print "The value of Pi is: ", pi_val

    
