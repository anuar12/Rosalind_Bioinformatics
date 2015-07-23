"""
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
We say that a common substring is a longest common substring if there does not exist 
a longer common substring.

Return: A longest common substring of the collection. (If multiple solutions exist, 
you may return any single solution.)

Sample:
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output:
AC     (or TA)
"""
# Brute Force (Naive Search) solution presented.
# For more optimized algorithm, see Rabin–Karp algorithm which is the most suited
# for multiple pattern search that uses hashed values.

from reader_FASTA import read_FASTA


def common_finder(n):
	possible_commons = [first_piece[i:n+i] for i in range(len(first_piece) - n + 1)]
	for common_str in possible_commons:
		for ind, dna_list in enumerate(all_dna_pieces[1:]):
			if common_str not in dna_list:
				break
			elif ind == len(all_dna_pieces) - 2:
				return common_str
			else:
				continue
	return 


file = open('/Users/Anuar_the_great/desktop/rosalind_lcsm.txt')
data = file.readlines()
all_dna_pieces = read_FASTA(data).values()
first_piece = all_dna_pieces[0]
file.close()
for i in range(len(min(all_dna_pieces)), 1, -1 ):
	if common_finder(i):
		least_common_str = common_finder(i)
		print least_common_str
		break