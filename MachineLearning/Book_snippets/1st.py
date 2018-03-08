import os

import hashlib
import tarfile
from six.moves import urllib
import matplotlib.pyplot as plt
import pandas as pd
pd.options.display.max_rows
import numpy as np
DOWNLOAD_ROOT = "C:\\Users\\balaswamy\\Desktop\\ML\Data\\Housing\\"
HOUSING_PATH = DOWNLOAD_ROOT +  "housing.csv"
HOUSING_URL = DOWNLOAD_ROOT + "housing.tgz"
def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    housing_tgz = tarfile.open(housing_url)
    housing_tgz.extractall(path=DOWNLOAD_ROOT)
    housing_tgz.close()
def load_housing_data(housing_path=HOUSING_PATH):
    return pd.read_csv(housing_path)
housing=load_housing_data()
#print(housing.describe())
# housing.hist(bins=50, figsize=(20,15))
# plt.show()
def Splitdata(data,split_ratio):
    shuffled_indices=np.random.permutation(len(data))
    test_size=int(len(data)*split_ratio)
    test_indices=shuffled_indices[:test_size]
    train_indices=shuffled_indices[test_size:]
    return data.iloc[train_indices],data.iloc[test_indices]
#trainset,Test_set =Splitdata(housing,0.2)
#print(len(trainset) ,len(Test_set))

housing_id=housing.reset_index()
def test_set_check(identifier, test_ratio, hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio

def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]
# train_set, test_set = split_train_test_by_id(housing_id, 0.2, "index")


from sklearn.model_selection import train_test_split
train_set,test_set=train_test_split(housing,test_size=0.2,train_size=42)

# print(housing["median_income"].describe())
housing["income_cat"]=np.ceil(housing["median_income"]/1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)
# print(housing["income_cat"].value_counts())
# housing["income_cat"].hist(bins=50, figsize=(5,5))
# plt.show()
from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]
    # strat_train_set["income_cat"].hist(bins=50,figsize=(5,5))
    # strat_test_set["income_cat"].hist(bins=50, figsize=(5, 15))
    # plt.show()
# print(housing["income_cat"].value_counts()/len(housing))
for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)
housing=strat_train_set.copy()
# housing.plot(kind="scatter",x="longitude",y="latitude",alpha=0.1,
# s=housing["population"]/100, label="population", figsize=(10,7),
#              c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True, )
# plt.legend()
# plt.show()
# corr_matrix=housing.corr()
# print(corr_matrix["median_house_value"].sort_values(ascending=False))

from pandas.tools.plotting import scatter_matrix as sm

attributes = ["median_house_value", "median_income", "total_rooms","housing_median_age"]
# sm(housing[attributes], figsize=(12, 8))
# plt.show()
from sklearn.preprocessing import Imputer
imputer=Imputer(strategy="median")
housing_num = housing.drop("ocean_proximity", axis=1)
# print(housing_num)
imputer.fit(housing_num)
# print(imputer.statistics_)

X= imputer.transform(housing_num) #it will load the median values
housing_tr=pd.DataFrame(X,columns=housing_num.columns)
print(housing_tr.describe())



