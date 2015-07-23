"""
A DNA string is a reverse palindrome if it is equal to its reverse complement. 
For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having 
length between 4 and 12. You may return these pairs in any order.

Sample:
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output:
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
"""
from rev_complem import reverse_complements

def rev_palind(dna):
	for length in range(4, 13):
		possible_palins = [dna[i:length+i] for i in range(len(dna) - length + 1)]
		for ind, possible_palin in enumerate(possible_palins):
			if possible_palin == reverse_complements(possible_palin):
				print ind + 1, length
	return


file = open('/Users/Anuar_the_great/desktop/code/rosalind_repo/data_files/rosalind_revp.txt')
file.readline()
dna = file.readlines()
dna = ''.join(dna).replace('\n', '')
file.close()

rev_palind(dna)