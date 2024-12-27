
# Task 1: Age Calculator

import datetime


def get_date_from_user():
    # Gets a valid date from the user in the form of 'dd-mm-yyyy' and returns this string
    while True:
        date_inputted = input("Enter a date in the form 'dd-mm-yyyy': ")
        input_check_list = date_inputted.split('-')
        wrong_format = False

        # Checking if input passed is non-decimal
        if not date_inputted.replace('-', '').isdecimal():
            wrong_format = True
            continue
        
        # checking if the format is correct (hyphen in correct place, not longer than format, numbers given in required format)
        for i, chr in enumerate(date_inputted):
            if (i in (2,5) and chr != '-') or len(date_inputted) > 10:
                wrong_format = True
            elif i not in (2,5) and not chr.isdecimal():
                wrong_format = True
        
        # Checking if the number is within the specified range for days (31 in month) and months (12 in year)
        for i, number in enumerate(input_check_list):
            if (i == 0 and not (1 <= int(number) <= 31)) or (i == 1 and not (1 <= int(number) <= 12)):
                wrong_format = True
            
        # If formatting is correct and a valid date, then user-input is returned
        if not wrong_format:
            return date_inputted
        

def convert_string_to_date_object(date_string):
    # Converts a string that has a date in the format of dd-mm-yyyy and returns a datetime object
    converted_string = datetime.date(
        day=int(date_string[:2]),
        month=int(date_string[3:5]),
        year=int(date_string[6:]))
    return converted_string


def find_age(date_of_birth):
    # Takes in datetime object and finds the difference between today and then to calculate the age which is returned
    date_today = datetime.date.today()
    age_of_user = (date_today - date_of_birth).days // 365
    return age_of_user


# Main program - displays age of date given by user

date_inputted = get_date_from_user()

user_date_converted = convert_string_to_date_object(date_inputted)

age_of_user = find_age(user_date_converted)

print(f"If you were born on {date_inputted}, then you would be {age_of_user} years old.")

