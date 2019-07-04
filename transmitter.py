from lz78 import compress

class Transmitter:
	def __init__(self):
		self.text = ''

	def readTextFromFile(self, filename):
		with open(filename, 'r') as file:
			self.text = file.read()

	#Main method for all the transmitter related procedure
	def send(self, receiver):
		print('\nOriginal size: {} bytes'.format(len(self.text))) #Each character is 1 byte
		compressed = compress(self.text)
		print('Compressed size: {} bytes'.format(len(compressed) / 4)) #Each 4 bits are 1 byte
		receiver.receive(compressed)
