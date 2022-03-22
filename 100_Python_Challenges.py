# Udemy course: 100 Python Challenges 
# https://www.udemy.com/course/100-python-challenges/learn/lecture/25954126?start=0#overview
from random import randrange
from random import randint
import math
import datetime

### update on daily basis until the challenges are completed ###

# 25. remove duplicate elements from a string
# example: inout_string = 'How are you?', expected_out = How areyu?
def remove_duplicates (input_string):
    output_string = ''
    for x in input_string:
        if x not in output_string:
            output_string = output_string + x
    print(output_string)
    return output_string

# 24. count the number of vowels in a given string
def count_vowels (input_string):
    v = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    count = 0
    for x in input_string:
        if x in v:
            count += 1
    print(count)
    return count

# 23. swap two variables without using a third variable

def swap_strings(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    s1 = s1 + s2
    s2 = s1
    s1 = s1.replace(s1[0:len1], '')
    s2 = s2.replace(s2[len2::], '')
    print(s1, s2)
    return s1, s2

# 22. reverse a string. accepts 2 strings. concatenate the 2 strings
# by inserting a space in between the strings and then reverse the resultant string
# return new_string
def string_reverse(first_name, last_name):

    result = (first_name + ' ' + last_name)[::-1]
    print(result)
    return result

# 21. Fibonacci: randomly choose any number, n, from 5 t0 10 inclusive and
# generates a Fibonacci sequence until n. return in form of a list, return (n, output-sequence)
def Fibonacci():
    output_sequence = list()
    f = 0  # the first int
    s = 1  # the second int
    x = 0  # for looping
    result = 0
    n = random.randint(5, 10)
    while x < n:
        output_sequence.append(f)
        result = f + s
        f = s
        s = result
        x += 1

    print(n, output_sequence)
    return n, output_sequence

# 20. accepts an int and converts it into binary form. then swap the twp bits at
# position 3 and 7 from left in the binary number and return the int result
def swap_bits(num):
    bin_num = f'{num:08b}'
    s3 = bin_num[2]
    s7 = bin_num[6]
    # print(bin_num[0:3])
    # 00101000 to 00001010
    bin_result = bin_num[0:2] + s7 + bin_num[3:6] + s3 + bin_num[-1]
    # print (bin_result)
    int_result = int(bin_result, 2)
    # print(int_result)
    return int_result

# 19. generate a list containing 10 random numbers between 0 and 100, inclusive
# then return a list of numbers divisible by 15; return input_list, output_list
def divide_by_15():
    input_list = [random.randrange(0, 100) for i in range(10)]
    output_list = []
    for x in input_list:
        if x % 15 == 0:
            output_list.append(x)
    # print(input_list, output_list)
    return input_list, output_list

# 18. randomly choose any number from 100 to 300, inclusive
# and calculate the sum of the digits in the number
# return n, total
def sum_digits():
    num = random.randint(100, 300)
    str_num = str(num)
    total = 0
    for x in range(0, len(str_num)):
        total += int(str_num[x])
    print(num, total)
    return num, total

# 17. accept a non-negative integer and returns True if it is a prime number
# returns False if it's not a prime number
def prime_num (num):
    result = []
    for x in range(1, num + 1):
        if num % x == 0:
            result.append(x)
    if sum(result) - 1 - num == 0:
        # print('True')
        return True
    else:
        # print('False')
        return False

# 16. check if a function returns a whole number w/ decimals after dividing
def check_division(num):
    if num - int(num) == 0:
        # print('T')
        return num, True
    else:
        # print('F')
        return num, False

# 15. randomly choose any number from 1 to 10, incluvsive
# then calculate the factorial of the number. return (num, factorial)

def factorial():
    num = random.randint(1,10)
    result = 1
    for x in range(1, num + 1):
        # print (x)
        result *= x
    # print(num, result)
    return num, result

# 14. accepts three bool variables, x, y and z. return True if at least 2
# of three variables are True. return (x, y, z, True/False)
# note to myself: should be able to simplify the code
def booleans(x, y, z):
    if x == y == z == True:
        return True
    elif x == y == True and z == False:
        return True
    elif x == z == True and y == False:
        return True
    elif x == False and x == y == True:
        return True
    elif x == y == False and z == False:
        return False
    elif y == z == False and x == True:
        return False
    elif z == x == False and y == True:
        return False
    elif x == y == z == False:
        return False

# 13. choose a random number from 1 and 5000, inclusive
# calculate the length of the number (do not use len() function)
# return (n, count)
def calculate_length():
    # num = randrange(5000)  # works
    num = random.randint(1, 5000)   # also works
    str_num = str(num)
    count = 0
    for x in (str_num):
        count += 1

    # print(num, count)
    return (num, count)

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
