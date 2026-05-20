import pytest;
# import sys;
# print(sys.executable)  # prints the path of the Python interpreter being used


def print_sum(a,b):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("These needs to be a number")
    return a + b

def test_print_sum():
    assert print_sum(35, 5) == 40, "positive test: adding 35 and 5"
def test_print_sum_exception():
    with pytest.raises(TypeError):
        print_sum(35, "a"), "negative test: adding 35 and a string should raise an exception"

# print(print_sum(3, 5))  # Should print 8
# print(print_sum(2.5, 4.5))  # Should print 7
# print(print_sum(3, "five"))  # Should raise TypeError


def division(a,b):
    if b == 0:
        raise ValueError("Cannot divide by 0")
    return a/b


def test_division():
    with pytest.raises(ValueError):
        division(10,0), "Cannot divide by O"