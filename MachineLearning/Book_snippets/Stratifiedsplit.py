import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit as strat
X = np.array([[4, 2], [3, 4], [4, 2], [3, 4]])
y = np.array([100, 100, 1, 1])
ss=strat(n_splits=1,test_size=0.5,random_state=0)
print(ss.get_n_splits(X, y))
for train_index,test_index in ss.split(X,y):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train_set,X_test_set=X[train_index],X[test_index]
    print(X_test_set,X_train_set)

