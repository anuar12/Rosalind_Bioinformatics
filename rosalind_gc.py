from __future__ import division

file = open('/Users/Anuar_the_great/desktop/rosalind_gc(2).txt')
data = file.readlines()
dict1 = {}

def formatter():
	for line in data:
		if line[0] == '>':
			id = line[1:-1]
		else:
			try:
				dict1[id] = dict1[id] + line
				dict1[id] = dict1[id].translate(None, '\n')
			except KeyError:
				dict1[id] = line
	return dict1
	

def gc_content(dict1):
	dict2 = {}
	for key, value in dict1.items():
		#print key, value
		percent = 100 * (value.count('G') + value.count('C')) / len(value)	
		dict2[key] = percent
	max_percent_key = max(dict2, key=dict2.get)
	return max_percent_key, dict2[max_percent_key]

dict = formatter()	
print gc_content(dict)