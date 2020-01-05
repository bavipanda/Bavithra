n=int(input())
num=list(map(int,input().split()))
a=0
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(num[i]>=num[j]):
           a=a+1
if(a==0):
   print('yes')
else:
  print('no')
