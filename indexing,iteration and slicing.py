import numpy as np
arr1=np.arange(24).reshape(6,4)
print(arr1)

arr2=np.array([1,2,3,4,5])
print(arr2)

print(arr2[1:4])                
print(arr2[-1])

print(arr1[ : ,2])  
print(arr1[3:5,1:3])        #  arr_name[starting row  : 1 before ended row , starting colum: 1 before ended colum]  endpoint will be not included  






# iteration: 



for i in arr1:
    print(i)  # this method print every singlwe row one by one of array not element by element.


for i in np.nditer(arr1):
    print(i)   # this method iterate on each element of array and print it. not go for row 



