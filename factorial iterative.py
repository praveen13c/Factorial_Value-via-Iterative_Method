# Factorial value via Iterative Method
# it will explain how factorial value is calculate ,step by step
# Code = Praveen Singh Chauhan

# Program Starts

def factorial_iterative(n):
    """
    :param n: take input from user and it will be an integer
    :return: n * n-1 * n-2 * n-3 * n-4 ....1
    how it will calculate
        print(f"fac = {fac} and i+1 = {i+1} ")  # how it will calculate the value which is 120
        fac = fac * (i+1) # it will calculate value from 1 to given value in 'n'
        print(f"now 'fac' is {fac}") # it will show calculated fac value
    """
    fac_iter = 1
    for i in range(n):
        # how it will calculate the value which is 120
        print(f"now i is {i} and + 1 = {i+1}")
        print(f"fac_iter x (i+1) <variables | value > {fac_iter} x {i+1} =  ")
        fac_iter = fac_iter * (i+1)  # it will calculate value from 1 to given value in 'n'
        print(f"After Calculation new'fac_iter' is {fac_iter} \n")  # it will show calculated fac value
    return fac_iter  # it will


while True:

    number = input("Give a number for Factorial via Iterative method  [ 13 = exit ] > ")

    if number == str(number) or number == None:
        try:
            number == int(number)
        except Exception as err_num:
            print(f"Please enter a Numeric value only. Error -[ {err_num} ] \n")
            continue

    if int(number) == 13:
        print("*" * 40)
        print("          Exit            ")
        print("*" * 40)
        break

    number = int(number)
    print(f"factorial using iterative method  and value is = {factorial_iterative(number)}")
    print("*" * 60, '\n')
# Program Ends
