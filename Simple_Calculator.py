# The program is modified based on https://hackr.io/blog/python-projects - 'Calculator'
# A simple calculator with functions of addition, subtraction, multiplication, division, modular,
# log, exponent and avg

import math

def addition ():
    print("Addition")
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
    print("Subtraction")
    inp = float(input("Enter a number: "))
    total = 0
    result = 0
    while inp != 0:
        result = result - inp
        total += 1
        inp = float(input("Enter another number (0 to calculate): "))
    return [result, total]

def modular ():
    print("Modular: You need to 2 numbers below")
    inp1 = int(input("Enter the first number: "))

    inp2 = int(input('Enter the second number: '))

    if inp1 == 0:
        result = inp2
    else:
        result = inp1 % inp2
        print(result)

    return [result, 2]


def exponent ():
    print("Exponent: You need to 2 numbers below")
    inp1 = int(input("Enter the first number: "))
    inp2 = int(input('Enter the second number: '))

    if inp1 == 0:
        result = 0
    else:
        result = inp1 ** inp2
        print(result)

    return [result, 2]

def multiplication ():
    print("Multiplication")
    inp = float(input("Enter a number: "))
    total = 0
    result = 1
    if inp == 0:
        result = 0
    while inp != 0:
        result = result * inp
        total += 1
        inp = float(input("Enter another number (enter 0 to calculate): "))
    return [result, total]

def divisiion ():
    result = 0
    print("Division: you need to enter 2 numbers below")
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
    return [result, 2]

def average():
    add = addition()
    sum1 = add[0]
    tt = add[1]
    result = round(sum1/tt,2)
    return [result, tt]

def log():
    print("Log function: you need to enter 2 numbers below ")
    inp_a = int(input("Enter the first number (a): "))
    inp_base = int(input('Enter the second number (base): '))
    result = math.log(inp_a, inp_base)
    print (result)
    return [result, 2]


while True:
    lst = []

    print("Enter 'a' for addition; 's' for subtraction; 'm for multiplication; 'd' for division; 'x' for exponent;"
          " 'u' for modular; 'v' for average; 'g' for log or enter 'q' to quit the program: ")

    key = input(" ")
    if key != 'q':
        if key == 'a':
            lst = addition()
            print("Result = ", lst[0], " total inputs ", lst[1])

        elif key == 's':
            lst = subtraction()
            print("Result = ", lst[0], " total inputs ", lst[1])

        elif key == 'm' :
            lst = multiplication()
            print("Result = ", lst[0], " total inputs", lst[1])

        elif key == 'd':
            lst = divisiion()
            print('Result = ', lst[0], 'total inputs ', lst[1])

        elif key == 'u':
            lst = modular()
            print("Result = ", lst[0], " total inputs ", lst[1])

        elif key == 'x':
            lst = exponent()
            print("Result = ", lst[0], "with total 2 inputs")

        elif key == 'v':
            lst = average()
            print("Result  = ", lst[0], " total inputs ", lst[1])

        elif key == 'g':
            lst = log()
            print("Result = ", lst[0], "with total 2 inputs")

        else:
            print("invalid input")
