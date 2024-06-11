from numpy import *

arr1=array([8,9,6,5])#1d array
arr=array([[1,2,3,4],[7,8,9,6]])#2d array
print(arr)
print(type(arr))
print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(sqrt(arr1))
print(min(arr1))
print(max(arr1))
print(unique(arr1))

import numpy as np

arr2 = np.array([])

n = int(input("Enter the size of arr2: "))
for i in range(n):
    x = int(input("Enter a value for arr2: "))
    arr2 = np.append(arr2, x)

print(arr2)

print(concatenate([arr1,arr2]))

arr3=arr1.view()
arr1[0]=5
print("arr1:",arr1)
print("arr3",arr3)
print(id(arr1))
print(id(arr3))

arr4=arr1.copy()
arr1[1]=8
print("arr1",arr1)
print("arr4",arr4)
print(id(arr4))
