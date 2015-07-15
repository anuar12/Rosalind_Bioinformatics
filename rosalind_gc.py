"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed 
by the GC-content of that string. 

SAMPLE:
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Expected Output:
Rosalind_0808
60.919540
"""

from __future__ import division
from reader_fasta import read_fasta

file = open('/Users/Anuar_the_great/desktop/rosalind_gc(2).txt')
data = file.readlines()
file.close()


def gc_content(dict1):
	dict2 = {}
	for key, value in dict1.items():
		percent = 100 * (value.count('G') + value.count('C')) / len(value)	
		dict2[key] = percent
	max_percent_key = max(dict2, key=dict2.get)
	return max_percent_key, dict2[max_percent_key]


dict = read_fasta(data)	
print gc_content(dict)