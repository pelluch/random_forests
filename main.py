from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing

import pandas as pd
import numpy as np

import DecisionTree

# Leemos los datos
data = pd.read_csv('OGLE.csv')
# labels = data.ix[:, 'class_name':'class_name']
# data = data.drop('class_name', 1)
unique_labels = data['class_name'].drop_duplicates()

# Normalizamos las columnas
# min_max_scaler = preprocessing.MinMaxScaler()
# x_scaled = min_max_scaler.fit_transform(data)
# data = pd.DataFrame(x_scaled)

num_trees = 10


min_instances_split = 10
max_samples = 0.5
# data.as_matrix()
del data['ogle_id']

def fit(X, y):
	print('fit')

def predict(x):
	print('predict')

def generate_bag(x):
	print('generate bag')

def calculate_entropy():
	print('Entropy')

def make_tree():
	print('tree')


		

# def calculate_entropy(X
tree = DecisionTree.DecisionTree(data)