from sage.all import *
from sage.coding.channel_constructions import random_error_vector
from random import randrange

class LC():
	def __init__(self, P, maxNoise):
		P = Matrix(P)
		G = Matrix(GF(2), identity_matrix(P.nrows()).augment(P))
		self.C = LinearCode(G)
		self.maxNoise = maxNoise

	#Encoding given binary
	def encode(self, original):

		#Padding
		while len(original) % self.C.dimension() != 0:
			original += '0'

		words = self.getWords(original, self.C.dimension())

		encoded = ''

		for word in words:
			encoded += self.encodeWord(word, self.maxNoise)

		print("{} bits added!".format(len(encoded) - len(original)))

		return encoded

	#Encoding given binary
	def decode(self, encoded):
		words = self.getWords(encoded, self.C.length())

		decoded = ''

		for word in words:
			decoded  += self.decodeWord(word)

		return decoded


	#Encodes a binary string with length equal to the code's dimension
	def encodeWord(self, word, maxNoise):
		encoded = self.C.encode(vector([int(bit) for bit in list(word)]))
		encoded += LC.getRandomNoise(len(encoded), maxNoise) #Applying noise to word
		return ''.join(str(bit) for bit in encoded)

	#Decodes a binary string with length equal to the code's length
	def decodeWord(self, word):
		decoded = self.C.decode_to_message(vector([int(bit) for bit in list(word)]))
		return ''.join(str(bit) for bit in decoded)

	#Breaks a binary into words of given length
	def getWords(self, binary, length):
		words = []

		for i in range(len(binary) / length):
			word = binary[length * i : length * (i + 1)]
			words.append(word)

		return words


	@staticmethod
	def getRandomNoise(length, noise_v):
		return sage.coding.channel_constructions.random_error_vector(length, GF(2), [randrange(length) for i in range(randrange(noise_v + 1))])

	@staticmethod
	def getErrorCorrectingCapability(P):
		P = Matrix(P)
		L = LinearCode(Matrix(GF(2), identity_matrix(P.nrows()).augment(P)))
		print  "\n", L
		d = L.minimum_distance()
		return (d - 1) / 2
		
		