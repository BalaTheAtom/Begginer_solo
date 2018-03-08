
import tensorflow
from scipy.spatial import distance
# import random
def euc(a,b):
    return distance.euclidean(a,b)

class scrappyKNN():
    def fit(self,X_train,y_train):
        self.X_train=X_train
        self.y_train=y_train

    def closest(self,row):
        best_distance=euc(row,X_train[0])
        best_index=0
        for i in range(1,len(self.X_train[0])):
            dist=euc(row,self.X_train[i])
            if(dist<best_distance):
                best_distance=dist
                best_index=i
            return self.y_train[best_index]

    def predict(self,X_test):
        predictions=[]
        for row in X_test:
            label=self.closest(row)
            predictions.append(label)
        return predictions


from sklearn import datasets
iris=datasets.load_iris()
X = iris.data
Y= iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train , y_test =train_test_split(X,Y,test_size=.8)

# from sklearn.neighbors import KNeighborsClassifier
my_classifier=scrappyKNN()
my_classifier.fit(X_train,y_train)
predict=my_classifier.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predict))