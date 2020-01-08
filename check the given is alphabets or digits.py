ch = input()
if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print("is an Alphabet") 
elif(ch >= '0' and ch <= '9'):
    print("is a Digit")
else:
    print("is Not an Alphabet or a Digit")
