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