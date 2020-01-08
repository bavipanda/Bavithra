english = float(input())
math = float(input())
computers = float(input())
physics = float(input())
chemistry = float(input())

total = english + math + computers + physics + chemistry
average = total / 5
percentage = (total / 500) * 100

print("\nTotal Marks = %.2f"  %total)
print("Average Marks = %.2f"  %average)
print("Marks Percentage = %.2f"  %percentage)
