import numpy as np
a=np.arange(2,11).reshape(3,3)
b=np.zeros(9)
b[2:]='5'
print(b)