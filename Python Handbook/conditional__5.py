"""conditional statements"""
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
weekend = ["saturday", "sunday"]
TODAY = "Friday"
TOMMOROW = "Saturday"


# if
if  5 > 4:
    print("5 is greater than 4")

# if-else
if  TODAY.lower() in weekdays:
    print("today is a weekday")
else:
    print("today is weekend")

# if-elif-else
# use if-elif-else if you want only one block to execute out of several
# use if-if if you want only several blocks based on some conditions
# you can omit the else block if needed
if  TOMMOROW.lower() in weekdays:
    print("tomorrow is a weekday")
elif TOMMOROW.lower() in weekend:
    print("tomorrow is weekend")
else:
    print("tomorrow is not your day")
