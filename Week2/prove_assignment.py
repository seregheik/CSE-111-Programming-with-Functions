# Osasere Ikponmwosa
import math
from datetime import datetime,timedelta

tire_width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio =  int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))


numerator = math.pi * (tire_width**2)*aspect_ratio*((tire_width*aspect_ratio)+(2540*diameter))
denominator = 10000000000

volume = numerator/denominator
volume = f'{volume:.2f}'
current_time = datetime.now()
saved_current_time = f'{current_time:%Y-%m-%d}'


print(f'The approximate volume is {volume} liters')

buy_tire = input('Do you want to purchase a tire? Yes/No: ').capitalize()
if buy_tire == 'Yes':
    phone_number = input('Please enter your phone number: ')
else:
    print('Have a nice day')
with open ('volumes.txt', mode='+at', encoding= 'UTF-8') as volumes_txt_file:
    print(f'{saved_current_time}, {tire_width}, {aspect_ratio}, {diameter}, {volume}, {phone_number}', file=volumes_txt_file)