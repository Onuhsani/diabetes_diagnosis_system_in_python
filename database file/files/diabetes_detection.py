import numpy as np
import pandas as pd
# import pandas_profiling
import pickle
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, f1_score, precision_score, classification_report

data = pd.read_csv("diabetes.csv")
# profile = data.profile_report(title='Diabetes Profiling Report')
# profile
X = data.iloc[:, :8]
# X.head()

y = data["Outcome"]
# y.head()

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=0)

# print(X_train.shape)
#
# print(y_train.shape)
#
# print(X_test.shape)
#
# print(y_test.shape)

# X_train.head()

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)

# X_train[:5, :]


# SVM Kernels
# for k in ('linear', 'poly', 'sigmoid', 'rbf'):
#     model = svm.SVC(kernel=k)
#     model.fit(X_train, y_train)
#     y_pred = model.predict(X_train)
#     print(k)
#     print(accuracy_score(y_train, y_pred))


model = svm.SVC(kernel='rbf')
model.fit(X_train, y_train)
y_pred = model.predict(X_train)

roc = roc_auc_score(y_train, y_pred)
print("The Accuracy score = ", accuracy_score(y_train, y_pred))
# print(classification_report(y_train, y_pred))
print("The recall score = ", recall_score(y_train, y_pred, average='macro'))
print("The Precision = ",precision_score(y_train, y_pred, average='macro'))
print("The f1_score = ",f1_score(y_train, y_pred, average='macro'))
print("The ROC value = ",roc)


# Making a Single Prediction
# 'pregnancies', 'glucose', 'bpressure', 'skinThickness'
# 'insulin', 'bml', 'pedigree', 'age'

filename = 'diabetes_model.sav'
pickle.dump(model, open(filename, 'wb'))

patient = np.array([[1., 150., 70., 45., 0., 40., 1.5, 25]])

# Normalize the data with the values used in the training set
# patient = scaler.transform(patient)
# model.predict(patient)
#
# patient = np.array([[1., 50., 70., 45., 0., 40., 1.5, 25]])

# Normalize the data
# patient = scaler.transform(patient)