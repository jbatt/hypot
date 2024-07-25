import pytest
from src.hypot.source import sqrt

# test sqrt function for input is even number
def test_sqrt_even():
    input = 4
    expected_output = 2.0
    output = sqrt(input)
    assert output == expected_output
    
# test sqrt function for input is odd number
def test_sqrt_odd():
    input = 9
    expected_output = 3.0
    output = sqrt(input)
    assert output == expected_output
    
# test sqrt function for input is zero
def test_sqrt_zero():
    input = 0
    expected_output = 0
    output = sqrt(input)
    assert output == expected_output
    
# test sqrt function for input is negative
def test_sqrt_neg():
    input = -9
    expected_output = 3.0
    output = sqrt(input)
    assert output == expected_output

# test hypot function

