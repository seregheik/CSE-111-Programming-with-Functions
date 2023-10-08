# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime

def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('Please enter your gender M/F: ')
    birthday = input('Please enter your date of birth YYYY-MM-DD: ')
    weight = float(input('Please enter your weight (US pounds): '))
    height = float(input('Please enter your height (US inches): '))
    
    # Call the compute_age, kg_from_lb, cm_from_in,
    full_age = compute_age(birth_str=birthday)
    weight_in_kg = float(kg_from_lb(weight))
    height_in_cm = cm_from_in(height)
    bmr = basal_metabolic_rate(gender=gender, weight=weight_in_kg, height=height_in_cm, age=full_age)
    bmi = body_mass_index(weight=weight_in_kg, height=height_in_cm)
    
    print(f'Age (years): {full_age}')
    print(f'Weight (kg): {weight_in_kg:.2f}')
    print(f'Height (cm): {height_in_cm:.1f}')
    print(f'Body mass index: {bmi:.1f}')
    print(f'Basal metabolic rate (kcal/day): {bmr:.0f}')
    

def compute_age(birth_str):
    # Convert a person's birthdate from a string
    # to a date object.
    birthday_formatted = datetime.strptime(birth_str,'%Y-%m-%d')
    today = datetime.now()
    
    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthday_formatted.year

    # If necessary, subtract one from the difference.
    if birthday_formatted.month > today.month or (birthday_formatted.month == today.month and \
            birthday_formatted.day > today.day):
        years -= 1
    return years
def kg_from_lb(pounds):
    kg_weight = pounds * 0.45359237
    return kg_weight
def cm_from_in(inches):
    cm_height = inches * 2.54
    return cm_height
def body_mass_index(weight, height):
    bmi = (10000*weight)/(height*height)
    return bmi
def basal_metabolic_rate(gender, weight, height, age):
    gender = gender[0].upper()
    if gender == 'F':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    elif gender == 'M':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    return bmr

main()