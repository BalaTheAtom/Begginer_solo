import matplotlib.pyplot as plt
import pydotplus
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
iris=load_iris()
x=iris.data[:,2:]
y=iris.target

tree_clf=DecisionTreeClassifier(max_depth=3)
a=tree_clf.fit(x,y)
print(iris)
plt.scatter(iris.data[:,2:3],iris.data[:,3:])
plt.legend(iris.feature_names[2:],iris.feature_names[3:]        )
plt.show()

from sklearn.tree import export_graphviz
dot_data=export_graphviz(
        tree_clf,
        out_file=None,
        feature_names=iris.feature_names[2:],
        class_names=iris.target_names,
        rounded=True,
        filled=True
    )
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png('tree.png')
