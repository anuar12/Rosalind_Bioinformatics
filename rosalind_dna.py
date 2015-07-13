"""
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of
times that the symbols 'A', 'C', 'G', and 'T' occur in s.

SAMPLE DATASET:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Expected Output:
20 12 17 21
"""


def counter():
	file = open('/Users/Anuar_the_great/desktop/rosalind_dna.txt')
	data = file.read()
	file.close()
	return data.count('A'), data.count('C'), data.count('G'), data.count('T')
	
print counter()