n=int(input())
num=list(map(int,input().split()))
minimum=sorted(num)
maximum=minimum[::-1]
a=[]
for i in range(len(num)):
    a.append(maximum[i])
    a.append(minimum[i])
print(*a[:n])
