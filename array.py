import numpy as np
A = np.array([1,2,3,4])
print(A)
print(np.ndim(A))
print(A.shape)
print(A.shape[0])

B = np.array([[1,2],[3,4]])
C = np.array([[5,6],[7,8]])
D = np.array([[1,2,3],[4,5,6]])
E = np.array([[1,2],[3,4],[5,6]])

X = np.array([3,2])
W = np.array([[1,3,5],[2,4,6]])

#ドット積
print("dot(B,C)")
print(np.dot(B,C))
print("dot(D,E)")
print(D.shape)
print(E.shape)
print(np.dot(D,E))
print("X * W")
print(np.dot(X,W))