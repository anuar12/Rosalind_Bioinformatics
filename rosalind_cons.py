"""
Given: A collection of at most 10 DNA strings of equal length in FASTA format.

Return: A consensus string and profile matrix for the collection. 
(If several possible consensus strings exist, then you may return any one of them.)

Sample:
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample Output:
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""

file = open('/Users/Anuar_the_great/desktop/rosalind_cons(7).txt')
data = file.read()
file.close()

import pandas as pd
pd.set_option('display.max_columns', len(data.splitlines()[1]))
pd.set_option('display.width', 1000)

index = range(len(data.splitlines()[1]))
columns = ['A', 'C', 'G', 'T']
profile_df = pd.DataFrame(index=index, columns=columns)
profile_df = profile_df.fillna(0)

def profiler():
	for line in data.splitlines():
		if line[0] == '>':
			pass
		else:
			for index, letter in enumerate(line):
				profile_df[letter][index] += 1
	
	return profile_df.T


def consensus(df):
	leest = []
	for i in index:
		leest.append(df[i].idxmax())
	return ''.join(leest)


df = profiler()
print df
print consensus(df)