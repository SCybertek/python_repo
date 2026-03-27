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
print('Using operator module for addition:', operator.add(2, 3))

def other_function(arg1, arg2 = 'a', arg3 = None):
    pass # Placeholder for future code

other_function(5, arg3=True)