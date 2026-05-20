# Find the sum of all numbers in a list
# list = [1,2,3,4]
def find_sum(my_list):
    return sum(my_list)

l = [1,2,3,4]
print(sum(l))
    
# Check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
          if num % i == 0:
              return False
    return True
print(is_prime(7))   # True
print(is_prime(10))  # False

# Find factorial of a number
# 5! = 1*2*3*4*5 = 24*5 = 120
def factorial(number):
    result = 1
    i = 1
    while i <= number:
        result *=i
        i+=1
    return result

# version 2 
def factorial2(number):
      result = 1
      for i in range(1, number + 1):
          result *= i

      return result
print(factorial(5))

# Generate Fibonacci sequence up to n - recursion ? 
def fibonacci_number(n):
      if n == 0:
          return 0
      if n == 1:
          return 1

      return fibonacci_number(n - 1) + fibonacci_number(n - 2)


def fibonacci_sequence(count):
      result = []

      for i in range(count):
          result.append(fibonacci_number(i))

      return result

print(fibonacci_sequence(3))

# Find common elements between two lists , sliding window?
# l = [1,2]
# m = [2,3,4]
# output : [2]

def find_common(first, second):
     result = []
     for num in first:
          for nums in second:
               if num == nums:
                    result.append(num)
     return result
print(find_common([1,2,3], [2,3,4]))
#the same solution, different approach 
res = list(set([1,2,3]) & set([2,3,4]))
print(res)


# Capitalize first letter of each word
#
def capitalize_first(text):
     return text.title()
          
print(capitalize_first("hello world")) 

# Sort a list without using sort()
#  This uses bubble sort. It repeatedly compares neighboring values and swaps them if they are in the wrong order.
def sort_list(numbers):
      result = numbers[:]

      for i in range(len(result)):
          for j in range(0, len(result) - i - 1):
              if result[j] > result[j + 1]:
                  result[j], result[j + 1] = result[j + 1], result[j]

      return result

print(sort_list([4, 2, 1, 3]))

# print(len([1,2,3,4])) # 4
# print(len("sofiya")) # 6

# Count words in a sentence
def count_words(text):
    return len(text.split())
print(count_words("Sofiya is dancing all day and she is so smart"))

# Find the maximum occurring character in a string
def max_occurring_char(s):
    freq = {}

    # Count frequency of each character
    #  freq.get(char, 0) means:
#   - if char already exists in the dictionary, get its current count
#   - if char does not exist yet, use 0
#   Then + 1 adds one more count for the current character.
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Find character with maximum frequency
    max_char = max(freq, key=freq.get) #“Look at each key in freq, but compare them using their values.”

    return max_char, freq[max_char]
print(max_occurring_char("banana"))

# Swap two variables without using a third variable
def swap_variable(a, b):
      a, b = b, a
      return a, b

print(2,3)