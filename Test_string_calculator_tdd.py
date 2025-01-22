import pytest
from string_calculator_tdd import StringCalculator

#for empty string
def test_empty_string():
    calc = StringCalculator()
    assert calc.add("") == 0