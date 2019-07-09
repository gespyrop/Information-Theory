from base64 import b64decode
from linear_code import LC
from lz78 import decompress
from json import loads

class Receiver:
	def __init__(self):
		pass

	#Main method for all the receiver related procedure
	def receive(self, json):
		info = loads(json)
		print("\nJSON received!")

		base64encoded = info["base64encoded"]
		print("\nDecoding with base64...")
		encoded = b64decode(base64encoded)

		code = info["code"]

		if code["name"] == "linear":
			print("\nDecoding with Linear Code...")
			P = code["P"]
			L = LC(P, 0)
			compressed = L.decode(encoded)
		else:
			compressed = ''


		if info["compression_algorithm"] == "LZ78":
			print("\nDecompressing with LZ78...")
			decompressed = decompress(compressed)
		else:
			decompressed = ''

		print("\nDecompressed message: {}".format(decompressed))