import time
x=range(10000000)
y=range(10000000,20000000)

start_time=time.time()
c=[(x,y) for x,y in zip(x,y)]
print(time.time()-start_time)

'''import numpy as np
import time
a=np.arange(10000000)
b=np.arange(10000000,20000000)
start_time=time.time()
c=a+b
print(time.time()-start_time)'''