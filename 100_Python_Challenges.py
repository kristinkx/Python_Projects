# Udemy course: 100 Python Challenges 
# https://www.udemy.com/course/100-python-challenges/learn/lecture/25954126?start=0#overview

# update on daily basis until the challenges are completed

# 12. return the next number greate than the 2 numbers a and b, and divisible by b
def check_division(a, b):
    if a % b == 0:
        # print(a + b)
        return a + b
    else:
        # print((a + b) - (a % b))
        return (a + b) - (a % b)
    
# 11. write a function accepts two inputs, yr (year) and mon (month) and
# return True if this yr/mon has Friday 13th, False otherwise
# note: return type: return date(yr, mon, day), T/F
def check_friday(yr, mon):
    friday = datetime(yr, mon, 13)
    if friday.strftime("%A") == "Friday":
        return datetime(yr, mon, 13), True
    else:
        return datetime(yr, mon, 13), False
    
# 10. check if a number is equal to the num of its positive divisors, except itself
def sum_pos_divisor(num):
    dividers = []
    for x in range(1, num + 1):
        if num % x == 0:
            dividers.append(x)
    if sum(dividers) - num == num :
        # print('True')
        return True
    else:
        # print ('False')
        return False
      
 # 9. calculate the number of numerical digits in a string
# example: input_string = 'gkoi6544', output = 4
def count_count_digits(input_string):
    counter = 0
    for x in input_string:
        if x.isnumeric():
            counter += 1
    # print(counter)
    return counter
  
# 8. if a number is multiple of 3, return 'fizz', if a number is a multiple of 5,
# return 'Buzz', if the number is a multiple of both 3 and 5, return 'FizzBuzz'
# if a number of not a multiple of either 3 or 5, return the num itself
def fizzbuzz (num):
    if num % 3 == 0 and num % 5 !=0:
        print('Fizz')
        return ('Fizz')
    elif num % 3  == 0 and num % 5 == 0:
        print ('FizzBuzz')
        return ('FizzBuzz')
    elif num % 3 !=0 and num % 5 == 0:
        print('Buzz')
        return ('Buzz')
    elif num % 3 != 0 and num % 5 != 0:
        print (num)
        return num

# 7. return the decimal part of a number
# if decimal part is zero, then return the string 'INTEGER'

def decimal_part (num):
    expected_out = 0
    if (num * 10) % 10 == 0:
        print ('INTEGER')
        return ('INTEGER')
    else:
        expected_out = round(num - int(num), 2)
        print(expected_out)
        return expected_out
        # return round(num - int(num), 2)
        
# 6. find power of any number x ^ y

def power (x, y):
    # print (x ** y)
    return x ** y
  
# 5. determine factors of a number; return the output in the form of a list

def factors(num):
    output_list = []
    for x in range(1, num + 1):
        if num % x == 0:
            output_list.append(x)
    # print(output_list)
    return output_list
  
# 4. check if a given number is odd or even
def even_odd(num):
    if num % 2 == 0:
        return ('Even')
    else:
        return ('Odd')
      
# 3. divide num1 by num2 and return the quotient and remainder.
# output rounded to 2 decimal places

def quot_rem(num1, num2):
    
    if num1 != 0 and num2 != 0:
        r = round(num1 % num2, 2)
        q = num1 / num2
    # print("remainder:", r)
    # print("quotient:", q)
    return q, r
  
# 2. return a square root of an input number, rounded to 3 decimal places

def sqrt (num):
    if num <=0:
        return 0
    # print(round(math.sqrt(num),3))
    return round(math.sqrt(num),3)
  
  
# 1. calculate the sum of 3 given numbers
# if the values are equal then return 2 times of their sum

import math
def sum_num (a,b,c):
    if a == b == c:
        print(2 * (a + b + c))
        return 2 * (a + b + c)
    else:
        print(a + b + c)
        return a + b + c
