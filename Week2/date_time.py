from datetime import datetime,timedelta 

# current_date = str(datetime.now())

# print(f'Today is : {current_date}')

two_days =timedelta(days=2)

# due = datetime.now() + two_days

# print(due)
birthday = '15/08/1998'
birthday_date = datetime.strptime(birthday, "%d/%m/%Y")
print(f'{birthday_date:%Y %A %m}')