---
title: "Fix IndentationError: expected an indented block..."
description: "Learn how to resolve the IndentationError in Python. Missing indentation after 'if' or 'def'...."
pubDate: "2026-01-17"
tags: ["python", "indentationerror", "debugging"]
---

## The Error

An `IndentationError` in Python indicates that the code does not conform to the expected indentation levels required by the language's syntax. Specifically, the message "expected an indented block" signifies that Python anticipates an indented line of code following a statement that introduces a new block, such as `if`, `def`, `for`, or `while`. Indentation is crucial in Python, as it dictates the structure and flow of control in the program.

## Why It Occurs

This error commonly occurs in the following scenarios:

1. **Missing indentation**: When a block of code is expected but not provided, especially after constructs like `if`, `def`, or `for`.
2. **Incorrect indentation level**: Mixing tabs and spaces or inconsistent indentation can lead to this error.
3. **Empty blocks**: Python does not allow empty blocks, and failing to provide at least a `pass` statement will result in this error.

## Example Code

Consider the following code snippet that triggers an `IndentationError`:

```python
def check_positive(number):
if number > 0:  # Missing indentation here
    return True
else:
    return False
```

When you run this code, you'll see an error similar to this:

```
IndentationError: expected an indented block
```

## How to Fix

To resolve an `IndentationError`, follow these steps:

1. **Identify the line causing the error**: The error message should point to the line where the indentation is missing.
2. **Add the necessary indentation**: Ensure that the code block following `if`, `def`, or any other statement requiring indentation is properly indented.

Here’s the corrected version of the previous example:

```python
def check_positive(number):
    if number > 0:  # Correctly indented
        return True
    else:
        return False
```

In this corrected code, the lines following the `if` statement are now properly indented, which resolves the `IndentationError`.

## Best Practices

To avoid `IndentationError` and ensure your code is clean and maintainable, follow these best practices:

1. **Consistent Indentation Style**: Choose either spaces or tabs for indentation and stick to one throughout your project. The Python community generally recommends using 4 spaces per indentation level.
2. **Use a Linter**: Tools like `pylint` or `flake8` can help catch indentation issues before you run your code.
3. **Editor Settings**: Configure your code editor to automatically insert spaces when you press the tab key and highlight indentation levels to ensure consistency.
4. **Always Indent After Control Statements**: Remember that any control statement (like `if`, `for`, `while`, `def`, etc.) requires an indented block to follow it. If there’s no code to execute, use the `pass` statement to indicate an empty block.
   
By adhering to these practices, you can significantly reduce the chances of encountering `IndentationError` in your Python code.