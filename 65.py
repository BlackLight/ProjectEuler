n, d, i = 2, 1, 100
while i>0:
  c = 1
  if i%3 == 0: c = 2*i/3
  n, d, i = d, c*d+n, i-1
print "Answer to PE65 = ", sum(int(i) for i in str(d))
