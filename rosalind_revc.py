"""
Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.  A <=> T and G <=> C

SAMPLE:
AAAACCCGGT

Expected Output:
ACCGGGTTTT
"""

from string import maketrans


def complement_pairs(data):
	trans_table = maketrans('ATCG', 'TAGC')
	return data[::-1].translate(trans_table)
	
filepath = '/Users/Anuar_the_great/desktop/code/rosalind_repo/data_files/rosalind_revc.txt'
file = open(filepath)
data = file.read()
file.close()
print complement_pairs(data)