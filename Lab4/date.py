#Task1

import datetime 
now = datetime.datetime.now()
five_days_ago = now - datetime.timedelta(days = 5)
print(five_days_ago)

#Task2

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print(today)
print(yesterday)
print(tomorrow)

#Task3

print(today.strftime('%Y/%m/%d, %H:%M:%S'))

#Task4

difference = today - five_days_ago
print(difference.days)