print('Hi', 'there!')
other_print = print
other_print('This is another print function call.')

num = 1
num += 5
print('The value of num is:', num)

num2 = 10
num3 = 3
result = num2 * num3; 
result = result + 4
result = result - 2
print('The final result is:', result)

#function 
def greet(name):
    return f"Hello, {name}!"

def do_math(a, b=3): #default parameter b=3
    result = a * b
    result = result + 4
    result = result - 2
    return result


print(greet("Alice"))
print('The result of do_math is:', do_math(10, 3)) 

import operator
from unicodedata import name
print('Using operator module for addition:', operator.add(2, 3))

def other_function(arg1, arg2 = 'a', arg3 = None):
    pass # Placeholder for future code

other_function(5, arg3=True)


age = 22

def check_age(age):
    if (age > 30) : 
        result = "young adult!"
    elif (age > 20) : 
        result = "college grad!"
    else :
        result = "still in school"
    return result

check_age(age)

def test_checking_age():
    assert check_age(33) == "young adult!"
    assert check_age(25) == "college grad!"
    assert check_age(18) == "still in school"

# for loop
for i in range(3):
    print("hello", i+1 )

# while loop
i = 0 
while i < 5:
    i = i + 1
    print(i)

# while True:
#     user_input = input("Enter a number (or 'q' to quit): ")
#     if user_input == 'q':
#         break
#     print("You entered:", user_input)

def hello(name): 
    # print('Hello',name)
    # print('Hello ' + name)
    return f"Hello, {name}!"

print(hello("Sarah"))

def add_numbers(a, b):
    pass # Placeholder for future code


number = input("Enter a number: ")
try:
    print(10 + int(number))
except:
    print('That is not the valid number!')


