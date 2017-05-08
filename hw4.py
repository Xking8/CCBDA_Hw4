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
i=0
for line in open(filenm).readlines():
	lis=line.split()
	Tx.update({i:lis})
	i = i+1

num_lines = i
#num_lines = sum(1 for line in open(filenm))
sup_count = int (round(num_lines * sup))

print "sup count:",sup_count
text = (open(filenm)).read().split()

for item in text:
	C1.update({item:C1.get(item,0)})
	C1[item] = C1.get(item,0)+1
indL1=0 #L1 index
for (item,count) in C1.items():
	#print item,count
	if count < sup_count :
		del C1[item]
	else:
		L1.update({indL1:item})
		indL1 = indL1+1

print "L1: ",L1,"indL1:",indL1

#start C2 L2
indC2 = 0
for i in xrange(indL1-1):
	for j in xrange(i+1,indL1):
		#print i,",",j
		C2.update( { indC2 : [L1[i],L1[j],0] } )
		indC2 += 1
		#print L1[i], L1[j]
print "h2" 
for (C2d,[p1,p2,count]) in C2.items():
	print C2d,p1,p2,count
	for Tranc,Tlist in Tx.items():
		#print "Tlist:",Tlist
		p1ck = False
		p2ck = False
		for obj in Tlist:
			if obj == p1 :
				 p1ck = True;
			if obj == p2 :
				 p2ck = True;
		if p1ck and p2ck:
			count += 1
			C2[C2d][2]+=1
print "C2:+++",C2			
C3List = []
for (C2d,[p1,p2,count]) in C2.items():
	if count < sup_count:
		del C2[C2d]
	else:
		if p1 not in C3List:
			C3List.append(p1)
		if p2 not in C3List:
			C3List.append(p2)
		
print "L2:***",C2
print "C3List",C3List,len(C3List)

#start C3 L3



#print "after del"
#for (item,count) in C1.items():
#	print item,count



