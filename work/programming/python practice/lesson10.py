import datetime

a = datetime.datetime.now()

b = datetime.timedelta(hours=2, minutes=32)
c = b + a
print('время через 2 часа 32 минуты: ' + c.strftime('%H:%M:%S'))

d = datetime.timedelta(days=5)
c = d + a
print('время дата через 5 дней: ' + c.strftime('%D'))
