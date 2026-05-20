age = 18 
name = "Sasha"

print(f"Hi my name is {name} and I am {age} old", end= " ||| ")
print("New print")

######################

# help(print)
#####################

my_range = range(10)

for x in my_range:
    print(x)


print("This new print adds number to the list: ")
print(list(my_range))

my_new_range = range(1,22, 2) # from , to , what iteration

for x in my_new_range:
    print(x)


############### map function
strings = ["my", "world", "apple", "pear"]
lengths = map(len, strings) # returns iterator 
print(list(lengths))

# lambda function : one liner functions 
lengths = map(lambda s: s + "!", strings) # returns iterator 
print(list(lengths))

lengths = map(lambda s: s[-1], strings) # returns iterator 
print(list(lengths))


################## filter function 
def is_even(nums):
    if type(nums) not in [int, float]:
        raise TypeError
    return nums % 2 == 0
    
numbers = [12, 33, 22, 10]
filtered = filter(is_even, numbers)
print(list(filtered)) # returns list of event numbers

print(is_even(10)) # returns true or false

def longer_than_4(string):
    return len(string) > 4
filtered = filter(longer_than_4, strings)
print(list(filtered))

print(len(numbers))
print(len(strings))
print(len("Sofiya"))

################ sum function 
numbers = [1, 2]
numbers2 = {1, 3}
print(f"printing sum ", sum(numbers))
print(f"printing sum ", sum(numbers2))
print(f"printing sum ", sum(numbers2, start=10))

############## sort
numbers = [1, 3, -2, 10, 7]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

people = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 35},
    {"name": "Avril", "age": 15},
]

sorted_people = sorted(people, key=lambda person: person['age'])
print(sorted_people)

############### enumerate 
tasks = ["write report", "Attend meeting", "Dance on the table", "Meet new people"]
# for i, each_task in tasks:
#     print(f"This is my index {i} and this is the task {each_task}")

for index in range(len(tasks)):
    task = tasks[index]
    print(f"{index+1}. {task}")

# for index in tasks:
#     print(f" {index}")

for index, task in enumerate(tasks):
    print(f"{index+1}. {task}")

print(list(enumerate(tasks)))

#################### zip function
names = ["Bob", "Alice", "Charlie", "David"]
ages = [20, 23, 26, 33]

for index in range(min(len(names), len(ages))):
    name = names[index]
    age = ages[index]
    print(f"{name} is {age} years old")

print(f"################################")

combined = list(zip(names, ages))
print(combined)
for name, age in combined:
    print(f"{name} is {age} years old")

############################### open function
print(f"################################")
file = open("test.txt", "w") # will overwrite 
file.write("Hello world \n my name is Sofi")
file.close

with open("test.txt", "a") as file: # append
    file.write("\n HEEEEE")
