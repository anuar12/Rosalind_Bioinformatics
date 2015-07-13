"""
Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.   T ==> U

SAMPLE:
GATGGAACTTGACTACGTAAATT

Expected Output:
GAUGGAACUUGACUACGUAAAUU
"""

from string import maketrans

file = open('/Users/Anuar_the_great/desktop/rosalind_rna.txt')
data = file.read()
file.close()

def DNA_to_RNA1():
	trans_table = maketrans('T', 'U')
	return data.translate(trans_table)
	

def DNA_to_RNA2():
	return 'U'.join(data.split('T'))
	
def DNA_to_RNA3():
    return data.replace('T','U')

print DNA_to_RNA1()
print DNA_to_RNA2()
print DNA_to_RNA3()
