# Code Editing Examples: Before and After

This document demonstrates practical examples of code editing techniques applied to the files in this repository.

## Example 1: Adding New Functions to Python Code

### Before (Original calculator.py):
```python
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract second number from first"""
    return a - b

def main():
    """Main function to test calculator"""
    print("Basic Calculator")
    print("5 + 3 =", add(5, 3))
    print("10 - 4 =", subtract(10, 4))
```

### After (Enhanced calculator.py):
```python
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
```

### What Was Changed:
1. **Added new functions**: `multiply()`, `divide()`, `power()`
2. **Improved error handling**: Added exception for division by zero
3. **Enhanced main function**: More comprehensive testing with error handling
4. **Better formatting**: Added visual separator and organized output

## Example 2: Improving JavaScript with Error Handling

### Before (Original script.js):
```javascript
function calculate() {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    
    const result = Number(num1) + Number(num2);
    
    document.getElementById('result').innerHTML = `Result: ${result}`;
}
```

### After (Enhanced script.js):
```javascript
function calculate() {
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    const resultDiv = document.getElementById('result');
    
    // Input validation
    if (!num1Input.value || !num2Input.value) {
        showResult("Please enter both numbers", "error");
        return;
    }
    
    const num1 = Number(num1Input.value);
    const num2 = Number(num2Input.value);
    
    // Check for valid numbers
    if (isNaN(num1) || isNaN(num2)) {
        showResult("Please enter valid numbers", "error");
        return;
    }
    
    const result = add(num1, num2);
    showResult(`${num1} + ${num2} = ${result}`, "success");
}

function showResult(message, type = "success") {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = message;
    resultDiv.className = type;
}
```

### What Was Changed:
1. **Added input validation**: Check for empty inputs and invalid numbers
2. **Improved error handling**: Display user-friendly error messages
3. **Better code organization**: Separated result display logic
4. **Enhanced user experience**: Clear success/error indicators

## Example 3: Refactoring HTML Structure

### Before (Original index.html):
```html
<div class="calculator">
    <input type="number" id="num1" placeholder="Enter first number">
    <input type="number" id="num2" placeholder="Enter second number">
    <button onclick="calculate()">Add Numbers</button>
    <div id="result"></div>
</div>
```

### After (Enhanced index.html):
```html
<div class="calculator">
    <div class="input-group">
        <input type="number" id="num1" placeholder="Enter first number">
        <input type="number" id="num2" placeholder="Enter second number">
    </div>
    
    <div class="operation-buttons">
        <button onclick="performOperation('add')" class="operation-btn">Add (+)</button>
        <button onclick="performOperation('subtract')" class="operation-btn">Subtract (-)</button>
        <button onclick="performOperation('multiply')" class="operation-btn">Multiply (×)</button>
        <button onclick="performOperation('divide')" class="operation-btn">Divide (÷)</button>
        <button onclick="performOperation('power')" class="operation-btn">Power (^)</button>
    </div>
    
    <div id="result" class="result"></div>
    
    <div class="clear-section">
        <button onclick="clearInputs()" class="clear-btn">Clear</button>
    </div>
</div>
```

### What Was Changed:
1. **Better organization**: Grouped related elements
2. **Multiple operations**: Added buttons for different calculations
3. **Improved accessibility**: Better class names and structure
4. **Added functionality**: Clear button for resetting inputs

## Key Editing Techniques Demonstrated

### 1. **Incremental Enhancement**
- Start with basic functionality
- Add features one at a time
- Test after each change

### 2. **Error Handling**
- Anticipate potential problems
- Provide meaningful error messages
- Handle edge cases gracefully

### 3. **Code Organization**
- Group related functionality
- Use descriptive names
- Separate concerns

### 4. **User Experience**
- Validate inputs
- Provide feedback
- Make interfaces intuitive

### 5. **Documentation**
- Add comments for complex logic
- Use docstrings for functions
- Keep documentation updated

## Best Practices Applied

1. **Make small, focused changes**
2. **Test frequently**
3. **Maintain consistency**
4. **Consider the user experience**
5. **Document your changes**
6. **Handle errors gracefully**
7. **Use meaningful names**
8. **Keep code readable**

These examples show how code editing is an iterative process of improvement, where each change builds upon the previous version while maintaining or enhancing functionality.