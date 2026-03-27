def print_sum(a,b):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("Both arguments must be numbers.")
    return a + b    


print(print_sum(3, 5))  # Should print 8
print(print_sum(2.5, 4.5))  # Should print 7
print(print_sum(3, "five"))  # Should raise TypeError