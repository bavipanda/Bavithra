import math
N,M=map(int,input().split())
root = math.sqrt(N)
if int(root + 0.5) ** 2 ==N:
    print('no')
else:
    print('yes')
