#calculation of a,b parameters for linear regression
input = [[1,2], [2,4], [3,6], [4, 8], [5, 10],  [6, 12], [7, 14], [8, 16], [9, 18]]

def LR(input):
    sumX = 0
    sumX2 = 0
    sumY = 0
    sumXY = 0
    output = {'a': 1, 'b': 0}
    n = len(input)
    for i in input:
        sumX += i[0]
        sumX2 += i[0]**2
        sumY += i[1]
        sumXY += i[0] * i[1]
    pow_sumX = sumX**2
    output['a'] = (n * sumXY - sumX * sumY) / (n * sumX2 - pow_sumX)
    output['b'] = (sumY - output['a'] * sumX) / n
    return output

out = LR(input)
print(out['a'])
print(out['b'])