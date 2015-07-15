"""
Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month
if all rabbits live for m months.

Sample:
6 3

Sample Output:
4
"""

duration = 6
lifespan = 3
adults = [1] + [0] * (lifespan - 1)

def mortal_fib():
	for year in range(1, duration):
		newborns = 0
		for j in range(1, lifespan):
			newborns += adults[(year - j - 1) % lifespan]
		adults[(year) % lifespan] = newborns
	return sum(adults)


print mortal_fib()




