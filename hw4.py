#!/usr/bin/python
import sys
filenm = sys.argv[1]
sup = 0.3
confidence = 0.3
Tx = {}
C1 = {}
L1 = {}
C2 = {}
L2 = {}
#print sys.argv[1], sys.argv[2]
i=1
for line in open(filenm).readlines():
	lis=line.split()
	Tx.update({i:lis})
	i = i+1

num_lines = sum(1 for line in open(filenm))
sup_count = num_lines * sup

print "sup count:",sup_count
text = (open(filenm)).read().split()

for item in text:
	C1.update({item:C1.get(item,0)})
	C1[item] = C1.get(item,0)+1
indL1=1 #L1 index
for (item,count) in C1.items():
	#print item,count
	if count < sup_count :
		del C1[item]
	else:
		L1.update({indL1:item})
		indL1 = indL1+1

print "L1: ",L1



#print "after del"
#for (item,count) in C1.items():
#	print item,count



