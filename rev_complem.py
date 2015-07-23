from string import maketrans

def reverse_complements(data):
	trans_table = maketrans('ATCG', 'TAGC')
	return data[::-1].translate(trans_table)