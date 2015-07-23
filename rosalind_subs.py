"""
Given: Two DNA strings s (DNA strand) and t (motif).

Return: All locations of t as a substring of s. (non-pythonic locations, added by 1)

Sample:
GATATATGCATATACTT
ATAT

Sample Output:
2 4 10
"""

def motifs1():
	lists = []
	for i in range(len(motif)):
		lists.append(dna[i:])
	n_bases = [ ''.join(string) for string in zip(*[shift_list for shift_list in lists])]
	ans = [index+1 for index, base_n in enumerate(n_bases) if base_n == motif]
	
	for i in range(len(ans)):
		print ans[i],
	
	return
	
def motifs2():
	position_list = []
	for i in range(len(dna)-len(motif)+1):
		position_list.append(dna.find(motif, 0+i, len(motif)+i) + 1)
	position_set = set(position_list)
	position_set.remove(0)
	return position_set


file = open('/Users/Anuar_the_great/desktop/rosalind_subs.txt')
dna = file.readline()
motif = file.readline()
file.close()

motifs1()
print ''
print motifs2()
