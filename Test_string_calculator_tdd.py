import pytest
from string_calculator_tdd import StringCalculator

#for empty string
def test_empty_string():
    calc = StringCalculator()
    assert calc.add("") == 0
    
# for a custom delimiter.
def test_custom_delimiter():
    calc = StringCalculator()
    assert calc.add("//;\n1;2") == 3
    assert calc.add("//*\n1*2*3")==6
    
#for a single number
def test_single_number():
    calc = StringCalculator()
    assert calc.add("1") == 1

# for two numbers.
def test_two_numbers():
    calc = StringCalculator()
    assert calc.add("1,5") == 6

#for multiple numbers.
def test_multiple_numbers():
    calc = StringCalculator()
    assert calc.add("1,2,3,4,5") == 15

#for negative numbers.
def test_negative_numbers():
    calc = StringCalculator()
    with pytest.raises(ValueError) as exc_info:
        calc.add("-1,2,-3")
    assert str(exc_info.value) == "negative numbers not allowed: -1,-3"