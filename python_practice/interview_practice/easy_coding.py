#reverse a string 
def reverse_string(string):
    reverse_string = ""
    for x in range(len(string)-1, -1, -1):
        reverse_string += string[x]
    return reverse_string


# def print_each(string):
#     for x in range(len(string)):
#         print(string[x])

word = "The world is fun!"

# # print_each(word)
reversed = reverse_string(word)
print(reversed)

# one liner reverse in Python 
print(word[::-1])

######################################
#check if a string is a palindrome 
def is_palindrome(string):
    left = 0
    right = len(string)-1
    while left < right:
        if string[left] != string[right]:
            return False
        left +=1
        right -=1
    return True

print(is_palindrome("abba"))

##$##################################
# find largest number in list
def largest_num(nums):
    large_num = 0
    for each in nums: 
        if each > large_num:
            large_num = each
    return large_num

nums = [1,2,45,78,99]
print(largest_num(nums))

#########################
# count vowels in string 
def vowel_counts(my_word):
    count = 0
    for each in my_word.lower():
        if each in ['a', 'o', 'u','e','i','y']:
            count +=1
    return count

print(vowel_counts("My world is big and beautiful"))

#########################
#remove duplicate from a list 
def remove_duplicate(my_list):
    new_set = set()
    for each in my_list:
        new_set.add(each)
    return new_set

old_list = [1,2,3,3,2,3,4]
print(remove_duplicate(old_list))
# or 
def remove_duplicates2(my_list):
    new_list = []
    seen = set()
    for each in my_list:
        if each not in seen:
            new_list.append(each)
            seen.add(each)
    return new_list

################
# find missing number from 1 to n
def find_missing_number(numbers):
      n = len(numbers) + 1
      expected_sum = n * (n + 1) // 2 
      # round to the nearest whole number after division 
      actual_sum = sum(numbers)

      return expected_sum - actual_sum

print(find_missing_number([1,2,3,5]))
#################
#Check if two strings are anagrams
# listen and silent
def is_anagram(first,second):
    first = first.lower()
    second = second.lower()

    if len(first) != len(second):
        return False
    
    return sorted(first) == sorted(second)


# or 
def is_anagram2(first, second):
    first = first.lower()
    second = second.lower()

    if len(first) != len(second):
        return False
    
    for char in first:
        if first.count(char) != second.count(char): # count method counts the instances of the character
            return False
    return True
    
print(is_anagram("listen", "Silent"))
print(is_anagram2("listen", "Silent"))

####################################
# Count frequency of each character in a string
# banana -> B: 1, A: 3, N : 2
def count_chars(text):
    frequency = {}
    for char in text.lower():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

print(count_chars("banana"))

####################################
#FizzBuzz is a common programming task where you print numbers from 1 to 100, 
# replacing multiples of 3 with "Fizz," multiples of 5 with "Buzz," 
# and multiples of both with "FizzBuzz". 
def fizzbuzz(number):
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else: 
        return number

for number in range(1,100):
    print(fizzbuzz(number))
###################################
#Find the second largest number in a list
def second_largest(my_list):
    largest = my_list[0]
    second_largest = None

    for num in my_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num

    return second_largest


my_list = [12, 22, 34, 67]
print(second_largest(my_list))

