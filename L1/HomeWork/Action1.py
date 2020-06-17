# Action1：求2+4+6+8+...+100的求和，用Python该如何写
import numpy as np
x1 = np.arange(2,102,2)
print('x1 = ', x1)
sum = np.sum(x1)
print('sum =', sum)
