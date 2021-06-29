from datetime import datetime
# from datetime import date
# from datetime import time

# import datetime

simdi = datetime.now()
result = simdi.year
result = simdi.hour
result = simdi.today
result = simdi.second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y')
result = datetime.strftime(simdi,'%H')

t = '6 May 2021 hour 15:30:31'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(2002, 4, 29,12,30,10)

result = datetime.timestamp(birthday)
result = datetime.fromtimestamp(birthday)

print(result)

