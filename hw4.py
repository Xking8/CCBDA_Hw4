#!/usr/bin/python
sup = 0.01
confidence = 0.6
C1 = {}

f = open("T40I10D100K.dat")
text = f.read().split()

num_lines = sum(1 for line in open('T40I10D100K.dat'))
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
