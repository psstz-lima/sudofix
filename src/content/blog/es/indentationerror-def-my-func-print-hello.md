---
title: "Fix IndentationError: def my_func(): print('hello')..."
description: "Learn how to resolve the IndentationError in Python. The body of the function must be indented...."
pubDate: "2026-01-17"
tags: ["python", "indentationerror", "debugging"]
---

# The Error: IndentationError

An `IndentationError` in Python indicates that there is a problem with the indentation of your code. Python uses indentation to define the structure of the code, particularly for defining blocks of code such as the body of functions, loops, and conditional statements. When the indentation is not consistent or is missing where it is expected, Python raises an `IndentationError`.

# Why it occurs

This error typically occurs when:

- The body of a function is not indented, as Python expects some form of indentation to indicate that the following lines belong to that function.
- There are mixed spaces and tabs in the code, leading to inconsistent indentation levels.
- An expected block of code is not provided after a statement that requires it, such as `if`, `for`, or `def`.

# Example Code

Consider the following code snippet that raises an `IndentationError`:

```python
def my_func():
print("hello")
```

When you run this code, you will encounter an error similar to:

```
IndentationError: expected an indented block
```

In this example, the print statement is not indented, which means Python cannot determine that it is part of the `my_func()` function.

# How to Fix

To resolve the `IndentationError`, you need to ensure that the body of the function is properly indented. Here’s a step-by-step guide:

1. Identify the function definition line:
   ```python
   def my_func():
   ```

2. Ensure that the subsequent lines that make up the function's body are indented with spaces or tabs consistently. The standard practice is to use 4 spaces for each level of indentation.

3. Modify the code as follows:
   ```python
   def my_func():
       print("hello")
   ```

4. Now, when you run the corrected code, it will execute without raising an `IndentationError`.

# Best Practices

To avoid `IndentationError` in the future, consider the following best practices:

1. **Consistent Indentation**: Choose either spaces or tabs for indentation and stick with your choice throughout your code. The Python community recommends using 4 spaces for indentation.

2. **Use a Code Editor**: Utilize a code editor or integrated development environment (IDE) that highlights indentation levels and helps maintain consistent formatting.

3. **Linting Tools**: Employ linting tools like `pylint` or `flake8` in your development workflow. These tools can identify and alert you to indentation issues before you run your code.

4. **Readability**: Regularly review your code for readability. Properly indented code is not only less prone to errors but also easier to maintain and understand.

By adhering to these practices, you can minimize the chances of encountering `IndentationError` and write cleaner, more maintainable Python code.