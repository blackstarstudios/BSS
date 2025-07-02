# BSS Python Standard
import os
import sys
import math

from collections import namedtuple

MAX_COUNT = 10

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

if __name__ == "__main__":
    main()
