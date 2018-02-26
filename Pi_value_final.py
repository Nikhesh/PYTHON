# To find the value of PI

import random
import math
sq_side=2
sq_area=(sq_side)**2
pi_val=0
for num in range(1,1001):
    a=0
    flag=0
    pi_i=0
    while a < 1000:
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        x1=-1+2*x
        y1=-1+2*y
        a=a+1
        y2=math.sqrt(1-(x*x));
        if (y2>y1):
            flag=flag+1
        else:
            continue
    pi_i=sq_area*float(flag/float(a))
    print "The value of pi in", num, "th iteration is ", pi_i 
    pi_val=pi_val+pi_i
    
pi_val_fin=pi_val/num
print "The value of Pi after ", num, "iterations is: ", pi_val_fin

    
