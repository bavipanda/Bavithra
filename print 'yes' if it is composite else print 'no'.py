N=int(input())
factor=0
for i in range(1,N):
  if N%i==0:
    factor=i
if factor>1:
  print ('yes')
else:
  print ('no')
