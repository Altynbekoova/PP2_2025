import datetime

x = datetime.datetime.now()
y = x - datetime.timedelta(days = 5)

print("current date: " + x.strftime("%Y-%m-%d-%A"))
print("date 5 days ago: " + y.strftime("%Y-%m-%d-%A"))