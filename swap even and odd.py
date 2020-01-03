s=str(input())
t=list(s)
t[::2],t[1::2]=t[1::2],t[::2]
i=''.join(t)
print(i)
