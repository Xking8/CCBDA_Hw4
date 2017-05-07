#!/usr/bin/python
import sys
filenm = sys.argv[1]
sup = 0.3
confidence = 0.3

C1 = {}
#print sys.argv[1], sys.argv[2]

f = open(filenm)
text = f.read().split()
f.close()
num_lines = sum(1 for line in open(filenm))
sup_count = num_lines * sup
print "sup count:",sup_count

for item in text:
	C1.update({item:C1.get(item,0)})
	C1[item] = C1.get(item,0)+1
for (item,count) in C1.items():
	print item,count
	if count < sup_count :
		del C1[item]
		#print "del--------------------------------------------------------------"
		#print item,count
print "after del"
for (item,count) in C1.items():
	print item,count

f = open(filenm)



