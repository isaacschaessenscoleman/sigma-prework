import datetime

date = input('Enter a date in the following format DD-MM-YEAR: ').split('-')
day, month, year = int(date[0]), int(date[1]), int(date[2])
inputted_date = datetime.date(year, month, day)

todays_date = datetime.datetime.today().date()

age = (todays_date - inputted_date).days / 365.25

age_format = "%.1f" % age

print(f"It's been {age_format} years since that date!")


# simply a test to see if i can clone, modify and push changes
