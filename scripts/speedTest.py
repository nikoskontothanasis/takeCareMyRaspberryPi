import os,mmap
filepath = sys.argv[1]
with open(filepath, 'r') as f:
	for line in f:
		if 'Download:' in line:
			totalValue=line.split(":")[1].strip()
			totalValue=totalValue.split(" ")[0].strip()
print(totalValue)