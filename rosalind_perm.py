"""
A permutation of length n is an ordering of the positive integers {1,2,…,n}. 
For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of 
all such permutations (in any order).

Sample dataset:
3

Sample Output:
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

from math import factorial
from itertools import permutations

# The number of permutations is just a factorial of the number of numbers given
def num_of_perms(n):
	return factorial(n)
	
	
def perms(n):
	return list(permutations(range(1, n+1)))
	

n = 3
possible_perms = perms(n)
print num_of_perms(n)
print len(possible_perms)
for perm in possible_perms:
	for i in range(n):
		print perm[i],
	print ''