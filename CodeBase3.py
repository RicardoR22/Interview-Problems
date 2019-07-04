"""
Given an list containing 9 numbers ranging from 1 to 10, write a function to find the missing number.
Assume you have 9 numbers between 1 to 10 and only one number is missing.

"""

def find_missing_number(list_numbers):
    curr_num = 1

    for num in list_numbers:
        if num != curr_num:
            return curr_num
        else:
            curr_num += 1
