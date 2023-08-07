##1
def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

word1 = "cinema"
word2 = "iceman"
result = are_anagrams(word1, word2)
print(result)

##2
arr = [64, 34, 25, 12, 22, 11, 90]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
bubble_sort(arr)
print(arr)

##3
strs = ["flower", "flow", "flight"]
def longest(strs):
    if not strs:
        return ""
    min_str = min(strs, key=len)
    for i, char in enumerate(min_str):
        for string in strs:
            if string[i] != char:
                return min_str[:i]
    
    return min_str
result = longest(strs)
print(result)

##4
input_string = "abc"
def string_permutations(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]
    permutations = []
    for i, char in enumerate(s):
        remaining_chars = s[:i] + s[i+1:]
        for perm in string_permutations(remaining_chars):
            permutations.append(char + perm)
    return permutations
permutations = string_permutations(input_string)
print(permutations)