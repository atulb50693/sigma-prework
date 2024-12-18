
# Task 2: Max and Min


def get_list_of_integers_from_user():
    # Returns a valid list of integers converted to int data type based on user input
    while True:
        user_input = input('Enter a list of integers separated by commas: ')
        list_of_integers = user_input.split(',')
        is_integer = True

        # Checking if every entry is an integer
        for i in list_of_integers:
            i = abs(int(i))
            if not str(i).isdecimal():
                is_integer = False
        
        if is_integer: 
            return [int(i) for i in list_of_integers]
        

def find_max_and_min_of_array(list_of_integers):
    # Takes in a list of integers and returns the highest and lowest number
    sorted_integers = sorted(list_of_integers)
    highest_number = sorted_integers[-1]
    lowest_number = sorted_integers[0]

    return highest_number, lowest_number


# main
list_of_integers = get_list_of_integers_from_user()
max_num, min_num = find_max_and_min_of_array(list_of_integers)

print([min_num, max_num])
