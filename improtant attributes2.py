# 1.shape 2.nDim 3.size 4.itemsize 5.Dtype 6.astype()
import numpy as np
arr1=np.array([1,2,3,4,5])
arr1

arr2=np.array([[1,2,3],[6,7,8]])
arr2

arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,20,30]]])
arr3

print(arr3.shape) # tell us number of rows, colums, and dimention.
print(arr3.ndim) # only dimention
print(arr1.ndim)

print(arr1.size)  #total number of elements
print(arr1.itemsize) # show bytes in memory

print(arr3.dtype) #

# we can convert the type of data in numpy. for example
arr4=arr3.astype('float') # use function astype from int to float.
print(arr4)

# we use this in ml and other area to convert float data into int data. that int take less space in memory and when run in algorithum it take less time whrn memory is less.

