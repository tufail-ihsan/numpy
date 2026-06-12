import numpy as np
arr1=np.array([1,2,3,4,5])  # ndarray
arr1
print(arr1)
print(type(arr1))  #type this is not list this is nd array


# 2-D array
arr2=np.array([[1,2,3,4],[5,6,7,8]])
print(arr2)
# 1
arr3=np.zeros((2,3))
print(arr3)

# 2
arr4=np.ones((2,3))
print(arr4)

# 3
arr5=np.identity((5))
print(arr5)

#4
arr6=np.linspace(1,2,3)
print(arr6)

#5
arr7=arr1.copy()
print(arr7)
