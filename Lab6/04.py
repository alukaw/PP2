with open(r"sample.txt", 'r') as file:
	lines = len(file.readlines())
	print('Total Number of lines:', lines)
