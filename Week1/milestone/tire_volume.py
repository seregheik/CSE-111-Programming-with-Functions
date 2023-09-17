# Osasere Ikponmwosa
import math

tire_width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio =  int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

numerator = math.pi * (tire_width**2)*aspect_ratio*((tire_width*aspect_ratio)+(2540*diameter))
denominator = 10000000000

volume = numerator/denominator

print(f'The approximate volume is {volume:.2f} liters')