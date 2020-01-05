b,h=map(int,input().split())
for i in range (2,100):
	if(b%i==0 and h%i==0):
		print(i)
