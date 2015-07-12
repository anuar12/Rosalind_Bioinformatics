from string import maketrans

file = open('/Users/Anuar_the_great/desktop/rosalind_revc.txt')
data = file.read()

def complement_pairs():
	trans_table = maketrans('ATCG', 'TAGC')
	return data[::-1].translate(trans_table)
	

print data
print complement_pairs()