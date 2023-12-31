# -*- coding: utf-8 -*-
"""Iris flower classification

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/155M4xp8Yx-UXE66cX1wlL5GT-0GSB2Xo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

columns = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Class_labels']
df = pd.read_csv('/content/iris.data', names=columns)
df.head(6)

df.describe()

df.info()

sns.pairplot(df,hue='Class_labels')

data = df.values
X = data[:,0:4]
Y = data[:,4]

Y_Data = np.array([np.average(X[:, i][Y==j].astype('float32')) for i in range (X.shape[1])
for j in (np.unique(Y))])
Y_Data_reshaped = Y_Data.reshape(4, 3)
Y_Data_reshaped = np.swapaxes(Y_Data_reshaped, 0, 1)
X_axis = np.arange(len(columns)-1)
width = 0.25

plt.bar(X_axis, Y_Data_reshaped[0], width, label = 'Setosa')
plt.bar(X_axis+width, Y_Data_reshaped[1], width, label = 'Versicolour')
plt.bar(X_axis+width*2, Y_Data_reshaped[2], width, label = 'Virginica')
plt.xticks(X_axis, columns[:4])
plt.xlabel("Features")
plt.ylabel("Value in cm.")
plt.legend(bbox_to_anchor=(1.3,1))
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

svn = SVC()
svn.fit(X_train, y_train)

predictions = svn.predict(X_test)
accuracy_score(y_test, predictions)

print(classification_report(y_test, predictions))

X_new = np.array([[3, 2, 1, 0.2], [  4.9, 2.2, 3.8, 1.1 ], [  5.3, 2.5, 4.6, 1.9 ]])
prediction = svn.predict(X_new)
print("Prediction of Species: {}".format(prediction))