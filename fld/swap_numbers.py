#swap two variables without third
A = 5
B = 7
print('A: ' + str(A))
print('B: ' + str(B))
print('============')
A = A + B
B = A - B
A = A - B
print('A: ' + str(A))
print('B: ' + str(B))
print('============')
A = A ^ B
B = A ^ B
A = A ^ B
print('A: ' + str(A))
print('B: ' + str(B))
print('============')