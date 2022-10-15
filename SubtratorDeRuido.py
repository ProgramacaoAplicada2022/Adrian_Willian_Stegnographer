import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(a=32, version=2)
a=[]
for i in range(25):
    #a.append(int(random.randrange(-6,7,1)))
    #a.append(int(random.randint(-6,6)))
    a.append(int(random.gauss(0, 2)))
a=np.array(a)
print(a)

plt.hist(a,101,rwidth=0.9,weights=np.ones_like(a)/len(a))
plt.show()