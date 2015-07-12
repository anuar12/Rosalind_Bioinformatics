from string import maketrans

file = open('/Users/Anuar_the_great/desktop/rosalind_rna.txt')
data = file.read()

def DNA_to_RNA():
	trans_table = maketrans('T', 'U')
	return data.translate(trans_table)
	

def DNA_to_RNA2():
	return 'U'.join(data.split('T'))

print DNA_to_RNA()
print DNA_to_RNA2()
