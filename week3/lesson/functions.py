from datetime import datetime
# def initial(name, uppercase=True):
#     if uppercase:
#         alphabet = name[0].upper()
#     else:
#         alphabet = name[0]
#     return alphabet
# def get_full_initials(first_name,last_name): 
#     initials = initial(first_name, False) + initial(last_name)
#     return (initials)
# firstname = 'osas'
# lastname = 'ikponmwosa'
# print(get_full_initials(first_name=firstname, last_name=lastname)) 
def compute_age():
    # Convert a person's birthdate from a string
    # to a date object.
    birthday_formatted = datetime.strptime('2003-11-26','%Y-%m-%d')
    # today = datetime.now()
    print(birthday_formatted)
    
    # Compute the difference between today and the
    # person's birthdate in years.
    # years = today.year - birthday_formatted.year

    # # If necessary, subtract one from the difference.
    # if birthday_formatted.month > today.month or (birthday_formatted.month == today.month and \
    #         birthday_formatted.day > today.day):
    #     years -= 1
    # return years

compute_age()