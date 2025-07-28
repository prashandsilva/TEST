#!/usr/bin/env python3
"""
Test file for calculator functions
Demonstrates testing code changes
"""

import sys
import os

# Add the current directory to the path so we can import calculator
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from calculator import add, subtract, multiply, divide, power

def test_addition():
    """Test addition function"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("✓ Addition tests passed")

def test_subtraction():
    """Test subtraction function"""
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    print("✓ Subtraction tests passed")

def test_multiplication():
    """Test multiplication function"""
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    print("✓ Multiplication tests passed")

def test_division():
    """Test division function"""
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    assert divide(0, 1) == 0
    
    # Test division by zero
    try:
        divide(5, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected
    print("✓ Division tests passed")

def test_power():
    """Test power function"""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 2) == 9
    print("✓ Power tests passed")

def run_all_tests():
    """Run all calculator tests"""
    print("Running calculator tests...")
    print("=" * 30)
    
    try:
        test_addition()
        test_subtraction()
        test_multiplication()
        test_division()
        test_power()
        
        print("=" * 30)
        print("🎉 All tests passed!")
        return True
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)