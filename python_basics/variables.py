variable_1 = 2
variable_2 = '2'
print(variable_1 + int(variable_2))
# The above line converts the string '2' to an integer before performing addition, resulting in 4.
print(variable_1, variable_2)

string_1 = "hello, "
string_2 = "world!"
print(string_1 + ' ' + string_2) 

print( string_1 * 3)  # string repetition : repeats the string 3 times
print( string_1 + str(variable_1)) 
# concatenation of string and integer (after converting integerto string)
print( string_1, variable_1) 
# using comma in print function : prints string and integer with a space in between (without concatenation)

boolean_1 = True
boolean_2 = False
print(boolean_1 and boolean_2)  # and operator : if one is False, returns False
print(boolean_1 or boolean_2)  # or operator : if one is True, returns True

print(not boolean_1)  # not operator : reverses the boolean value   

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
print(list_1 + list_2)  # concatenation of two lists  

dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'd': 4}  

print(dict_1, "helloooo", dict_2['c'])  # prints the first dictionary, and first value of the second dictionary

merged_dict = {**dict_1, **dict_2}  # merging two dictionaries
print(merged_dict)

print(type(variable_1))  # prints the type of variable_1
print(type(string_1))    # prints the type of string_1
print(type(boolean_1))   # prints the type of boolean_1
print(type(list_1))      # prints the type of list_1
print(type(dict_1))      # prints the type of dict_1