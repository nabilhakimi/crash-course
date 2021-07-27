from datetime import datetime, timedelta

'''
current_date = datetime.now()
one_day = timedelta(days = 1)
one_week = timedelta(weeks = 1)

yesterday = current_date - one_day
last_week = current_date - one_week
last_year = current_date - one_year

print("Today is: " + str(current_date))
print("Yesterday was: " + str(yesterday))
print("Last week was: " + str(last_week))
'''

birthday = input("when is your birthday (dd/mm/yyyy)? \n")

birthday_date = datetime.strftime(birthday, '%d/%m/%Y')

print("Birthday: " + str(birthday_date))