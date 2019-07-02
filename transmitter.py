from lz78 import compress
from sys import getsizeof

class Transmitter:
	def __init__(self):
		self.text = ''

	def readTextFromFile(self, filename):
		with open(filename, 'r') as file:
			self.text = file.read()

	#Main method for all the transmitter related procedure
	def send(self, receiver):
		print('\nOriginal size:',getsizeof(self.text))
		compressed = compress(self.text)
		print('Compressed size:',getsizeof(compressed))
		print("\nCompressed message: {}".format(compressed))
		receiver.receive(compressed)
