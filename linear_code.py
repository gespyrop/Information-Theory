from sage.all import *
from sage.coding.channel_constructions import random_error_vector
from random import randrange

class LC():
	def __init__(self, P):
		P = Matrix(P)
		G = Matrix(GF(2), identity_matrix(P.nrows()).augment(P))
		self.C = LinearCode(G)

	#Encodes a binary string with length equal to the code's dimension
	def encodeWord(self, word):
		encoded = self.C.encode(vector([int(bit) for bit in list(word)]))
		return ''.join(str(bit) for bit in encoded)

	#Decodes a binary string with length equal to the code's length
	def decodeWord(self, word):
		decoded = self.C.decode_to_message(vector([int(bit) for bit in list(word)]))
		return ''.join(str(bit) for bit in decoded)

	@staticmethod
	def getRandomNoise(length, noise_v):
		return sage.coding.channel_constructions.random_error_vector(length, GF(2), [randrange(length) for i in range(randrange(noise_v + 1))])