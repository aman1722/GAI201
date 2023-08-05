'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello World')



#2

# Integer
integer_var = 10

# Float
float_var = 3.14

# String
string_var = "Hello, world!"

# Boolean
boolean_var = True

# List
list_var = [1, 2, 3, 4, 5]

# Tuple
tuple_var = (5, 10, 15)

# Dictionary
dict_var = {'a': 1, 'b': 2, 'c': 3}

# Set
set_var = {2, 4, 6, 8, 10}

# Printing types and values
print(f"Type of integer_var: {type(integer_var)}, value: {integer_var}")
print(f"Type of float_var: {type(float_var)}, value: {float_var}")
print(f"Type of string_var: {type(string_var)}, value: {string_var}")
print(f"Type of boolean_var: {type(boolean_var)}, value: {boolean_var}")
print(f"Type of list_var: {type(list_var)}, value: {list_var}")
print(f"Type of tuple_var: {type(tuple_var)}, value: {tuple_var}")
print(f"Type of dict_var: {type(dict_var)}, value: {dict_var}")
print(f"Type of set_var: {type(set_var)}, value: {set_var}")




#3
number=list(range(1,11))
number.append(20)
number.remove(2)
number.sort()

print(number)




#4

number=[10,20,30,40,50,60]

sumnumber=sum(number);
avg=sumnumber/len(number)

print(avg)




#5
input_string="Python";

def reverse_string(input_string):
    reversed_sting=input_string[::-1]
    return reversed_sting
    
output=reverse_string(input_string)
print(output)






#6
def count_vowels(input_string):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    
    for char in input_string:
        if char in vowels:
            vowel_count += 1
            
    return vowel_count
    
input_string = "Hello"
vowel_count = count_vowels(input_string)
print(vowel_count)




#7
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    
    return True
input_number = 13
if is_prime(input_number):
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")







#8

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

input_number = 5
factorial_result = factorial(input_number)
print(f"Factorial of {input_number} is {factorial_result}.")






#9

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

input_n = 5
fibonacci_sequence = fibonacci(input_n)
print(f"Fibonacci sequence: {fibonacci_sequence}")




#10

squares_list = [x**2 for x in range(1, 11)]
print(squares_list)

