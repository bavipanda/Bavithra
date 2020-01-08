def compound_interest(principle, rate, time):
    result = principle * (pow((1 + rate / 100), time))
    return result
 
 
p,r,t =map(float,input().split())
amount = compound_interest(p, r, t)
interest = amount - p
print("Compound amount is %.2f" % amount)
print("Compound interest is %.2f" % interest)
