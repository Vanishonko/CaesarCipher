while True:
	print("What word would you like to get the word pattern for?")
	word = input()
	if word == '!!':
		break
	wordpattern = ''
	usedLettersList = []

	for i in word:
		if not i in usedLettersList:
			usedLettersList.append(i)	
		wordpattern += str(usedLettersList.index(i)) + '.'

	wordpattern = wordpattern[:-1]

	print(wordpattern)
