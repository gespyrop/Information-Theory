from lz78 import compress

class Transmitter:
	def __init__(self):
		self.text = '';

	def readTextFromFile(self, filename):
		with open(filename, 'r') as file:
			self.text = file.read()

	#Main method for all the transmitter related procedure
	def send(self, receiver):
		receiver.receive(self.text)