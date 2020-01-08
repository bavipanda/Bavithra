weekNumber = input("Enter the week number:")
weekNumber = int(weekNumber)

if (weekNumber == 1):
  weekDay = "Saturday"
elif (weekNumber == 2):
  weekDay = "Sunday"
elif (weekNumber == 3):
  weekDay = "Monday"
elif (weekNumber == 4):
  weekDay = "Tuesday"
elif (weekNumber == 5):
  weekDay = "Wednesday"
elif (weekNumber == 6):
  weekDay = "Thursday"
elif (weekNumber == 7):
  weekDay = "Friday"
else:
  weekDay = "Please enter the week number between 1 and 7"
  
print weekDay
