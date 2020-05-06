import os,mmap,sys

def returnValue(value):
	return value

filepath = sys.argv[1]
with open(filepath, 'r') as f:
	for line in f:
		if 'Download:' in line:
			totalValue=line.split(":")[1].strip()
			totalValue=totalValue.split(" ")[0].strip()
print(totalValue)
returnValue(totalValue)
