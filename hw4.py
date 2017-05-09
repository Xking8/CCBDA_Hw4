#!/usr/bin/python
import sys
filenm = sys.argv[1]
sup = 0.3
confidence = 0.3
rule = 0
Tx = {}
C1 = {}
L1 = {}
C2 = {}
L2 = {}
C3 = {}
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

C2t = {}
#start C2 L2
indC2 = 0
for i in xrange(indL1-1):
    for j in xrange(i+1,indL1):
        #print i,",",j
        C2.update( { indC2 : [L1[i],L1[j],0] } )
        C2t.update( { (L1[i],L1[j]):0 } )
        indC2 += 1
        #print L1[i], L1[j]
print "h2" 
for (C2d,[p1,p2,count]) in C2.items():
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
            C2[C2d][2] += 1
            C2t[(p1,p2)] += 1
print "C2t", C2t
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
indC3 = 0
for p1 in C3List[:-2]:
    for p2 in C3List[C3List.index(p1)+1:-1]:
        for p3 in C3List[C3List.index(p2)+1:]:
            #print p1,p2,p3
            C3.update( { indC3 : [p1,p2,p3,0] } )
            indC3 += 1

for (C3d,[p1,p2,p3,count]) in C3.items():
    #print "-------------",C3d
    for Tranc,Tlist in Tx.items():
        p1ck = False
        p2ck = False
        p3ck = False
        for obj in Tlist:
            if obj == p1:
                p1ck = True
            if obj == p2:
                p2ck = True
            if obj == p3:
                p3ck = True
        if p1ck and p2ck and p3ck:
            C3[C3d][3] += 1
    #print "_____________________________"
        

print "C3$$$$",C3
for (C3d,[p1,p2,p3,count]) in C3.items():
    if count < sup_count:
        del C3[C3d]
print "L3:",C3

#finding rules:L2, L3
for (C2d,[p1,p2,count]) in C2.items():
    M = [p1,p2]
    print "M:",M
    for P in M:
        Q = list(M)
        Q.remove(P)
        print "P:",P
        print "Q:",Q
        print Q,"count: ",C1[Q[0]], count
        conf = float(count) / C1[ Q[0] ]
        if conf > confidence:
            print Q[0],"->",P," ",conf
            rule += 1
    print "------"
print rule

print "finding rule: L3"
for (C3d,[p1,p2,p3,count]) in C3.items():
    M = [p1,p2,p3]
    for P in M:     #pick 1 element in P
        Q = list(M)
        Q.remove(P)
        print Q,":",C2t[(Q[0],Q[1])]
        numQ = C2t[(Q[0],Q[1])]
        conf = float(count) / numQ
        if conf > confidence:
            print Q[0],",",Q[1],"->",P," ",conf
            rule += 1
        conf = float (count)/C1[P]
        if conf > confidence:
            print P,"->",Q[0],",",Q[1]," ",conf
            rule += 1
#    for P1 in M[:-1]:     #pick 2 elements
#        for P2 in M[M.index(P1):]:
#            print P1, P2
        
print rule






