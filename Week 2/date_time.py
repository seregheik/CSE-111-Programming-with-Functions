from datetime import datetime,timedelta 

current_date = str(datetime.now())

print(f'Today is : {current_date}')

two_days =timedelta(days=2)

due = datetime.now() - two_days

print(due)