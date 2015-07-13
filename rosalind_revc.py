"""
Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.  A <=> T and G <=> C

SAMPLE:
AAAACCCGGT

Expected Output:
ACCGGGTTTT
"""

from string import maketrans

file = open('/Users/Anuar_the_great/desktop/rosalind_revc.txt')
data = file.read()
file.close()

def complement_pairs():
	trans_table = maketrans('ATCG', 'TAGC')
	return data[::-1].translate(trans_table)
	

print complement_pairs()