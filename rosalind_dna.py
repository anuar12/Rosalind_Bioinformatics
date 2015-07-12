def counter():
	file = open('/Users/Anuar_the_great/desktop/rosalind_dna.txt')
	data = file.read()
	return data.count('A'), data.count('C'), data.count('G'), data.count('T')
	
print counter()