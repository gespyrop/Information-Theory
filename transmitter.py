from lz78 import compress
from entropy import calculateEntropy

class Transmitter:
	def __init__(self):
		self.text = ''

	def readTextFromFile(self, filename):
		with open(filename, 'r') as file:
			self.text = file.read()

	#Main method for all the transmitter related procedure
	def send(self, receiver):
		
		#Original Text
		print('\nOriginal Size: {} bytes\nOriginal Text Entropy: {}'.format(len(self.text), calculateEntropy(self.text))) #Each character is 1 byte

		#Compressed Text
		compressed = compress(self.text)
		print('\nCompressed Size: {} bytes\nCompressed Text Entropy: {}'.format(len(compressed) / 4, calculateEntropy(compressed))) #Each 4 bits are 1 byte

		receiver.receive(compressed)
