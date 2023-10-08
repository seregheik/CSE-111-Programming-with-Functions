
def main():
    start_odometer_value = float(input('Enter starting odometer value (miles): '))
    end_odometer_value = float(input('Enter ending odometer value (miles): '))
    fuel_used = float(input('Enter ammount of fuel used (gallons): '))
    efficiency= miles_per_gallon(start=start_odometer_value,end=end_odometer_value,gallons=fuel_used)
    converted = lp100k_from_mpg(efficiency)
    print(f'{efficiency:.1f} miles per gallon')
    print(f'{converted:.2f} liters per 100 kilometers')
    # print(f'{lp100k_from_mpg()}')
    

def miles_per_gallon(end=0,start=0,gallons=0):
    mpg = (end - start)/gallons
    return mpg
def lp100k_from_mpg(mpg=0):
    lp100k = 235.215/mpg
    return lp100k

main()