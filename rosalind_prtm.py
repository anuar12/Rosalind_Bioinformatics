"""
Given: The standard weight assigned to each member of the 20-symbol amino acid
alphabet is the monoisotopic mass of the corresponding amino acid.
A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.

Sample:
SKADYEK

Sample Output:
821.392
"""

import pandas as pd

def protein_mass(data):
	protein_code = ''
	codons_df = pd.read_csv('/Users/Anuar_the_great/desktop/mass_table.txt', delimiter=' ',\
					 index_col=False, header=None, skipinitialspace=True,\
					 keep_default_na=False)
	
	codons_df = codons_df.set_index(codons_df[:][0])
	codons_series = pd.Series(codons_df[:][1])
	data_list = list(data)
	data_list[0] = float(codons_series[data[0]])
	f = lambda x, y: x + float(codons_series[y])
	total_mass = reduce(f, data_list)
	return total_mass


file = open('/Users/Anuar_the_great/desktop/rosalind_prtm.txt')
data = file.read()
file.close()
print protein_mass(data)