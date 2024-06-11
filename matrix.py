import numpy as np
arr1=np.array([[1,3,4],[4,5,6]])

arr2=arr1.flatten()
print("arr2",arr2)
print(arr2.ndim)
print(arr2.dtype)
print(arr2.shape)
print(arr1.size)

arr3=arr2.reshape(3,2)
print(arr3)
print(arr3.ndim)
print(arr3.shape)
arr4=arr2.reshape(3,2,1)
print(arr4)
print(arr4.ndim)
print(arr4.shape)
m=np.matrix(arr1)
m1=np.matrix(arr4)
m2=m1*m
print(m2)
