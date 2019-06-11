from transmitter import Transmitter
from receiver import Receiver

transmitter = Transmitter()
receiver = Receiver()

try:
	filename = input("Insert file name: ")

	transmitter.readTextFromFile(filename)
	transmitter.send(receiver)
except FileNotFoundError:
	print("File '{}' not found!".format(filename))