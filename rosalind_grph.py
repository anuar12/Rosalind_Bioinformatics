"""
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: For a collection of strings and a positive integer k, the overlap graph for
the strings is a directed graph Ok in which each string is represented by a node, and 
string s is connected to string t with a directed edge when there is a length k 
suffix of s that matches a length k prefix of t, as long as s!=tThe adjacency list 
corresponding to O3. You may return edges in any order.

Sample:
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

Sample Output:
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""

from reader_FASTA import read_FASTA

file = open('/Users/Anuar_the_great/desktop/rosalind_grph(1).txt')
data = file.readlines()
file.close()
	
def adjacency_list1(dict):
	leest = []
	for key1, value1 in dict.items():
		for key2, value2 in dict.items():
			if key1 != key2:
				if value1.endswith(value2[0:3]):
					leest.append([key1, key2])
	
	return leest
	
# More optimized code (same logic but uses list comprehension)
def adjacency_list2(dict):
	return [[key1, key2] for key1, value1 in dict.items() for key2, value2 in dict.items()\
		    if key1 != key2 if value1.endswith(value2[0:3])]

dict = read_FASTA(data)
leest1 = adjacency_list1(dict)
leest2 = adjacency_list2(dict)
for nodes1, nodes2 in zip(leest1, leest2):
	print nodes1[0], nodes1[1], '; ', nodes2[0], nodes2[1]