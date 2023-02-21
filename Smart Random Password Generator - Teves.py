# Joshua Munich Teves
# CSCI 101 - Section C (Fall 2020)
# Create Project
# References: 101 Lab 9 code, https://note.nkmk.me/en/python-random-shuffle/ for (random.shuffle()) usage in line 313
# https://www.youtube.com/watch?v=mHezNgNBnuA for time module and lines 385 and 386
# Time: 6hrs 30mins

"""
min_char = str(input("Please enter the minimum number of characters required for the password. "))
max_char = str(input("Please enter the maximum number of characters required for the password. "))
uppercase_char = str(input("Please enter the minimum number of uppercase characters required. "))
special_char = str(input("Please enter the minimum number of special characters required. "))
number_char = str(input("Please enter the minimum number of number characters required. "))
"""

import random
import time

def min_check(min_char):
    #min_char = str(input("Please enter the minimum number of characters required for the password. "))
    min_integer_check = True
    if min_char.isdigit():
        min_integer_check = True
        return min_integer_check
    else:
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("ERROR: Please enter a positive integer with a value of at least 0 for the minimum character amount, no floats or strings.")
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        min_integer_check = False
        return min_integer_check

#test_run = min_check()


def max_check(min_char, max_char):
    #max_char = str(input("Please enter the maximum number of characters required for the password. "))
    max_integer_check = True
    if max_char.isdigit():
        max_integer_check = True
        #return max_integer_check
    else:
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("ERROR: Please enter a positive integer with a value of at least 0 for the maximum character amount, no floats or strings.")
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        max_integer_check = False
        return max_integer_check

    min_max_check= True
    min_char = int(min_char)
    max_char = int(max_char)
    if min_char > max_char:
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("ERROR: Please enter a maximum character amount that is greater than or equal to the minimum number of characters.")
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        min_max_check = False
        return min_max_check
    else:
        return min_max_check

#min_char = 3
#test_run = max_check(min_char)


def uppercase_check(min_char, max_char, uppercase_char):
    #uppercase_char = str(input("Please enter the minimum number of characters required to be uppercase. "))
    uppercase_check = True
    min_char = int(min_char)
    max_char = int(max_char)
    if uppercase_char.isdigit():
        uppercase_check = True
        #return min_integer
    else:
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("ERROR: Please enter an uppercase character requirement with a value of at least 0, no floats or strings.")
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        uppercase_check = False
        return uppercase_check

    uppercase_char = int(uppercase_char)
    if uppercase_char > max_char:
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("ERROR: Minimum number of characters required to be uppercase is greater than the maximum number of characters initially input.")
        print("Please enter the minimum number of characters required to be uppercase again (with a value less than the maximum character amount.)")
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        uppercase_check = False
        return uppercase_check
    else:
        #print(uppercase_check)
        return uppercase_check

#min_char = 3
#max_char = 16
#test_run = uppercase_check(min_char, max_char)


def special_check(min_char, max_char, uppercase_char, special_char):
    #special_char = str(input("Please enter the minimum number of special characters required. "))
    special_check = True
    min_char = int(min_char)
    max_char = int(max_char)
    if special_char.isdigit():
        special_check = True
        #return special_check
    else:
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("ERROR: Please enter a special character requirement with a value of at least 0, no floats or strings.")
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        special_check = False
        return special_check

    special_char = int(special_char)
    if special_char > max_char:
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("ERROR: Minimum number of special characters is greater than the maximum number of characters initially input.")
        print("Please enter the minimum number of special characters again (with a value less than the maximum character amount.)")
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        special_check = False
        return special_check

    uppercase_char = int(uppercase_char)
    extra_conditions = uppercase_char + special_char
    if extra_conditions > max_char:
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("ERROR: The sum of the character requirements for uppercase and special characters is greater than the maximum character amount.")
        print(f"Uppercase characters: {uppercase_char}")
        print(f"Special characters: {special_char}")
        print(f"Sum: {extra_conditions} > Maximum characters: {max_char}")
        print("Please enter an uppercase or special character amount that will not lead to the sum of uppercase and special characters to be greater than the maximum character amount.")
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        special_check = False
        return special_check
    else:
        #print(special_check)
        return special_check

#min_char = 3
#max_char = 16
#uppercase_char = 5
#test_run = special_check(min_char, max_char, uppercase_char)


def number_check(min_char, max_char, uppercase_char, special_char, number_char):
    #number_char = str(input("Please enter the minimum number of numbers required. "))
    number_check = True
    min_char = int(min_char)
    max_char = int(max_char)
    if number_char.isdigit():
        number_check = True
        #return number_check
    else:
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("ERROR: Please enter a number character requirement with a value of at least 0, no floats or strings.")
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        number_check = False
        return number_check

    number_char = int(number_char)
    if number_char > max_char:
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("ERROR: Minimum number of number characters is greater than the maximum number of characters initially input.")
        print("Please enter the minimum number of number characters again (with a value less than the maximum character amount.)")
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        number_check = False
        return number_check

    uppercase_char = int(uppercase_char)
    special_char = int(special_char)
    extra_conditions = uppercase_char + special_char + number_char
    if extra_conditions > max_char:
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("ERROR: The sum of the character requirements for uppercase, special, and number characters is greater than the maximum character amount.")
        print(f"Uppercase characters: {uppercase_char}")
        print(f"Special characters: {special_char}")
        print(f"Number characters: {number_char}")
        print(f"Sum: {extra_conditions} > Maximum characters: {max_char}")
        print("Please enter an uppercase, special, or number character amount that will not lead to the sum of uppercase, special, and number characters to be greater than the maximum character amount.")
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        number_check = False
        return number_check
    else:
        #print(number_check)
        return number_check

#min_char = 3
#max_char = 16
#uppercase_char = 5
#special_char = 3
#test_run = number_check(min_char, max_char, uppercase_char, special_char)


def checks():
    overall_check = True
    min_check_result = min_check(min_char)
    if min_check_result == False:
        overall_check = False
        return overall_check
    
    max_check_result = max_check(min_char, max_char)
    if max_check_result == False:
        overall_check = False
        return overall_check
    
    uppercase_check_result = uppercase_check(min_char, max_char, uppercase_char)
    if uppercase_check_result == False:
        overall_check = False
        return overall_check

    special_check_result = special_check(min_char, max_char, uppercase_char, special_char)
    if special_check_result == False:
        overall_check = False
        return overall_check

    number_check_result = number_check(min_char, max_char, uppercase_char, special_char, number_char)
    if number_check_result == False:
        overall_check = False
        return overall_check

    if overall_check == True:
        print("All checks passed!")
        return overall_check

#test_run = checks()


def password_generator(min_char, max_char, uppercase_char, special_char, number_char):
    min_char = int(min_char)
    max_char = int(max_char)
    uppercase_char = int(uppercase_char)
    special_char = int(special_char)
    number_char = int(number_char)

    alphabet_characters = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = list(alphabet_characters)
    uppercase_characters = alphabet_characters.upper() #uppercase characters
    uppercase_list = list(uppercase_characters)
    special_characters = '~`!@#$%^&*()-=_+[]\|;:<,>.?/'
    special_list = list(special_characters)
    number_characters = '1234567890'
    number_list = list(number_characters)
    
    password_check = True
    #testing password conditions
    test_conditions = checks()
    if test_conditions == False:
        password_check = False
        return password_check

    #actual password generation
    lowercase_alphabet_iteration = 0
    uppercase_alphabet_iteration = 0
    special_iteration = 0
    number_iteration = 0

    choice_list = [1, 2, 3, 4]
    #1: lowercase alphabet character
    #2: uppercase alphabet character
    #3: special character
    #4: number character
    choice = 0
    index = 0
    chosen_character = ''
    password_list = []
    total_iteration = max_char
    if total_iteration == 0:
        print("NOTE: No max character count detected. Generating max character count between 1 and 99...")
        total_iteration = random.randint(1, 99)
        print(f"Generated max character count of {total_iteration}, generating password based on this...")
    current_iteration = 0
    print("Generating password...")
    while current_iteration < total_iteration:
        chosen_character = ''
        index = 0
        choice = 0
        if uppercase_alphabet_iteration < uppercase_char:
            choice = 2
        elif special_iteration < special_char:
            choice = 3
        elif number_iteration < number_char:
            choice = 4
        else:
            choice = random.randint(1, 4) #selects a choice from choice_list

        if choice == 1:
            #print("Lowercase alphabet character")
            index = random.randint(0, len(alphabet_list) - 1)
            #print(index)
            chosen_character = alphabet_list[index]
            password_list.append(chosen_character)
            lowercase_alphabet_iteration += 1
        elif choice == 2:
            #print("Uppercase alphabet character")
            index = random.randint(0, len(uppercase_list) - 1)
            #print(index)
            chosen_character = uppercase_list[index]
            password_list.append(chosen_character)
            uppercase_alphabet_iteration += 1
        elif choice == 3:
            #print("Special character")
            index = random.randint(0, len(special_list) - 1)
            #print(index)
            chosen_character = special_list[index]
            password_list.append(chosen_character)
            special_iteration += 1
        elif choice == 4:
            #print("Number character")
            index = random.randint(0, len(number_list) - 1)
            #print(index)
            chosen_character = number_list[index]
            password_list.append(chosen_character)
            number_iteration += 1
        current_iteration += 1

    random.shuffle(password_list)
    password = ''.join(password_list)
    return password


while True:
    min_char = str(input("Please enter the minimum number of characters required for the password. "))
    max_char = str(input("Please enter the maximum number of characters required for the password. "))
    uppercase_char = str(input("Please enter the minimum number of uppercase characters required. "))
    special_char = str(input("Please enter the minimum number of special characters required. "))
    number_char = str(input("Please enter the minimum number of number characters required. "))
    
    print("Would you like to generate a password at max character length?")
    print("NOTE: If you enter 'no', the generator can still generate a random password at max character length. Entering 'no' means you have no preference.")
    print("It is recommended to enter 'yes' because it would be more secure than a password less than the max character length.")
    most_secure = True
    yes_list = ['y', 'yes']
    no_list = ['n', 'no']
    yes_or_no = ''
    while True:
        yes_or_no = str(input("Please enter 'yes' or 'no'. "))
        yes_or_no = yes_or_no.lower()
        if yes_or_no in yes_list:
            most_secure = True
            break
        elif yes_or_no in no_list:
            most_secure = False
            break
        else:
            print("ERROR: Input not recognized. Please enter a valid response ('yes' or 'no').")

    random_password_length = 0
    if most_secure == False:
        uppercase_char = int(uppercase_char)
        special_char = int(special_char)
        number_char = int(number_char)
        min_char = int(min_char)
        max_char = int(max_char)
        sum_char = uppercase_char + special_char + number_char
        
        if sum_char <= max_char:
            if sum_char >= min_char:
                random_password_length = random.randint(sum_char, max_char)
                #print(random_password_length)
                max_char = random_password_length
        
                uppercase_char = str(uppercase_char)
                special_char = str(special_char)
                number_char = str(number_char)
                min_char = str(min_char)
                max_char = str(max_char)
            else:
                uppercase_char = str(uppercase_char)
                special_char = str(special_char)
                number_char = str(number_char)
                min_char = str(min_char)
                max_char = str(max_char)
        else:
            uppercase_char = str(uppercase_char)
            special_char = str(special_char)
            number_char = str(number_char)
            min_char = str(min_char)
            max_char = str(max_char)

    generated_password = password_generator(min_char, max_char, uppercase_char, special_char, number_char)
    if generated_password == False:
        continue
    else:
        password_check = True
        print("Password generated! Now writing to file...")
        #break
        if password_check == True:
            current_time_num = time.time()
            current_time = time.ctime(current_time_num)
            with open('generated_password_history.txt', 'a') as f:
                f.write(current_time)
                f.write('\n')
                f.write('Generated Password: ')
                f.write(generated_password)
                f.write('\n')
                f.write('~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-')
                f.write('\n')
            print("Password written to file!")
            print('~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-')

            end = True
            print("Would you like to generate another password?")
            while True:
                continue_generation = str(input("Please enter 'yes' or 'no'. "))
                continue_generation = continue_generation.lower()
                if continue_generation in yes_list:
                    print('~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-')
                    end = False
                    break
                elif continue_generation in no_list:
                    print("Program exiting...")
                    print("Goodbye!")
                    print('~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-')
                    end = True
                    break
                else:
                    print("ERROR: Input not recognized. Please enter a valid response ('yes' or 'no').")
            if end == True:
                break
            else:
                continue
