#!/usr/bin/env python3
def print_fibonacci(length):
    fibonacci_sequence = []  # Initialize an empty list to store the Fibonacci sequence

    # Generate the Fibonacci sequence up to the desired length
    a, b = 0, 1
    for _ in range(length):
        fibonacci_sequence.append(a)  # Add the current Fibonacci number to the sequence
        a, b = b, a + b  # Update the Fibonacci numbers for the next iteration

    print(fibonacci_sequence)

# Test the function with a length of 9
print_fibonacci(9)
