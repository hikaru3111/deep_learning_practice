import sys, os
import numpy as np
import pickle
from PIL import Image
from dlfsm.dataset.mnist import load_mnist

#親ディレクトリをインポートするため
sys.path.append(os.pardir)

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

#get test data and label
def get_data():
    (x_train, t_train), (x_test,t_test) = load_mnist(flatten = True, normalize = True,one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("dlfsm/ch03/sample_weight.pkl", "rb") as f:
        network = pickle.load(f)
        return network

def predict(network,x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]


(x_train, t_train), (x_test,t_test) = load_mnist(flatten = True, normalize = False)

print(x_train.shape)
print(x_test.shape)
print(t_train.shape)
print(t_test.shape)

#extracting first img
print("extracting first img")
img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)

print("reshaping img")
img = img.reshape(28,28)
img_show(img)


