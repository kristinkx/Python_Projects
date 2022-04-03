# The practice program is modified based on https://hackr.io/blog/python-projects - 'Calculator'
# A simple calculator with functions of addition, subtraction, multiplication, division,
# modular, log, exponent, sin and avg

import math

# WIP: having challenges to call this function to check if the input is a number
################################################################################


def check_number(inp):
    while True:
        try:
            if isinstance(inp, float) == True:
                break
        except ValueError:
            print("This input is invalid.")

################################################################################


def addition ():

    result = 0
    # tracks non-zero input
    total = 0

    print("Addition Operation: you can enter multiple numbers")
    inp = float(input("Enter a number: "))

    # total input number
    total = 0
    result = 0

    while inp != 0:
        result = result + inp
        total += 1
        inp = float(input("Enter another number (enter 0 to calculate the sum): "))
    return [result, total]


def subtraction ():
    result = 0

    print("Subtraction Operation: you can enter multiple numbers")
    inp = float(input("Enter a number: "))
    result = 0

    while inp != 0:
        result = result - inp
        inp = float(input("Enter another number or enter 0 to calculate: "))

    return result


def multiplication():
    print("Multiplication Operation: you can enter multiple numbers")
    inp = float(input("Enter a number: "))
    result = 1

    if inp == 0:
        result = 0
    while inp != 0:
        result = result * inp
        inp = float(input("Enter another number or enter 0 to calculate): "))
    return result


def division ():
    result = 0
    print("Division Operation: take 2 inputs")
    inp_n = float(input("Enter the first number (numerator): "))

    if inp_n == 0:
        result = 0
    else:
        inp_d = float(input("Enter the second number (denominator): "))
        if inp_d == 0:
            print("error! divided by 0")
        else:
            result = round(inp_n/inp_d, 2)
            print(result)
    return result


def average():
    # call addition function first; then access the total and total number of inputs
    add = addition()
    total = add[0]
    number = add[1]
    result = round(total/number, 2)
    return result


def modular():
    print("Modular arithmetic: take 2 inputs")

    inp1 = int(input("Enter the first number: "))
    inp2 = int(input('Enter the second number: '))

    if inp1 == 0:
        result = inp2
    else:
        result = inp1 % inp2

    return result


def exponent():
    print("Exponent function: take 2 inputs")

    inp1 = int(input("Enter the first number: "))
    inp2 = int(input('Enter the second number: '))

    if inp1 == 0:
        result = 0
    else:
        result = inp1 ** inp2

    return result


def log():
    print("Log function: take 2 inputs ")

    inp_a = int(input("Enter the first number: "))
    inp_base = int(input('Enter the second number (base): '))

    result = math.log(inp_a, inp_base)
    return result


def sin():
    inp_array = []
    out_array = []
    count = 0
    print("Sin function: take multiple inputs ")
    total = int(input('How many inputs are you providing? '))

    if total <= 0:
        print('Goodbye')
    else:
        for x in range(total):
            inp = float(input('Enter a value: '))
            inp_array.append(inp)
            count += 1

        for x in range(len(inp_array)):
            out_array.append(math.sin(inp_array[x]))

    return out_array


# call the functions and print the results
while True:

    print("Enter 'a' for addition; 's' for subtraction; 'm' for multiplication; "
          "'d' for division; 'v' for average: ")
    print("Or enter 'x' for exponent; 'u' for modular;  'n' for sin; "
          "'g' for log or enter 'q' to quit the program: ")

    key = input(" ")

    if key.lower() == 'q':
        break

    elif key.lower() != 'q':
        if key.lower() == 'a':
            sum_res = addition()
            print("Sum = ", sum_res[0])

        elif key.lower() == 's':
            sub_res = subtraction()
            print("Delta = ", sub_res)

        elif key.lower() == 'm':
            mul_res = multiplication()
            print("Product = ", mul_res)

        elif key.lower() == 'd':
            div_res = division()
            print("Division = ", div_res)

        elif key.lower() == 'u':
            mod_res = modular()
            print("Modular arithmetic result = ", mod_res)

        elif key.lower() == 'x':
            exp_res = exponent()
            print("Exponent = ", exp_res)

        elif key.lower() == 'v':
            avg_res = average()
            print("Average = ", avg_res)

        elif key.lower() == 'g':
            log_res = log()
            print("Log result = ", log_res)

        elif key.lower() == 'n':
            sin_res = sin()
            print('Sin result = ', sin_res)

    else:
        print("Invalid input!")
        break
