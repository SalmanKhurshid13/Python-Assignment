# Task 1 - Factorial using Recursion

def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1

    # Recursive Case
    return n * factorial(n - 1)


try:
    number = int(input("Enter a positive integer: "))

    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {number} is: {factorial(number)}")

except ValueError:
    print("Invalid input! Please enter an integer.")

# Task 2

import math

try:
    number = float(input("Enter a number: "))

    if number < 0:
        print("Square root and logarithm are not defined for negative numbers.")
    else:
        print(f"Square Root: {math.sqrt(number)}")

        if number == 0:
            print("Natural Logarithm: Undefined")
        else:
            print(f"Natural Logarithm: {math.log(number)}")

        print(f"Sine: {math.sin(number)}")

except ValueError:
    print("Invalid input! Please enter a valid number.")




   