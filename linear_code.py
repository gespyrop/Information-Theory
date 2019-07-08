from sage.all import *
from sage.coding.channel_constructions import random_error_vector
from random import randrange

class LC():
	def __init__(self):
		pass

	@staticmethod
	def getRandomNoise(length, noise_v):
		return sage.coding.channel_constructions.random_error_vector(length, GF(2), [randrange(length) for i in range(randrange(noise_v + 1))])