# #Problem 1: Print the following pattern
# #Write a program to print the following number pattern using a loop.
# # '''
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5
# # '''
# # # Solution:-

n = 5  

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#Solution


# ##2
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)


##3
def append_middle(s1, s2):
    middle = len(s1) // 2  # Calculate the middle index
    s3 = s1[:middle] + s2 + s1[middle:]  # Combine the strings
    return s3

s1 = "Ault"
s2 = "Kelly"
res = append_middle(s1, s2)
print(res)

#4
def arrange_lower_first(s):
    lower_chars = [char for char in s if char.islower()]
    upper_chars = [char for char in s if char.isupper()]
    arranged_str = ''.join(lower_chars + upper_chars)
    return arranged_str

str1 = "ChAnDaN"
result = arrange_lower_first(str1)
print(result)

##5
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

def addlist(list1, list2):
    newlist = []
    minlen = min(len(list1), len(list2))
    for i in range(minlen):
        newlist.append(list1[i] + list2[i])
    
    if len(list1) > minlen:
        newlist.extend(list1[minlen:])
    elif len(list2) > minlen:
        newlist.extend(list2[minlen:])
    
    return newlist

res = addlist(list1, list2)
print(res)

##6
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

def addlist(list1, list2):
    new_list = [item1 + item2 for item1 in list1 for item2 in list2]
    return new_list

res = addlist(list1, list2)
print(res)

##7
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
def reverse(list1, list):
    for item1, item2 in zip(list1,reversed(list2)):
        print(item1 , item2)
reverse(list1,list2)

##8
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

add = {employee: defaults.copy() for employee in employees}
print(add)

##9
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]

new_dict = {key: sample_dict[key] for key in keys}
print(new_dict)

##10
tuple1 = (11, [22, 33], 44, 55)
tuple_list = list(tuple1)
tuple_list[1][0] = 222
modified_tuple = tuple(tuple_list)
print(modified_tuple)