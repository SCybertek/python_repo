import pytest; 

def fuzzy_math(num, operator, num2): 
    if type(num) not in [int, float] or type(num2) not in [int, float]:
        raise Exception("Both num and num2 must be numbers.")
    if operator == '+':
        result = num + num2
    elif operator == '*':
        result = num * num2
    else: 
        raise Exception("Operator must be one of '+', '*'")  
    
    if result < 0 : 
        return "Negative"
    elif result < 10:
        return "Small number"
    elif result < 20:
        return "Medium number"
    else: 
        return "Large number"
    
# print(fuzzy_math(3, '+', 4))  # Should print "Small number"
# print(fuzzy_math(5, '*', 3))  # Should print "Medium number"
# print(fuzzy_math(10, '+', 15))  # Should print "Large number

class TestFuzzyClass: # has to be at the root level
    # writing test 
    # def test_fuzzy_math(self):
    #     assert fuzzy_math(3, '+', 4) == "Small number"
    #     assert fuzzy_math(5, '*', 3) == "Medium number"
    #     assert fuzzy_math(10, '+', 15) == "Large number"
    #     assert fuzzy_math(-5, '+', 2) == "Negative"

    def test_non_numeric_input_num1(self):
        with pytest.raises(Exception) as exc_info:
            fuzzy_math('three', '+', 4) 
        assert 'Both num and num2 must be numbers.' in str(exc_info)

    def test_non_numeric_input_num2(self):
        pass
    def test_addition_with_invalid_operator(self):
        pass
    def test_addition_with_small_result(self):
        assert fuzzy_math(3, '+', 4) == "Small number"
    def test_addition_with_medium_result(self):
        pass
    def test_addition_with_large_result(self):
        pass
    def test_multiplication_with_invalid_operator(self):
        pass
    def test_multiplication_with_small_result(self):
        pass
    def test_multiplication_with_medium_result(self):
        pass
    def test_multiplication_with_large_result(self):
        pass