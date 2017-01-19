import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets as ds
from sklearn.cluster import KMeans
#print(iris)
#print(iris['DESCR'])
#print(iris['target_names']) #['setosa' 'versicolor' 'virginica']
#print(iris['feature_names']) #['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
#print(iris['target'])
iris = ds.load_iris()

sepal_l = iris['data'][:, 0]
sepal_w = iris['data'][:, 1]
petal_l = iris['data'][:, 2]
petal_w = iris['data'][:, 3]

all_set = np.c_[iris['data'], iris['target']]
all_0 = all_1 = all_2 = np.empty((0,5))
for i in all_set:
    if i[4] == 0:
        all_0 = np.append(all_0, np.array([i]), axis=0)
    if i[4] == 1:
        all_1 = np.append(all_1, np.array([i]), axis=0)
    if i[4] == 2:
        all_2 = np.append(all_2, np.array([i]), axis=0)
#plt.plot(all_0[:,0], all_0[:,1], 'ro', all_1[:,0], all_1[:,1], 'bo', all_2[:,0], all_2[:,1], 'go')
#plt.plot(all_0[:,2], all_0[:,3], 'ro', all_1[:,2], all_1[:,3], 'bo', all_2[:,2], all_2[:,3], 'go')
#plt.show()


#plt.scatter(iris['data'][:,2], iris['data'][:,3], c=all_set[:,4])
#plt.show()



km1 = KMeans(n_clusters = 3).fit_predict(iris['data'])
km2 = KMeans(n_clusters = 3).fit_predict(iris['data'][:,2:4])
all_set_km1 = np.c_[all_set, km1]
all_set_km2 = np.c_[all_set, km2]
a = np.c_[all_set_km1, all_set_km1[:,4]+10 + all_set_km1[:,5]]
plt.scatter(a[:,2], a[:,3], c=a[:,6])
plt.show()
