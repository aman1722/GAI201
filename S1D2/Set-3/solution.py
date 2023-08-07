##1
data = [("John", 25), ("Jane", 30)]
output = [f"{name} is {age} years old." for name, age in data]
output = " ".join(output)
print(output)

##2




##3
def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)


##4
input_string = "madam"
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]
if is_palindrome(input_string):
    print(f"The word {input_string} is a palindrome.")
else:
    print(f"The word {input_string} is not a palindrome.")

##5
# from queue import Queue
# class StackUsingQueue:
#     def _init_(self):
#         self.queue1 = Queue()
#         self.queue2 = Queue()
#     def push(self, value):
#         self.queue1.put(value)
#     def pop(self):
#         if self.queue1.empty():
#             return None
#         while self.queue1.qsize() > 1:
#             self.queue2.put(self.queue1.get())
#         popped_value = self.queue1.get()
#         self.queue1, self.queue2 = self.queue2, self.queue1  # Swap the queues
#         return popped_value
# stack = StackUsingQueue()
# stack.push(1)
# stack.push(2)
# print(stack.pop())
# stack.push(3)
# print(stack.pop())
# print(stack.pop())



##6
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
##7
arr = [64, 25, 12, 22, 11]
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
selection_sort(arr)
print(arr)

