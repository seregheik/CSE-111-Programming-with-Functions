from datetime import datetime,timedelta
date = '15/08/1998'
date_of_birth = datetime.strptime(date, '%d/%m/%Y')
name = 'Osasere'

with open("osasere.txt", mode='+rt', encoding='UTF-8') as osasere:
    print(name,date_of_birth,file=osasere)
