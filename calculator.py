#!/usr/bin/env python3
"""
Simple Calculator Module
A basic calculator to demonstrate code editing techniques
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract second number from first"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide first number by second"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Raise first number to the power of second"""
    return a ** b

def main():
    """Main function to test calculator"""
    print("Enhanced Calculator")
    print("=" * 30)
    
    # Basic operations
    print("5 + 3 =", add(5, 3))
    print("10 - 4 =", subtract(10, 4))
    print("6 * 7 =", multiply(6, 7))
    print("15 / 3 =", divide(15, 3))
    print("2 ^ 4 =", power(2, 4))
    
    # Error handling demonstration
    try:
        print("10 / 0 =", divide(10, 0))
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()