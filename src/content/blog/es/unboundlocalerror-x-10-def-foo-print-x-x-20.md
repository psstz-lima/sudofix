---
title: "Fix UnboundLocalError: x = 10; def foo(): print(x); x..."
description: "Learn how to resolve the UnboundLocalError in Python. Local variable 'x' referenced before assignment. U..."
pubDate: "2026-01-17"
tags: ["python", "unboundlocalerror", "debugging"]
---

# The Error

The `UnboundLocalError` is a specific type of error that occurs in Python when a local variable is referenced before it has been assigned a value. This situation typically arises when a variable is declared within a function scope but is attempted to be accessed before the local assignment takes place. The error message indicates that the variable is being treated as a local variable, but it has not yet been initialized with a value.

# Why it occurs

This error commonly occurs under the following circumstances:

1. **Local vs Global Scope**: When a variable is assigned a value in a function, Python treats it as a local variable unless explicitly declared as global. If you try to access it before the assignment, an `UnboundLocalError` is raised.
   
2. **Variable Shadowing**: If a variable in the local scope has the same name as a variable in the global scope, Python will prioritize the local variable, which can lead to confusion if you intend to access the global variable instead.

3. **Function Definitions**: When a function is defined, any variable that is assigned within that function is considered local to that function. If you reference such a variable before it's assigned, Python will throw an `UnboundLocalError`.

# Example Code

Here’s an example that demonstrates the `UnboundLocalError`:

```python
x = 10

def foo():
    print(x)  # Attempt to print the local variable 'x' before assignment
    x = 20    # Local variable assignment

foo()
```

When the `foo()` function is called, the interpreter will raise an `UnboundLocalError` with a message similar to:

```
UnboundLocalError: local variable 'x' referenced before assignment
```

This happens because Python sees the assignment `x = 20` within the function and assumes `x` is a local variable. However, the `print(x)` statement tries to access `x` before it has been assigned a value within the local scope.

# How to Fix

To resolve the `UnboundLocalError`, you have a couple of options based on the context of your program:

### Option 1: Use `global` keyword

If you intend to use the global variable `x`, you can declare it as global within the function.

```python
x = 10

def foo():
    global x  # Declare x as global
    print(x)  # Now this references the global x
    x = 20    # Modify the global variable

foo()  # Output: 10
print(x)  # Output: 20
```

### Option 2: Pass as an argument

Another approach is to pass the variable as an argument to the function.

```python
x = 10

def foo(x):
    print(x)  # Access the argument x
    x = 20    # This modifies the local x, not the global one
    return x

new_x = foo(x)  # Output: 10
print(new_x)    # Output: 20
print(x)        # Output: 10 (global x remains unchanged)
```

By passing `x` as an argument, you maintain clarity and avoid unintended modifications to the global variable.

# Best Practices

To prevent `UnboundLocalError` and similar issues, consider the following best practices:

1. **Explicitly declare global variables**: If you intend to modify a global variable within a function, always use the `global` keyword.

2. **Use function arguments**: Instead of relying on global variables, pass necessary values as arguments to functions. This makes your functions more reusable and easier to test.

3. **Avoid variable shadowing**: Use distinct names for local and global variables to minimize confusion and accidental shadowing.

4. **Initialize variables**: Always initialize your variables before their usage to ensure they contain expected values.

5. **Code reviews and linting**: Regularly review your code and use linters to catch potential issues early in the development process. Tools like `pylint` or `flake8` can help identify problematic patterns.

By adhering to these practices, you can write cleaner, more maintainable Python code and avoid common pitfalls such as `UnboundLocalError`.