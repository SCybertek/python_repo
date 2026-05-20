# Two Sum
# Return indices of two numbers that add up to a target.
# [1,2,3,5 ] target 8 
# output [2,3]
def two_sum(numbers, target):
    existing_nums = {};
    for i, each_num in enumerate(numbers):
        needed_num = target - each_num
        if needed_num in existing_nums:
            return [existing_nums[needed_num], i]
        
        existing_nums[each_num] = i

    return None


print(two_sum([1,2,3,5 ],8 ))

# version 2
def two_sum2(numbers, target):
      existing_nums = {}

      for index in range(len(numbers)):
          number = numbers[index]
          needed_num = target - number

          if needed_num in existing_nums:
              return [existing_nums[needed_num], index]

          existing_nums[number] = index

      return None

print(two_sum([1,2,3,5 ],8 ))

###########################################
# Valid Parentheses
# Use a stack to validate brackets.
def is_valid_parentheses(text):
    stack = []#last in first out data structure 
    parentheses_map = {')': '(', '}': '{', ']': '['}
    
    for char in text:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map.keys():
            if not stack or stack[-1] != parentheses_map[char]:
                return True

#  That means the most recent opening parenthesis is the first one we check when we find a closing parenthesis.

#   parentheses_map = {')': '(', '}': '{', ']': '['}

#   Creates a dictionary that maps each closing symbol to its matching opening symbol.

#   Example:

#   ')' matches '('
#   '}' matches '{'
#   ']' matches '['

#   for char in s:

#   Loops through each character in the string.

#   Example:

#   s = "({})"

#   The loop sees:

#   "("
#   "{"
#   "}"
#   ")"

#   if char in parentheses_map.values():

#   Checks if the current character is an opening parenthesis.

#   The values are:

#   '(', '{', '['

#   So this is true for opening symbols.

#   stack.append(char)

#   Adds the opening symbol to the stack.

#   Example:

#   stack = ["(", "{"]

#   elif char in parentheses_map.keys():

#   Checks if the current character is a closing parenthesis.

#   The keys are:

#   ')', '}', ']'

#   So this is true for closing symbols.

#   if not stack or stack[-1] != parentheses_map[char]:

#   This checks two failure cases.

#   First:

#   not stack

#   Means the stack is empty.

#   Example:

#   s = ")"

#   There is a closing parenthesis, but no opening parenthesis before it.

#   Second:

#   stack[-1] != parentheses_map[char]

#   Means the most recent opening symbol does not match the current closing symbol.

#   Example:

#   s = "(]"

#   When char is ]:

#   parentheses_map[char]

#   means:

#   parentheses_map[']']

#   which gives:

#   '['

#   But:

#   stack[-1]

#   is:

#   '('

#   So they do not match.

#   return False

#   If either failure happens, the string is invalid.

#   stack.pop()

#   If the closing parenthesis matched correctly, remove the last opening parenthesis from the stack.

#   Example:

#   stack = ["(", "["]
#   char = "]"

#   "]" matches "[", so pop removes "[".

#   Now:

#   stack = ["("]

#   return len(stack) == 0

#   After checking the full string, the function returns True only if the stack is empty.

#   If the stack is empty, every opening parenthesis had a matching closing parenthesis.

#   Example:

#   "({[]})"

#   returns:

#   True

#   If the stack is not empty, there were extra opening parentheses.

#   Example:

#   "((("

#   returns:

#   False


# parentheses_map = {')': '(', '}': '{', ']': '['}
# print(parentheses_map.values()) #dict_values(['(', '{', '['])
# print(parentheses_map.keys())#dict_keys([')', '}', ']'])


#Merge two sorted lists
def merge_two_list(lista, listb):
    merged_list = []
    i = 0
    j = 0
    while i < len(lista) and j < len(listb):
        if lista[i] < listb[j]:
            merged_list.append(lista[i]) #Adds one single element to the end of the list.Adds all elements from an iterable to the end of the list.
            i+=1
        else: 
            merged_list.append(listb[j])
            j+=1

    merged_list.extend(lista[i:]) #.Adds all elements from an iterable to the end of the list.
    merged_list.extend(listb[j:])
    return merged_list

print(merge_two_list([1,2,3], [5,6]))

##################################
# Group anagrams
# first let's write a code for anagram stuff 
#Input: arr[] = ["act", "god", "cat", "dog", "tac"]
# Output: [["act", "cat", "tac"], ["god", "dog"]]
# Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.
def group_anagrams(words):
      groups = {}

      for word in words:
          key = "".join(sorted(word.lower())) # sorted(word.lower()) =>   ["a", "c", "t"]
                                                # join converts to a full string

          if key not in groups: #Checks whether this sorted key is already in the dictionary.
              groups[key] = [] #Creates a new empty list for that anagram group.

          groups[key].append(word) #Adds the original word to the correct group.
                                    #groups["act"].append("cat")

      return list(groups.values()) #  Returns only the grouped words, not the dictionary keys.

arr = ["act", "god", "cat", "dog", "tac"]
print(group_anagrams(arr))

############################################
#Find first non-repeating character
#Given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1.
def unique_char(text):
    for index in range(len(text)): # banana
        char = text[index] # b = banana[0]
        if text.count(char) == 1: #counts how many times that same character appears in the whole string.
            return index
    return -1
        
print(unique_char("anabna"))


######################################
# Longest substring without repeating characters - sliding window 
#Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# for indexes ALWAYS use in range 
#  - seen remembers the last index where each character appeared
#   - when we see a repeated character inside the current substring, move start
#   - keep track of the longest valid length seen so far

def longest_substring(text):
      seen = {}
      start = 0
      longest = 0

      for index in range(len(text)): #"abcabcbb"
          char = text[index]# a = text[0]

          if char in seen and seen[char] >= start: # if 'a' in seen and seen['a'] = 0 >=start
              start = seen[char] + 1 # 0 = seen['a'] + 1 = 1

          seen[char] = index # 0 = 0

          current_length = index - start + 1 # 0 = 0 - 1 + 1 = 0

          if current_length > longest: # if 0 > 0
              longest = current_length

      return longest
print(longest_substring("abcabcbb"))

# or 
def length_of_longest_substring(s):
    seen = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        # If char was seen and is inside the current window
        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len

####################################################
#Rotate an array by k positions ? 
from collections import deque

nums = deque([1, 2, 3, 4, 5])
nums.rotate(2)  # Rotates 2 steps to the right
# Result: deque([4, 5, 1, 2, 3])

# right rotation 
def rotate_right(nums, k):
    n = len(nums)
    k %= n  # Handle k > n
    return nums[-k:] + nums[:-k]

# left rotation 
def rotate_left(nums, k):
    n = len(nums)
    k %= n
    return nums[k:] + nums[:k]
#####################################
# find duplicates in a list 
# use SET 
def find_duplicates(mylist):
    my_set = set()
    my_duplicates = set()

    for each in mylist:
        if each in my_set:
            my_duplicates.add(each)

        my_set.add(each)

    return list(my_duplicates)


a = [1, 2, 3, 4, 5, 2, 6, 3, 2]
b = ["string", "lava", "monster", "lava", "monster", "monster"]

print(find_duplicates(a))
print(find_duplicates(b))

####################################
#Flatten a nested list by using recursion !
# list = [['a', 'b'],['c', 'd']]
# output = ['a', 'b','c', 'd']
def flatten_list(my_matrix):
    result = []
    for row in my_matrix:
        for each in row:
            result.append(each)
    return result

# BELLOW VERSION IS universal : 

def flatten_list_recursion(my_list):
      result = []

      for item in my_list:
          if isinstance(item, list): # if item is another list - meaning 3d matrix
              result.extend(flatten_list_recursion(item)) # pass the list BACk into this method - recursion 
          else:
              result.append(item)

      return result

a = [['a', 'b'],['c', 'd']]
l = [1, 2, [3, 4, [5, 6] ], 7, 8, [9, [10] ] ]
m = [[['item1', 'item2']], [['item3', 'item4']]] 
print(flatten_list(a))
print(flatten_list_recursion(l))
print(flatten_list_recursion(m))






# import math

# n = 3.7
# F_num = math.floor(n)

# print(F_num)

# b = 3.7
# B_num = math.ceil(b)

# print(B_num)