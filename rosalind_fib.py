"""
Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months 
if we begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

SAMPLE:
5 3

Expected Output: 
19
"""

generations = [1]
def fibonacci(k):
	if generations[:-1] == []:
		next_gen = k
	else:
		next_gen = sum(generations[:-1]) * k
	generations.append(next_gen)
	return generations
	
months = 27
for n in range(months - 2):
	fibonacci(3)

print generations
print 'Number of Rabbits: ', sum(generations) 