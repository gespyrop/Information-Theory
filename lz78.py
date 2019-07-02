def compress(text):
	dictionary = {'' : 0}

	compressed = ''
	w = ''

	for c in text:

		#If the new word is in the dictionary another character is read
		if w + c in dictionary:
			w = w + c

		#If it's a new word
		else:
			compressed += '({},{})'.format(str((dictionary[w])), c) #Adding new term to the output
			dictionary[w + c] = len(dictionary) #Adding the new word to the dicitonary
			w = '' #Reinitializing the word

	#If the last word is already in the dicitonary
	if w != '':
		compressed += '({})'.format(str((dictionary[w])), c)

	return compressed


def decompress(compressed):
	dictionary = {0 : ''}

	decompressed = ''

	#Creating a list containing all terms
	terms = compressed.split(')(')
	terms[0] = terms[0][1:]
	terms[-1] = terms[-1][:-1]

	for term in terms:

		#If the term contains a new symbol
		if ',' in term:
			pair = term.split(',')
			index = int(pair[0])
			symbol = pair[1]

			word = dictionary[index] + symbol

			dictionary[len(dictionary)] = word
			decompressed += word

		#If the last word is already in the dicitonary	
		else:
			decompressed += dictionary[int(term)]

	return decompressed