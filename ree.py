import matplotlib.pyplot as plt
import numpy as np
from random import uniform
alpha=input('Enter the mean')
beta=input('Enter the value for beta')
for n in range(1000):
    x=uniform(0,1);
    r=alpha*(-(np.log(x))**(1/beta);
    print r
plt.hist(r)    
