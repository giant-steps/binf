

import numpy as np

a = (0,1,2,3,4,5,6,7,8)
b = (2,2,2,2,3,3,3,3,3)

aa = np.array(a)
bb = np.array(b)


c = np.vstack((aa,bb))

print(str(c))

d = c[0][7]

print(d)