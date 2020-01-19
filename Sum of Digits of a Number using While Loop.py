Number = int(input())
Sum = 0

while(Number > 0):
    Reminder = Number % 10
    Sum = Sum + Reminder
    Number = Number //10

print("\n Sum of the digits of Given Number = %d" %Sum)
