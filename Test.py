# To find the value of PI

import random
import math
sq_side=2
sq_area=(sq_side)**2
pi_val=0
for num in range(1,10):
    a=0
    flag=0
    while a < 100:
        x=random.uniform(0,1.0)
        y=random.uniform(0,1.0)
        x1=-1+2*x
        y1=-1+2*y
        a=a+1
        print "The coordinate is (" ,x1 ,"," ,y1, ")";
        y2=math.sqrt(1-(x*x));
        if (y2>y1):
            flag=flag+1
            print "Flag=", flag
        else:
            continue
    pi_val=pi_val+sq_area*float(flag/float(a))
    print pi_val

print flag
print sq_area
print a
pi_val_fin=pi_val/10 
print "The value of Pi is: ", pi_val_fin

    
