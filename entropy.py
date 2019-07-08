from math import log

def calculateEntropy(text):
	symbols = set(text) #using a set to get each symbol once
	probabilities = [float(text.count(symbol)) / len(text) for symbol in symbols] #calculating probability of each symbol

	return -sum([(p * log(p,2)) for p in probabilities])	#calculating text's Shannon Entropy