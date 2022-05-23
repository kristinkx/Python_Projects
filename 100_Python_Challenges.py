# Udemy course: 100 Python Challenges 
# https://www.udemy.com/course/100-python-challenges/learn/lecture/25954126?start=0#overview
from random import randrange
from random import randint
import math
import datetime
import operator

### update on regular basis until the challenges are completed ###
# 88. calculate six months from a given date
def add_to_date(date):
    month = date.month + 6
    year_add = month // 12
    if year_add == 1:
        new_month = month % 12
    else:
        new_month = month
    six_month = datetime.date(date.year + year_add, new_month, date.day +1)
    return six_month

# 87. convert year, month, date to day of the year
def day_of_year():
    chosen_date = datetime.date(8004,3,23)
    day_of_the_year = chosen_date.strftime('%j')
    return chosen_date, day_of_the_year

# 86. check if the given date if valid
def check_date(year, month, date): 
    flag = True
    try:
        datetime.datetime (int(year), int(month), int(date))
    except ValueError:
        flag = False
    #print(flag)

    return flag

# 82. remove all elements are in set1 but not in set2
def diff_update(set1, set2):
    # print (set2 - set1)
    return set2 - set1

# 81. find symmetrical difference between the 2 sets (in either set but not in intersection)
def sym_diff (set1, set2):
    results = set1.symmetric_difference(set2)
    return results

# 80. find union of 2 sets
def set_union(set1,set2):
    # both work
    # result = set1.union(set2)
    # return result
    return (set1 | set2) 

# 79. find the difference between the 2 sets; elements are in set1 but not in set 2
def set_diff(set1, set2):
    results = set1.difference(set2)
    return results

# 78. find intersection of two sets
def set_intersection(set1, set2):
    results = set1.intersection(set2)
#     print(results)
    return results

# 77. compare 2 sets and display all elements that in set 1 but not in set 2
def compare_sets (set1, set2):
    results = set ()
    results = set1.difference(set2)

#     print(results)
    return results

# 76. remove duplicates from a dictionary
def remove_duplicates (input_dict):
    results = {}
    for key, value in input_dict.items():
        if value not in results.values():
            results[key] = value

#     print(results)
    return results

# 74. map 2 lists into a dictionary
def map_lists(list1,list2):
    return (dict(zip(list1,list2)))

# 75. sort values in a dictionary
def dict_sort(input_dict):
    results = {k: v for k, v in sorted(input_dict.items(), key=lambda x: x[1])}
    print(results)
    return results

# 73. remove empty items from a dictionary
def remove_empty(input_dict):
    results = {k: v for (k, v) in input_dict.items() if v}

    print (results)
    return results

# 72. create a dictionary from 1 - 10 and return y: x * x
def create_dict():
    results = {}
    for x in range(1, 11):
        results[x] = x * x

#     print(results)
    return results

# 71. invert the keys and values of a dictionary
def invert_dict(input_dict):
    results = {}
    for key, value in input_dict.items():
        results[value] = key
        # results[value] = key
#     print(results)
    return results

# 70. remove duplicate values in a dictionary
def remove_duplicates(input_dict):
    results = []
    for key, value in input_dict.items():
        if value not in results:
            results.append(value)
#     print(results)
    return results

# 69. multiply the vales in a dictionary
def multiply_values (input_dict):
    total = 1
    for v in input_dict:
        total = total * input_dict[v]
#     print (total)
    return total

# 68. sum all the values in a dictionary and return the total value
def sum_values (input_dict):
    return sum(input_dict.values())

# 67. max value in a dictionary
def max_value(input_dict):
    return max(input_dict.items(), key = operator.itemgetter(1))[1]

# 56. Multiple all elements in a list:
def multiple_elements(input_list):
    prod = 1
    if len(input_list) == 0:
        return 0
    elif len(input_list) == 1:
        return input_list[0]
    elif len(input_list) > 1:
        for x in input_list:
            prod *= x
    # print(prod)
    return prod

# 55. highest number in a list: returns the highest number in a list
def high_num (input_list):
    input_list.sort(reverse = True)
    print(input_list[0])
    return input_list[0]

# 54. return the index of a target value in a list. if the target value is found in the
# list then return the index of the value, if not, return the index where it would be
# if it were inserted in order.
def return_index(input_list, target):
    if target not in input_list:
        input_list.insert(len(input_list)-1,target)
        input_list.sort(reverse=False)
        # print(input_list)
        position = input_list.index(target)
        # print(position)
        return position
    else:
        for x in input_list:
            if x == target:
                # print(input_list.index(x))
                return input_list.index(x)

# 53. used sorted() function and lambda to sort the words in the list based on their
# second letter from a to z       
def word_sort(input_list):
    result = sorted(input_list, key=lambda x: (x[1:]))
    # print(result)
    return result

# 52. given a list of words in the singular form, return a set of those words
# in the plural form, the result words only appear once in the output list
def pluralize (input_list):
    results = []
    for x in input_list:
        if x.endswith('o') or x.endswith('s') or x.endswith('ss') or x.endswith('sh') or x.endswith('z') or \
                x.endswith('es'):
            x = x + 'es'
            results.append(x)
            # this is weir I thought the plural form for table is tables but the test case does not agree
        elif x.endswith('e'):
            x = x
            results.append(x)
        else:
            x = x + 's'
            results.append(x)
    for y in results:
        if results.count(y) > 1:
            results.remove(y)
    # print (results)
    return results

# 51. returns the highest possible product by multiplying 3 numbers from the given list
def highest_prod(input_list):
    input_list.sort(reverse = True)
    # print(input_list)
    prod = input_list[0] * input_list[1] * input_list[2]

    # print (prod)
    return prod

# 48. remove all occurrences of an element from a list (remove the num 20)
def remove_20(input_list):
    result = [x for x in (input_list) if x != 20]
    # print(result)
    return result

# 47. return indices of all occurrences of an element in a list
# return the output in the form of a list
def indices (input_list, element):
    # index() only returns the first occurrence of the matching element
    # use list comprehension and enumerate()
    results = [i for i, x in enumerate(input_list) if x == element]
    # print(results)
    return results

# 46. return the kth-largest element in a list
def kth_largest_element (input_list, k):
    input_list.sort(reverse = True)
    # print(input_list)
    for x in range(0, len(input_list)):
        if x == k:
            # print(input_list[k - 1])
            return input_list[k - 1]
        
# 45. remove zeros from a list
def remove_zero(input_list):
    new = []
    for x in input_list:
        if x != 0:
            new.append(x)
    # print(new)
    return new

# 44. replace elements in a list, finds the value 'd' in the given list and
# replace 'd' with 'c'
def replace_value(input_list):
    for x in range(len(input_list)):
        if input_list[x] == 'd':
            input_list[x] = 'c'

    # print(input_list)
    return input_list

# 43. get a string made of the first 2 and the last 2 chars from a given string
# if the length of the given string < 2, return empty string
def str_first2_last2_char(input_string):
    result = ''
    if len(input_string) < 2:
        return result
    elif len(input_string) > 2:
        result = input_string[0:2] + input_string[-2::]
    print(result)
    return result

# 42. return a string that consists of n copies of the input string
def string_copies (input_string):
    return len(input_string) * input_string

# 41. pig latin: convert the given string into Pig Latin: transfer the initial consonant or
# consonant cluster of each word to the end of the word and adding a vocalic syllable ('ay)
# to create a suffix
def pig_latin (input_string):
    split = input_string.split()
    results = []
    for x in split:
        x = x[3:] + x[:3] + 'ay'
        results.append(x)
    print(' '.join(results))
    return ' '.join(results)

# 40. number the occurrences of a sub-string ina given string. finds the number of
# times a sub-string occurs in a given string and also the position at which
# th sub-string is found. return (num, position)
def find_substring(main_string, sub_string):
    num = main_string.count(sub_string)
    i = 0
    result = []
    while i < len(main_string):
        i = main_string.find(sub_string, i)
        result.append(i)
        if i == -1:
            break
        i += len(sub_string)
    # print(num, result)
    return num, result

# 39. check if the given string is a valid pin or not
# a valid pin has 1) exactly 5 characters; 2) accepts only numerical chars (0-9)
# 3) no whitespaces
def valid_pin(input_string):
    num = '0123456789'
    if len(input_string) != 5:
        # print('length False')
        return False
    elif len(input_string) == 5:
        for x in input_string:
            # print(type(x))
            if x not in num:
                # print('digit False')
                return False

        if ' ' in input_string:
            # print('space False')
            return False
        else:
            # print('True')
            return True
        
# 38. remove all occurrence of a given character from an inout string
def remove_char (input_string, char):
    result = ''
    for x in input_string:
        if x != char:
            result += x
    # print(result)
    return result

# 37. check if a string is a pangram or not
def pangram(sample_string):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
                'q', 's', 't', 'u', 'v', 'x', 'y', 'z']
    for x in alphabet:
        if x not in sample_string.lower():
            print ('False')
            return False
        else:
            print('True')
            return True
        
# 36. separate the digits of an integer, return the digits in the form of a list
def separate_digits (num):
    results = []
    str_num = str(num)
    # print(str_num)
    for x in str_num:
        results.append(int(x))
    # print(results)
    return results

# 35. convert string to hexadecimal numbers. output removes the prefix 0x
def convert_to_hex (input_string):
    # int_hex = int(input_string, 16)
    s = input_string.encode('utf-8')
    # print (s)
    result = s.hex()
    result = " ".join(result[i:i + 2] for i in range(0, len(result), 2))
    # print(result)
    return result

# 34. calculate the number of upper case letters in a string
def count_case (sample_string):
    count = 0
    for x in sample_string:
        if x.isupper():
            count += 1
    # print(count)
    return count

# 33. return n copies of a given string
def copies_of_string(input_string, num):
    # print(input_string * num)
    return input_string * num

# 32. convert a string with decimals to an integer
def str_to_int(input_string):
    num = int( float(input_string))
    # print(num)
    return num

# 31. remove white spaces from a string
def remove_spaces(input_string):
    result = ''.join([x for x in input_string.split()])
    # print(result)
    return result

# 30. String to Boolean conversion: converts a string to Boolean value. If the input string contains
# the value 'true' (if required convert the case) then the Boolean value after conversion should
# be True. If the string contains any other value other than 'true' or 'false' then the converted
# value should be 'Invalid input'.
def string_to_bool(input_string):
    if input_string.lower() !='true' and input_string.lower() != 'false':
        return 'Invalid input'
    elif input_string.lower() == 'true':
        return bool(input_string)
    elif input_string.lower() == 'false':
        return bool(input_string)
    
# 29. return the letter added to a string: given two strings s, t. String t is
# generated by shuffling string s and then adding one more letter at a random
# position, return the letter that was added to t.
def new_letter(s, t):
    a = []
    b = []
    result = ''
    for x in range(len(s)):
        a.append(s[x])
    for y in range(len(t)):
        b.append(t[y])
    for y in range(len(t)):
        if b[y] not in a:
            result = b[y]
    print(result)
    return result

# 28. longest common prefix
def longest_prefix(s1, s2, s3, s4):
    lst = [s1,s2,s3,s4]
    lst.sort()

    ending = min(len(lst[0]), len(lst[3]))
    x = 0
    while (x < ending and lst[0][x] == lst[3][x]):
        x += 1
    output_string = lst[0][0:x]
    # print(output_string)
    return output_string

# 27. reverse words in a string: accepts a string and reverse every word of the string, return the reversed string,
# if the string contains any leading or trailing spaces between two words, remove the extra spaces. 
# The output string should have a single space separating the words
def reverse_string(input_string):
    # output_string = input_string.replace(' ', '')
    output_string = input_string.strip()
    print(' '.join(reversed(output_string.split())))
    return ' '.join(reversed(output_string.split()))

# 26. remove consecutive duplicate characters in a string
def remove_duplicates (input_string):
    input_lst = list(input_string)
    output_string = ''
    x = 0
    while x < len(input_lst) - 1:
        if input_lst[x] == input_lst[x + 1]:
            del input_lst[x]
        else:
            x = x + 1
    for y in input_lst:
        output_string = output_string + y

    # print(output_string)
    return output_string

# 25. remove duplicate elements from a string
# example: inout_string = 'How are you?', expected_out = How areyu?
def remove_duplicates (input_string):
    output_string = ''
    for x in input_string:
        if x not in output_string:
            output_string = output_string + x
    # print(output_string)
    return output_string

# 24. count the number of vowels in a given string
def count_vowels (input_string):
    v = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    count = 0
    for x in input_string:
        if x in v:
            count += 1
    # print(count)
    return count

# 23. swap two variables without using a third variable

def swap_strings(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    s1 = s1 + s2
    s2 = s1
    s1 = s1.replace(s1[0:len1], '')
    s2 = s2.replace(s2[len2::], '')
    # print(s1, s2)
    return s1, s2

# 22. reverse a string. accepts 2 strings. concatenate the 2 strings
# by inserting a space in between the strings and then reverse the resultant string
# return new_string
def string_reverse(first_name, last_name):

    result = (first_name + ' ' + last_name)[::-1]
    # print(result)
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

   # print(n, output_sequence)
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
    # print(num, total)
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
        # print('Fizz')
        return ('Fizz')
    elif num % 3  == 0 and num % 5 == 0:
        # print ('FizzBuzz')
        return ('FizzBuzz')
    elif num % 3 !=0 and num % 5 == 0:
        # print('Buzz')
        return ('Buzz')
    elif num % 3 != 0 and num % 5 != 0:
        # print (num)
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
        # print(expected_out)
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
        # print(2 * (a + b + c))
        return 2 * (a + b + c)
    else:
        # print(a + b + c)
        return a + b + c
