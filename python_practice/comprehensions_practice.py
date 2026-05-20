import pprint


values = []
for x in range(10):
    values.append(x)

print(values)


##### list comprehension 
values = [x for x in range(10)]
print(values)

values = [x + 1  for x in range(10)]
print(values)

######## get all even numbers from 0 to 50 and add them to the list 
evens = []

for x in range(50):
    if x % 2 == 0:
        evens.append(x)

print(evens)

evens = [num for num in range(50) if num % 2 == 0]
print(evens)

# strings that start with "a" and finish with "e"
strings = ["apple", "banana", "avocado", "grape", "orange"]
new_strings = []

for word in strings:
    if len(strings) <= 1:
        continue
    if word[0] == "a" and word[-1] == "e":
        new_strings.append(word)

print(new_strings)
# ALL conditions MUST beb TRUE -> bellow is the same as above but with comprehensions 
valid_strings = [ word for word in strings 
                 if len(strings) >= 2 
                 if word[0] == "a" 
                 if word[-1] == "e"
                 ]

########################
# flatting a matrix ( list of lists)
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flatted = []

for row in matrix:
    for num in row:
        flatted.append(num)

print(flatted)
# exterior and then interior loop
flatted = [ num for row in matrix for num in row]
print(flatted)

#####################
#categorize number to be even or odd
nums = [1,2,3,4,5,6,7]
for each in nums:
    if each % 2 == 0:
        print(f"{each} is even")
    else:
        print(f"{each} is odd")


##################
#build 3 D list 
printer = pprint.PrettyPrinter()

list = []

for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for num in range(5):
            l2.append(num)
        l1.append(l2)
    list.append(l1)
# printer.pprint(list)

list = [[[num for num in range(5)] for _ in range(5) ] for _ in range(5)]
# printer.pprint(list)

############ list comp. with functions 
# right side is a filter
# left side is what exactly you want to take 

def square(x):
    return x*x

square_num = [square(x) for x in range(10)]
print(square_num)

############# creating dictionary comp.
pairs = [("a", 1), ("b", 2), ("c", 3)]
my_dict = {k: v for k,v in pairs}
print(my_dict)

############# creating set comp.
# removing duplicates form a list while applying a function
# SET DO NOT HAVE keys!!! both have {} brakets 
nums = [1,2,2 ,3,3,3,3,4,4,4,5] 
unique_num = {x for x in nums}
print(unique_num)
# or add a function as well 
unique_num = {x**2 for x in nums}
print(unique_num)

############# gennerator comp.
# generate a sum of all the squares from 1 to 100000
sum_of_squares = sum(x**2 for x in range(100))
print(sum_of_squares)
# generator ONLY retuns values when they need to be used, 
# generates on the fly NOT stored in memory
# [s]um(x**2 for x in range(100))] --> will generate VALUES and STORE Them , do NOT use it unless you need to store

