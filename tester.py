

import numpy as np

z = np.zeros((2,2), dtype='U2')
o = np.ones((2,1), dtype='O')
pr = np.hstack([o, z])

print(str(pr))

