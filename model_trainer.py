# from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
import pandas as pd
import pickle
from niapy.problems import Problem
from niapy.task import Task
from niapy.algorithms.basic import ParticleSwarmOptimization
from sklearn.metrics import recall_score, roc_auc_score, f1_score, precision_score


class SVMFeatureSelection(Problem):
    def __init__(self, X_train, y_train, alpha=0.99):
        super().__init__(dimension=X_train.shape[1], lower=0, upper=1)
        self.X_train = X_train
        self.y_train = y_train
        self.alpha = alpha

    def _evaluate(self, x):
        selected = x > 0.5
        num_selected = selected.sum()
        if num_selected == 0:
            return 1.0
        accuracy = cross_val_score(SVC(), self.X_train[:, selected], self.y_train, cv=2, n_jobs=-1).mean()
        score = 1 - accuracy
        num_features = self.X_train.shape[1]
        return self.alpha * score + (1 - self.alpha) * (num_selected / num_features)

# load the dataset, run the algorithm and compare the results
data = pd.read_csv("diabetes.csv")
X = data.iloc[:, :8]
X = X.values

y = data["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=1234)

problem = SVMFeatureSelection(X_train, y_train)
task = Task(problem, max_iters=100)
algorithm = ParticleSwarmOptimization(population_size=1, seed=500)
best_features, best_fitness = algorithm.run(task)

selected_features = best_features > 0.5
print('Number of selected features:', selected_features.sum())

model_selected = SVC()
model_all = SVC()

model_selected.fit(X_train[:, selected_features], y_train)
print('The accuracy score:', model_selected.score(X_test[:, selected_features], y_test))

y_pred = model_selected.predict(X_train[:, selected_features])

model_selected.fit(X_train, y_train)

roc = roc_auc_score(y_train, y_pred)

print("The recall score = ", recall_score(y_train, y_pred, average='macro'))
print("The Precision = ",precision_score(y_train, y_pred, average='macro'))
print("The f1_score = ",f1_score(y_train, y_pred, average='macro'))
print("The ROC value = ",roc)

filename = 'diabetes_model.sav'
pickle.dump(model_selected, open(filename, 'wb'))
