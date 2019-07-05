from math import log

def compress(text):
	dictionary = {'' : 0}

	pairs = []	#Compressed pairs (index, symbol)
	w = ''

	for c in text:

		#If the new word is in the dictionary another character is read
		if w + c in dictionary:
			w = w + c

		#If it's a new word
		else:
			pairs.append((dictionary[w], c)) #Adding new term to the pairs' list
			dictionary[w + c] = len(dictionary) #Adding the new word to the dicitonary
			w = '' #Reinitializing the word

	#If the last word is already in the dicitonary
	if w != '':
		pairs.append(((dictionary[w]),''))

	return binaryEncode(pairs)


def decompress(compressed):

	pairs = binaryDecode(compressed)

	dictionary = {0 : ''}
	
	decompressed = ''

	for pair in pairs:
		index = pair[0]
		symbol = pair[1]

		word = dictionary[index] + symbol

		#If the word is not already in the dictionary
		if symbol != '':
			dictionary[len(dictionary)] = word	#Add

		decompressed += word

	return decompressed



#So
BitIt = lambda num, length : format(int(bin(num)[2:]), '#0' + str(length)) #Returns binary string of specified length
#just BitIt hooooooo
	
binaryAscii = lambda character : BitIt(ord(character), 7) if character != '' else ''


#Encoding LZ78 compressed pairs to binary
def binaryEncode(pairs):
	encoded = binaryAscii(pairs[0][1])

	for iteration, pair in enumerate(pairs[1:]):
		index = pair[0]
		symbol = pair[1]

		index_len = int(log(iteration + 1, 2) + 1)
		
		encoded += BitIt(index, index_len) + binaryAscii(symbol)

	return encoded

#Decoding binary to LZ78 compressed pairs
def binaryDecode(binary):
	pairs = [(0, chr(int(binary[0:7], 2)))]

	cursor = 7
	iteration = 1

	while cursor < len(binary):
		index_len = int(log(iteration, 2) + 1)

		index = int(binary[cursor : cursor + index_len], 2)
		cursor += index_len

		if cursor < len(binary):
			symbol = chr(int(binary[cursor : cursor + 7], 2))
			cursor += 7
		else:
			symbol = ''

		pairs.append((index,symbol))

		iteration += 1

	return pairs