#Problem **1: Print the following pattern**
#Write a program to print the following number pattern using a loop.
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
# Solution:-

n = 5  

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()



'''
### Problem **2: Display numbers from a list using loop**

Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the next number
- If the number is greater than 500, then stop the loop
'''

#Solution

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)




'''
Problem **3: Append new string in the middle of a given string**

Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

Input:-
s1 = "Ault"
s2 = "Kelly"

Output:-
AuKellylt

'''


def appendMiddle(s1,s2):
    middle = len(s1)//2
    s3=s1[:middle]+s2+s1[:middle]
    print(s3)




'''
### Problem **4: Arrange string characters such that lowercase letters should come first**

Given string contains a combination of the lower and upper case letters. Write a program to arrange 
the characters of a string so that all lowercase letters should come first.

Input:-
str1 = PyNaTive

Output:-
yaivePNT
'''

def arrangeLowerFirst(s):
    lowerChars = [char for char in s if char.islower()]
    upperChars = [char for char in s if char.isupper()]
    ans = "".join(lowerChars + upperChars)
    print(ans)









