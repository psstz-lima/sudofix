---
title: "Fix TypeError: 'a' - 'b'..."
description: "Learn how to resolve the TypeError in Python. Unsupported operand type(s) for -: 'str' and 'str'..."
pubDate: "2026-01-17"
tags: ["python", "typeerror", "debugging"]
---

## The Error

The `TypeError` in Python is raised when an operation or function is applied to an object of inappropriate type. Specifically, in the context of the error message `'a' - 'b'`, Python is indicating that it encountered an unsupported operation between two string operands. In this case, the subtraction operator (`-`) is not defined for string types, hence the error message "unsupported operand type(s) for -: 'str' and 'str'".

## Why it Occurs

This error typically occurs in scenarios where a developer mistakenly attempts to perform arithmetic operations on strings. Common causes include:

- Misunderstanding the data types being used in operations.
- Attempting to manipulate string representations of numbers without converting them to a numeric type.
- Copying and pasting code without verifying the data types of variables involved in operations.

## Example Code

Here is an example that triggers the `TypeError`:

```python
# Example of TypeError: unsupported operand type(s) for -: 'str' and 'str'
a = "10"
b = "5"

# Attempting to subtract two strings
result = a - b  # This line will raise a TypeError
print(result)
```

In this example, both `a` and `b` are strings, and the operation `a - b` is invalid, leading to a `TypeError`.

## How to Fix

To resolve this error, you need to ensure that the operands involved in the arithmetic operation are of compatible types. Here are the steps to fix the error:

1. **Identify the Data Types**: Check the types of the variables involved in the operation using the `type()` function.
   
   ```python
   print(type(a))  # Output: <class 'str'>
   print(type(b))  # Output: <class 'str'>
   ```

2. **Convert Strings to Numbers**: If the strings represent numeric values, convert them to an appropriate numeric type (e.g., `int` or `float`).

   ```python
   a = int(a)  # Convert '10' from string to integer
   b = int(b)  # Convert '5' from string to integer
   ```

3. **Perform the Operation**: After the conversion, you can safely perform the subtraction.

   ```python
   result = a - b  # Now this will work
   print(result)    # Output: 5
   ```

Here is the complete corrected code:

```python
a = "10"
b = "5"

# Convert strings to integers
a = int(a)
b = int(b)

# Perform the subtraction
result = a - b
print(result)  # Output: 5
```

## Best Practices

To avoid encountering `TypeError` when performing arithmetic operations in Python, consider the following best practices:

1. **Type Checking**: Always verify the data types of variables before performing operations. Utilize the `type()` function for clarity.

2. **Input Validation**: When accepting user input or data from external sources, validate and sanitize the data to ensure it is in the expected format.

3. **Use Exceptions**: Implement error handling using `try` and `except` blocks to gracefully manage potential type errors.

   ```python
   try:
       result = int(a) - int(b)
   except ValueError as e:
       print(f"Error converting to integer: {e}")
   except TypeError as e:
       print(f"Type error: {e}")
   ```

4. **Clear Documentation**: Document your code clearly, specifying expected data types for variables, especially when their types may change.

By following these practices, you can significantly reduce the occurrence of `TypeError` and ensure smoother execution of your Python code.