#WARNING 'sagemath' required for linear_code.py to run.Run as 'sage main.py'

from transmitter import Transmitter
from receiver import Receiver
from linear_code import LC
from random import randint

transmitter = Transmitter()
receiver = Receiver()

try:
	filename = raw_input("Insert file name: ")
	try:
		P = input("\n(Press ENTER to use a default [13, 3] linear code option)\nInsert P matrix as list of lists(rows): ")
	except Exception:
		P = [[0, 1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 1, 1, 0, 1, 0, 1], [1, 1, 0, 0, 0, 0, 0, 1, 1, 1]]

	print("Warning: Current code can correct up to {} errors per word!\n".format(LC.getErrorCorrectingCapability(P)))
	maxNoise = int(raw_input("Insert max noise per word: "))

	transmitter.readTextFromFile(filename)
	transmitter.send(receiver, P, maxNoise)
except IOError:
	print("File '{}' not found!".format(filename))
