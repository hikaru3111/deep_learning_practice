#活性化関数
import numpy as np
import matplotlib.pylab as plt

def step_function(x)):
    if x > 0:
        return 1
    else:
        return 0

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def relu(x):
    return np.maximum(x,0)

#test
st_x = np.arrange(-5.0,5.0,0.1)
st_y = step_function(st_x)
plt.plot(st_x,st_y)
plt.ylim(-0.1, 1.1)
plt.show()

sg_x = np.arrange(-5.0,5.0,0.1)
sg_y = sigmoid(sg_x)
plt.plot(sg_x,sg_y)
plt.ylim(-0.1, 1.1)
plt.show()

re_x = np.arrange(-0.5,0.5,0.1)
re_y = relu(x)
plt.plot(re_x,re_y)
plt.ylim(-0.1,1,1)
plt.show()