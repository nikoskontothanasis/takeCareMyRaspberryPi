import os,mmap

with open('test.txt', 'r') as f:
	for line in f:
		if 'Download:' in line:
			totalValue=line.split(":")[1].strip()
			totalValue=totalValue.split(" ")[0].strip()
print(totalValue)