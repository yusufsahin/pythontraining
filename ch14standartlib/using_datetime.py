from datetime import datetime,timedelta

now=datetime.now()

dt=datetime(2023, 5, 29, 12, 0, 0)
print(dt)

delta=timedelta(days=5)
future_date=now+delta
print(future_date)

print(dt+delta)