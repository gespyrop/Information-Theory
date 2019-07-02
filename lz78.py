def compress(text):
	dictionary = {'' : 0}

	compressed = ''
	w = ''
	for c in text:
		if w + c in dictionary:
			w = w + c
		else:
			compressed += '({},{})'.format(str((dictionary[w])), c)
			dictionary[w + c] = len(dictionary)
			w = ''

	if w != '':
		compressed += '({})'.format(str((dictionary[w])), c)

	return compressed


def decompress(compressed):
	pass