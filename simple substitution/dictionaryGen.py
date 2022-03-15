import wordmapping as wm

dictPatterns = open("patterns.txt", "a")

with open("dictionary.txt", "r") as dictWords:
	line = dictWords.readline()
	while line != '':
		dictPatterns.write(line[:-1] + ': ' + wm.genPattern(line[:-1]) + '\n')
		line = dictWords.readline()