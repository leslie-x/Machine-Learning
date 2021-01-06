import numpy as np
import matplotlib.pyplot as plt

#read test data
train = np.loadtxt('/home/pi/Documents/Machine Learning/click.csv',delimiter=',',skiprows=1)
train_x=train[:,0]
train_y=train[:,1]

theta0=np.random.rand()
theta1=np.random.rand()

def f(x):
    return theta0+theta1*x

def E(x,y):
    return 0.5*np.sum((y-f(x))**2)

mu=train_x.mean()
sigma=train_x.std()

#standardize
def standardize(x):
    return (x-mu)/sigma

train_z = standardize(train_x)

ETA=1e-3
diff=1
#count=0
error=E(train_z,train_y)

while diff>1e-2:
    #data update
    tmp0=theta0-ETA*np.sum((f(train_z)-train_y))
    tmp1=theta1-ETA*np.sum((f(train_z)-train_y)*train_z)
    theta0=tmp0
    theta1=tmp1
    #caculate error
    current_error=E(train_z,train_y)
    diff=error-current_error
    error=current_error
    #log
    #count +=1
    #log='{}time:theta0={:.3f},theta1={:.3f},diff={:.4f}'
    #print(log.format(count,theta0,theta1,diff))

#plot
x=np.linspace(-3,3,100)
plt.plot(train_z,train_y,'o')
plt.plot(x,f(x))
plt.show()