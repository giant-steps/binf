

import numpy as np

a = (0,1,2,3,4,5,6,7,8)
b = (2,2,2,2,3,3,3,3,3)

aa = np.array(a)
bb = np.array(b)

c = np.concatenate([a,b],axis=0)
d = np.array_split(c,10,axis=1)

print(str(d))

