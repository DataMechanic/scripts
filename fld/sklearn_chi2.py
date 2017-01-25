
## ALGORITHM
## sklearn.feature_selection chi2
## http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2
## http://stattrek.com/chi-square-test/independence.aspx?Tutorial=AP
## http://stackoverflow.com/questions/21281328/scikit-learn-%CF%87%C2%B2-chi-squared-statistic-and-corresponding-contingency-table
## https://habrahabr.ru/post/264915/

import numpy as np
from scipy.stats import chisquare
from sklearn.preprocessing import normalize
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2
#X - features
input_data = np.array([['male', 'yes'],
                       ['male', 'yes'],
                       ['male', 'yes'],
                       ['male', 'yes'],
                       ['male', 'yes'],
                       ['male', 'no'],
                       ['female', 'yes'],
                       ['female', 'no'],
                       ['female', 'no']])
#preprocessing: string -> int
x = input_data[:, :1].reshape(1,-1)[0]
y = input_data[:, 1:].reshape(1,-1)[0]
le_x = LabelEncoder()
le_y = LabelEncoder()
le_x.fit(x)
le_y.fit(y)
X = le_x.transform(x).reshape(-1,1)
Yt = le_y.transform(y)

Y = np.vstack([1 - Yt, Yt]) #Stack arrays in sequence vertically
observed = np.dot(Y,X) # get observed data
feature_count = X.sum(axis=0)
class_prob = Y.mean(axis=1)
expected = np.dot(feature_count.reshape(-1,1), class_prob.reshape(1,-1)).T
score, pval = chisquare(observed, expected)
print('Chi2 calculated: ', score, pval)

chi_square = chi2(X, Yt)
print('Chi2 from sklearn package: ', chi_square)
