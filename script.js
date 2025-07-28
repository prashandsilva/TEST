/**
 * JavaScript Calculator Functions
 * Demonstrates basic JavaScript code editing and best practices
 */

// Main calculation function with improved error handling
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

// Improved result display function
function showResult(message, type = "success") {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = message;
    resultDiv.className = type;
}

// Basic arithmetic functions
function add(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}

// Additional utility functions
function multiply(a, b) {
    return a * b;
}

function divide(a, b) {
    if (b === 0) {
        throw new Error("Cannot divide by zero");
    }
    return a / b;
}

function power(a, b) {
    return Math.pow(a, b);
}

// Advanced calculator function with operation selection
function performOperation(operation) {
    const num1 = Number(document.getElementById('num1').value);
    const num2 = Number(document.getElementById('num2').value);
    
    if (isNaN(num1) || isNaN(num2)) {
        showResult("Please enter valid numbers", "error");
        return;
    }
    
    let result;
    let operationSymbol;
    
    try {
        switch(operation) {
            case 'add':
                result = add(num1, num2);
                operationSymbol = '+';
                break;
            case 'subtract':
                result = subtract(num1, num2);
                operationSymbol = '-';
                break;
            case 'multiply':
                result = multiply(num1, num2);
                operationSymbol = '×';
                break;
            case 'divide':
                result = divide(num1, num2);
                operationSymbol = '÷';
                break;
            case 'power':
                result = power(num1, num2);
                operationSymbol = '^';
                break;
            default:
                throw new Error("Unknown operation");
        }
        
        showResult(`${num1} ${operationSymbol} ${num2} = ${result}`, "success");
    } catch (error) {
        showResult(`Error: ${error.message}`, "error");
    }
}

// Utility function to clear inputs
function clearInputs() {
    document.getElementById('num1').value = '';
    document.getElementById('num2').value = '';
    document.getElementById('result').innerHTML = '';
    document.getElementById('result').className = '';
}