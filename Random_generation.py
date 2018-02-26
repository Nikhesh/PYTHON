import numpy as np
import math
import random
x = 0
lis=[]
while x < 100:
    ra = random.uniform(-1.0,1.0)
    r=2*(-1*np.log(ra))**(2)
    lis.append(r)
    x+=1
print r
