import numpy as np

# AND gate
def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5, -0.5])
    b = -0.7
    tmp = x*w + b
    if tmp <= 0:
        return 0
    else:
        return 1

#NAND gate
def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

#OR gate
def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

#XOR gate
def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

print("AND gate")
print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))