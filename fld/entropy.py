

import numpy as np
import math

import csv
from sklearn import datasets as ds



'''
iris = ds.load_iris()
arr = []
for i in iris['target']:
    if i == 0: arr.append('Iris-Setosa')
    elif i == 1: arr.append('Iris-Versicolour')
    else: arr.append('Iris-Virginica')
target_nm = np.array(arr)
all_set = np.c_[iris['data'], target_nm]
'''

data_set = []
with open('d:\\scripts\\color_size_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for r in reader:
        data_set.append(r)
all_set = np.array(data_set)

def entropy(inp, cn):
    dim = inp.shape
    # if inp.ndim != 2: return 1 # ndim - number of dimensions/axis
    if len(dim) != 2: return -1
    if cn > dim[1]: return -1
    cln = {}
    for i in inp:
        try:
            cln[i[cn]] += 1
        except:
            cln[i[cn]] = 1
    totalAmount = 0
    for i in cln:
        totalAmount += cln[i]
    prb = 0
    ent = 0
    for i in cln:
        prb = cln[i] / totalAmount
        ent += prb * math.log(prb, 2)
    ent = ent * (-1)
    return ent

def info_gain(input, targetColNum):
    dim = input.shape
    initialEntropy = entropy(input, targetColNum)
    totalRows = 0
    for i in input:
        totalRows += 1
    i = 1
    for i in range(0,dim[1]):
        if i != targetColNum:
            colStat = {}
            for j in input:
                try:
                    colStat[j[i]] += 1
                except:
                    colStat[j[i]] = 1
            conditionalEntropy = 0
            for l in colStat:
                filteredSet = input[(input[:,i] == l)]
                jointEntropy = entropy(filteredSet, targetColNum)
                conditionalEntropy += (colStat[l] / totalRows) * jointEntropy
        else: conditionalEntropy = -1
        print(conditionalEntropy)
    return initialEntropy


#all_set_new = all_set[(all_set[:,3] == 'Irregular')]
a = info_gain(all_set, 4)
#print (a)



