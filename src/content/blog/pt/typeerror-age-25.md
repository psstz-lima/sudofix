---
title: "Fix TypeError: 'Age: ' + 25..."
description: "Learn how to resolve the TypeError in Python. Cannot concatenate string and integer. Use str(25)..."
pubDate: "2026-01-17"
tags: ["python", "typeerror", "debugging"]
---

# The Error

The `TypeError` in Python is a built-in exception that occurs when an operation or function is applied to an object of inappropriate type. Specifically, in the context of concatenating strings and integers, this error arises when you attempt to combine a string with a non-string type, such as an integer, without explicit conversion.

In Python, the `+` operator is used for both numeric addition and string concatenation. However, it cannot be used to concatenate a string with a non-string type directly. Thus, trying to perform the operation `"Age: " + 25` results in a `TypeError`.

# Why it Occurs

This error commonly occurs in the following scenarios:

1. **String Concatenation with Non-String Types**: Attempting to concatenate a string with an integer or any other non-string type directly using the `+` operator.
2. **Implicit Type Assumptions**: When developers assume that variables will always be of a certain type (e.g., string), leading to unexpected type mismatches.
3. **Dynamic Data Handling**: In cases where data types are not strictly enforced, such as when handling input from users or external data sources, which may produce unexpected type combinations.

# Example Code

Here is a straightforward example that causes a `TypeError`:

```python
age = 25
message = "Age: " + age
print(message)
```

When you run this code, the output will be:

```
TypeError: can only concatenate str (not "int") to str
```

This error message indicates that Python cannot combine a string (`"Age: "`) with an integer (`25`).

# How to Fix

To resolve the `TypeError`, you need to explicitly convert the integer to a string before concatenation. Here’s a step-by-step solution:

1. Identify the variable that is causing the type mismatch. In this case, it's `age`, which is an integer.
2. Use the `str()` function to convert `age` to a string.
3. Rewrite the concatenation with the converted string.

Here’s the corrected code:

```python
age = 25
message = "Age: " + str(age)
print(message)
```

When you run this fixed code, the output will be:

```
Age: 25
```

By converting the integer to a string, we successfully concatenate the two types without any errors.

# Best Practices

To avoid encountering `TypeError` due to type mismatches in the future, consider the following best practices:

1. **Type Checking**: Always check the types of variables before performing operations that involve multiple types. Use the `type()` function or `isinstance()` to verify types.
   
   ```python
   if isinstance(age, int):
       message = "Age: " + str(age)
   ```

2. **Using f-Strings**: For Python 3.6 and later, consider using f-strings (formatted string literals) which allow for easier and more readable formatting:
   
   ```python
   age = 25
   message = f"Age: {age}"
   print(message)
   ```

3. **Type Annotations**: Use type annotations to document expected types in function definitions, making it clear what types are expected, thus reducing the likelihood of type-related errors.

4. **Unit Testing**: Implement unit tests to ensure that your functions handle various data types correctly, which helps catch type errors early in the development process.

By adhering to these practices, you can significantly reduce the occurrence of `TypeError` and improve the robustness of your Python code.