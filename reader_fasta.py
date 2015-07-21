# Reads the FASTA formated data that is used for naming genetic strings for DBs

def read_FASTA(data):
	dict1 = {}
	#for line in data.splitlines():   # If your data is a sample string
	for line in data:
		if line[0] == '>':
			id = line[1:]
			id = id.translate(None, '\n')
		else:
			try:
				dict1[id] = dict1[id] + line
				dict1[id] = dict1[id].translate(None, '\n')
			except KeyError:
				dict1[id] = line
				dict1[id] = dict1[id].translate(None, '\n')
	return dict1
	
	