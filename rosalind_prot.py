"""
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s according to the codon table.

Sample:
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output:
MAMAPRTEINSTRING
"""

import pandas as pd

file = open('/Users/Anuar_the_great/desktop/rosalind_prot.txt')
data = file.read()
file.close()

def splitter(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]

def RNA_to_protein():
	protein_code = ''
	codons_df = pd.read_csv('/Users/Anuar_the_great/desktop/codons.txt', delimiter=' ',\
					 index_col=False, header=None, skipinitialspace=True,\
					 keep_default_na=False)
	
	codons_df = codons_df.set_index(codons_df[:][0])
	codons_series = pd.Series(codons_df[:][1])
	triples = splitter(data, 3)
	for triple in triples:
		protein_code += codons_series[triple]
	return protein_code
	

print RNA_to_protein()