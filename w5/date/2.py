import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(yesterday.strftime("%Y-%m-%d-%A"))
print(today.strftime("%Y-%m-%d-%A"))
print(tomorrow.strftime("%Y-%m-%d-%A"))