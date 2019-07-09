from lz78 import compress
from entropy import calculateEntropy
from linear_code import LC
from base64 import b64encode
from json import dumps

class Transmitter:
	def __init__(self):
		self.text = ''

	def readTextFromFile(self, filename):
		with open(filename, 'r') as file:
			self.text = file.read()

	#Main method for all the transmitter related procedure
	def send(self, receiver, P, maxNoise):
		
		#Original Text
		print('\nOriginal Size: {} bytes\nOriginal Text Entropy: {}'.format(len(self.text), calculateEntropy(self.text))) #Each character is 1 byte

		print("\nCompressing with LZ78...")
		#Compressed Text
		compressed = compress(self.text)
		print('\nCompressed Size: {} bytes\nCompressed Text Entropy: {}'.format(len(compressed) / 8, calculateEntropy(compressed))) #Each 8 bits are 1 byte

		#Encoding with linear code
		print("\nEncoding with Linear Code...\n")
		L = LC(P, maxNoise)
		encoded = L.encode(compressed)

		print("\nEncoding with base64...\n")
		base64encoded = b64encode(encoded)

		json = dumps({"compression_algorithm":"LZ78", "code":{"name":"linear", "P":P}, "base64encoded":base64encoded})

		print("Sending JSON...\n")
		receiver.receive(json)
