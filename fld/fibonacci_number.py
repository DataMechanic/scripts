
'''
    Fibonacci number
'''

import time
import numpy as np

n = 34

def method1(n):
    # it isn't effective
    if n <= 0: return 0
    if n == 1: return 1
    return method1(n-1) + method1(n-2)

def method2(n):
    # best method!
    x = [0,1]
    i = 2
    while i <= n:
        x.append(x[i-1] + x[i-2])
        i += 1
    return x[-1]

def method3(n):
    # for n <= 45
    x = np.array([[0, 1], [1, 1]])
    f_0_1 = np.array([[0],[1]])
    f_n = np.linalg.matrix_power(x,n-1).dot(f_0_1)
    return f_n[1,0]

start_time = time.time()
result = method1(n)
end_time = time.time()
exec_time = end_time - start_time
print('result fib1: ' + str(result) + '; time: ' + str(exec_time))

start_time = time.time()
result = method2(n)
end_time = time.time()
exec_time = end_time - start_time
print('result fib2: ' + str(result) + '; time: ' + str(exec_time))

start_time = time.time()
result = method3(n)
end_time = time.time()
exec_time = end_time - start_time
print('result fib3: ' + str(result) + '; time: ' + str(exec_time))
