"""
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could
have been translated, modulo 1,000,000. (Don't neglect the importance of the stop
 codon in protein translation.)
 
Sample:
MA

Sample Output:
12 
"""

import pandas as pd

file = open('/Users/Anuar_the_great/desktop/rosalind_mrna.txt')
data = file.read()
file.close()

def protein_to_mRNA():
	sample = 'MAV'
	codons_df = pd.read_csv('/Users/Anuar_the_great/desktop/codons.txt', delimiter=' ',\
					 header=None, skipinitialspace=True,\
					 keep_default_na=False)
	codons_df = codons_df.set_index(codons_df[:][1])
	codons_series = pd.Series(codons_df[:][0])
	
	num = 1
	for amino in data:
		if type(codons_series[amino]) == str:
			pass
		else:
			num *= len(codons_series[amino])
	num *= 3
	return num
	

print protein_to_mRNA() % 1000000