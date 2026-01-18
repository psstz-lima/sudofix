---
title: "Fix TypeError: len(123)..."
description: "Learn how to resolve the TypeError in Python. Object of type 'int' has no len(). len() works on ..."
pubDate: "2026-01-17"
tags: ["python", "typeerror", "debugging"]
---

# The Error

The `TypeError` in Python is raised when an operation or function is applied to an object of inappropriate type. Specifically, the error message associated with `len(123)` indicates that the function `len()` is being called on an integer (`int`), which is not a valid operation. The `len()` function is designed to return the number of items in a container, such as a string, list, tuple, or dictionary. Since an integer does not have a defined length in this context, Python raises a `TypeError`.

# Why it occurs

The `TypeError` occurs when a programmer mistakenly assumes that an integer can be treated as a sequence or a collection of items. Common scenarios that lead to this error include:

- Attempting to use `len()` on a numeric variable instead of a sequence type.
- Passing an integer to a function or method that expects a sequence.
- Mistakenly using an integer where a string or list is expected.

# Example Code

Below is an example that demonstrates the `TypeError`:

```python
def print_length(value):
    try:
        print(f"The length of the value is: {len(value)}")
    except TypeError as e:
        print(f"Error: {e}")

# Attempting to get the length of an integer
print_length(123)
```

When the code is executed, the output will be:

```
Error: object of type 'int' has no len()
```

This message indicates that `len()` was called on an integer, which is not allowed.

# How to Fix

To resolve the `TypeError`, you need to ensure that you are passing a sequence type to the `len()` function. Here’s a step-by-step solution:

1. **Identify the Type**: Check the type of the variable you are passing to `len()`. Use the `type()` function if necessary.
   
   ```python
   print(type(123))  # Output: <class 'int'>
   ```

2. **Change the Input**: If the input is an integer, consider whether you meant to pass a different type, such as a string or list.
   
   For example, if you intended to get the length of a string:

   ```python
   value = "123"
   print_length(value)  # Output: The length of the value is: 3
   ```

3. **Use Conditional Logic**: If your function needs to handle different types, implement conditional logic to manage varying input types.

   ```python
   def print_length(value):
       if isinstance(value, (str, list, tuple, dict)):
           print(f"The length of the value is: {len(value)}")
       else:
           print("The provided value does not have a length.")
   
   print_length(123)    # Output: The provided value does not have a length.
   print_length("123")  # Output: The length of the value is: 3
   ```

# Best Practices

To avoid encountering a `TypeError` with `len()` in the future, follow these best practices:

- **Type Checking**: Always check the type of variables before performing operations that depend on specific data types.
- **Use Type Hints**: Leverage Python's type hints to indicate expected types in function signatures, making it easier for both you and others to understand the intended usage.
  
  ```python
  def print_length(value: str) -> None:
      print(f"The length of the value is: {len(value)}")
  ```

- **Documentation**: Provide clear documentation for your functions, specifying the expected input types and behavior.
- **Testing**: Implement unit tests for your functions to catch type-related errors early in the development process.

By adhering to these practices, you can minimize the occurrence of `TypeErrors` and improve the robustness of your code.