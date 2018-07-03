#set operations


A=set([1,2,3,4,1]);
B=set([2,3,6,1,8]);
print "set A"
print A
print "set B" 
print B
print len(A)
print "union set"
print A.union(B)
print "intersection set"
print A.intersection(B)
print "symmetric differance: "
print A^B
print "difference: A-B "
print A-B
print "difference: B-A "
print B-A

