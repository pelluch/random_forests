import math
import random
import Node

class DecisionTree:
	root = None
	features_per_split = 5
	num_bins = 10

	def __init__(self, data):
 	
		
		root = self.generate_node(data)
		# print(lowest_entropy)

	def generate_node(self, data):
		print(self.calculate_entropy(data))
		feature_list = list(data.columns.values)
		# print(feature_list)
		random.shuffle(feature_list)
		# print(feature_list[0:features_per_split])

		lowest_entropy = float("inf")
		chosen_attr = None


		for attr in feature_list[0:self.features_per_split]:
			attr_entropy = self.calculate_attr_entropy(data, attr)[0]
			if attr_entropy < lowest_entropy:
				lowest_entropy = attr_entropy
				chosen_attr = attr

		print(chosen_attr)
		node = Node.node(chosen_attr)


	def calculate_entropy(self, X):
		num_total = len(X)
		counts = dict()
		for index, row in X.iterrows():
			label = row['class_name']
			if label in counts:
				counts[label] += 1
			else:
				counts[label] = 1

		probs = [ float(class_count) / num_total for class_count in counts.values() ]
		entropy = 0
		for prob in probs:
			entropy -= prob * math.log(prob, 2)
		return entropy

	def calculate_attr_entropy(self, X, attr_name):
		num_total = len(X)
		min_value = X[attr_name].min()
		max_value = X[attr_name].max()
		step = (max_value - min_value)/self.num_bins
		current_split = step
		lowest_entropy = float("inf")
		best_split = current_split

		while current_split < max_value:
			current_split += step
			split_less = X[X[attr_name] <= current_split]
			split_greater = X[X[attr_name] > current_split]
			entropy_less = len(split_less)/num_total*self.calculate_entropy(split_less)
			entropy_greater = len(split_greater)/num_total*self.calculate_entropy(split_greater)
			new_entropy = entropy_less + entropy_greater
			if new_entropy < lowest_entropy:
				best_split = current_split
				lowest_entropy = new_entropy

		return lowest_entropy, best_split
	        