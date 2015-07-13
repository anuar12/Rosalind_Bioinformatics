"""
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t), which is the number of corresponding symbols 
that differ in s and t.

Sample:
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Expected Output:
7
"""

file = open('/Users/Anuar_the_great/desktop/rosalind_hamm.txt')
line1 = file.readline()
line2 = file.readline()
file.close()

def point_mutations1():
	mutations = 0
	for i in range(len(line1)):
		print line1[i]
		if line1[i] == line2[i]:
			pass
		else:
			mutations += 1
	return mutations
	

def point_mutations2():
	line1 = list(line1)
	line2 = list(line2)
	mutations = len([i for i in range(len(line1)) if line1[i] != line2[i]])
	return mutations
	
	
# The most optimized code:
def point_mutations3():
	return sum(a != b for a, b in itertools.izip(line1, line2))
	
print point_mutations1()
print point_mutations2()
print point_mutations3()
