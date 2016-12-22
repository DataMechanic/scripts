

import numpy as np
import statistics as stc
arr = [1,2,3,4,2,3,4,5,4,2,4,5,6,7,8,2,4]
print('variance: ' + str(stc.variance(arr)))
####
s = 0
for i in arr:
    s += i
avg = s/len(arr)

v = 0
for j in arr:
    v += (j - avg)**2
vrc = v / (len(arr) - 1)
print('variance: ' + str(vrc))
