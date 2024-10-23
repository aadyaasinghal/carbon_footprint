import numpy as np
x = np.array([[2,5,6],
     [6,7,8],
     [8,9,10]])
y = np.array([[1,2,3],
              [6,6,8]
              ])
def slice (x,y):
    z =x[0,:]
    a = y[0,:]
    return (z*a)
z = slice(y,x)

def avg (x):
    y=x[:,0]
    z=np.mean(y)
    print (z)
avg(x)
def sum (x):
    y=x[:,2]
    z = np.sum(y)
    print (z)
sum(x)
def slice (x):
    y = x[0,0:2]
    z = y[0]/y[1]
    print (z)
slice(x)