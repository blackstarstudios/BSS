# BSS Python Standard
import os
import sys
import math

from collections import namedtuple

MAX_COUNT = 10

i = 1
i = i + 1
i += 1
x = i*2 - 1
hypot2 = x*x + i*i
c = (x+x) * (i-i)

class Greeter:
    """A class to greet users."""

    def __init__(self, name):
        self.name = name
      
    def greet(self):
        """Return a greeting message."""
        return f"Hello, {self.name}!"

def calculate_area(radius):
    """Return the area of a circle given its radius."""
    return math.pi * (radius ** 2)

def process_numbers(numbers):
    """Process a list of numbers and return their squares."""
    squares = []
    for number in numbers:
        # PEP 8: Inline comment example
        squares.append(number ** 2)
    return squares

def main():
    """Main function to run the script."""
    greeter = Greeter("Alice")
    message = greeter.greet()
    print(message)

    Circle = namedtuple("Circle", ["radius"])
    circle = Circle(radius=5)
    area = calculate_area(circle.radius)
    print(f"Area: {area:.2f}")

    numbers = [1, 2, 3, 4, 5]
    squares = process_numbers(numbers)
    print("Squares:", squares)

    count = 0
    while count < MAX_COUNT:
        print(f"Count: {count}")
        count += 1

    if len(sys.argv) > 1:
        # PEP 8: Block comment example
        # This block handles command-line arguments
        print("Arguments:", sys.argv[1:])

# Example of a multi-line docstring. If your function has some complexity
# a more descriptive docstring is recommended that includes descriptions
# of the function arguments and outputs like so.

def add_one(number):
    """
    add_one() takes an integer, float and returns that value 
    added by one.
    """
    number_plus_one = number + 1
    return number_plus_one

def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
    
# Aligned with opening delimiter 
foo = long_function_name('var_one', 'var_two',
                         'var_three', 'var_four')

# Below is a verbose list comprehension that is 79 characters long as a silly example
[integer**2+1 for integer in range(1,100) if integer > 20 and integer % 5 == 0]

income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

def add_two(number):
    """
    add_two() takes an integer, float and returns that value 
    added by one.
    
    Arguments: number - a single integer or float.
    
    Returns:   number_plus_two - the sum of the given integer or float and 
               two.
    """
    number_plus_one = number + 1
    return number_plus_one


if __name__ == "__main__":
    main()
