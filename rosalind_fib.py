generations = [1]
def fibonacci(k):
	if generations[:-1] == []:
		next_gen = k
		print "ASNKJFNDJF"
	else:
		next_gen = sum(generations[:-1]) * k
	generations.append(next_gen)
	return generations
	
months = 27
for n in range(months - 2):
	fibonacci(3)

print generations
print sum(generations) 