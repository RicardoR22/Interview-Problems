def factorial_recursive(num):
    if num == 2:
        return num

    return num * factorial_recursive(num - 1)



print(factorial_recursive(5))
