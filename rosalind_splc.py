"""
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings 
of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons
of s. Introns should be deleted(Note: Only one solution will exist for the 
dataset provided.) Also T => U.

Sample dataset:
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

Sample output:
MVYIADKQHVASREAYGHMFKVCA
"""

from reader_FASTA import read_FASTA
from rna_to_prot import RNA_to_protein


def RNA_splicing(data, main_dna):
	for id, intron in data.items():
		main_dna[1] = main_dna[1].replace(intron, '')
	main_dna[1] = main_dna[1].replace('T', 'U')
	main_dna[1] = RNA_to_protein(main_dna[1])
	return main_dna
	

file = open('/Users/Anuar_the_great/desktop/Data_files/rosalind_splc.txt')
main_dna = [file.readline()[1:].strip('\n'), file.readline().strip('\n')]
data = file.readlines()
print type(data)
file.close()
# Alternative version for read_FASTA (returns a list instead):
# no_introns = filter(lambda line: line[0] != '>', data)
data = read_FASTA(data)
print RNA_splicing(data, main_dna)


