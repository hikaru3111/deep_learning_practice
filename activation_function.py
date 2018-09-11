#活性化関数
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x >0, dtype=np.int)

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def relu(x):
    return np.maximum(x,0)

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) #for prevending overflow
    exp_sum_a = np.sum(exp_a)
    y = exp_a / exp_sum_a
    return y
#test
#st_x = np.arange(-5.0,5.0,0.1)
#st_y = step_function(st_x)
#plt.plot(st_x,st_y)
#plt.ylim(-0.1, 1.1)
#plt.show()
#
#sg_x = np.arange(-5.0,5.0,0.1)
#sg_y = sigmoid(sg_x)
#plt.plot(sg_x,sg_y)
#plt.ylim(-0.1, 1.1)
#plt.show()
#
#re_x = np.arange(-0.5,0.5,0.1)
#re_y = relu(re_x)
#plt.plot(re_x,re_y)
#plt.ylim(-0.1,0.5)
#plt.show()