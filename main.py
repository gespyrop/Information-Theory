from transmitter import Transmitter
from receiver import Receiver

transmitter = Transmitter()
receiver = Receiver()

try:
	filename = raw_input("Insert file name: ")

	transmitter.readTextFromFile(filename)
	transmitter.send(receiver)
except IOError:
	print("File '{}' not found!".format(filename))