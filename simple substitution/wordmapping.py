def genPattern(word):
	wordpattern = ''
	usedLettersList = []
	for i in word:
		if not i in usedLettersList:
			usedLettersList.append(i)	
		wordpattern += str(usedLettersList.index(i)) + '.'
	usedLettersList.clear()
	return wordpattern[:-1]
