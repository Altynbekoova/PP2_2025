import datetime

date1 = datetime.datetime(2025, 2, 1, 13, 2, 0)  
date2 = datetime.datetime(2025, 2, 10, 14, 59, 0) 

sec = abs((date2 - date1).total_seconds())

print("Difference in seconds:", sec)