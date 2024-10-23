import numpy as np
import matplotlib.pyplot as plt

y = np.array([1,1,2,3,1,1,2,3,3,1,1])
x = np.arange(0,len(y))
print (x)
fit = np.polyfit(x,y,2)
p = np.poly1d(fit)
print(p)
plt.plot(x,y,".")
plt.plot(x,p(x))
x2 = np.arange(0,15)
plt.plot(x2,p(x2),".")
plt.show()