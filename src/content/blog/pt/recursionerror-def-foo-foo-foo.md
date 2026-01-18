---
title: "Fix RecursionError: def foo(): foo(); foo()..."
description: "Learn how to resolve the RecursionError in Python. Maximum recursion depth exceeded. Check base case ..."
pubDate: "2026-01-17"
tags: ["python", "recursionerror", "debugging"]
---

## The Error

In Python, a `RecursionError` is raised when the maximum recursion depth is exceeded. This means that a function has called itself too many times without reaching a base case that would stop the recursion. Python has a default recursion limit (which can be checked or modified using `sys.getrecursionlimit()` and `sys.setrecursionlimit()`, respectively), and when this limit is surpassed, Python raises a `RecursionError` to prevent a stack overflow.

## Why it occurs

A `RecursionError` typically occurs due to one of the following reasons:

1. **Missing Base Case**: A recursive function must have a base case that stops the recursion. If there is no base case or if the base case is unreachable, recursion will continue indefinitely.
  
2. **Incorrect Base Case Logic**: If the logic to reach the base case is flawed, the function may never hit the condition that stops the recursion.

3. **Too Many Recursive Calls**: Even with a correct base case, if the function calls itself too many times before reaching the base case, it can still exceed the maximum recursion depth.

## Example Code

Here is a simple example that demonstrates how a `RecursionError` can occur:

```python
def foo():
    foo()  # Recursive call without a base case

foo()
```

In this example, the function `foo` calls itself indefinitely. Since there is no base case to terminate the recursion, Python will eventually raise a `RecursionError`, displaying a message like:

```
RecursionError: maximum recursion depth exceeded in comparison
```

### A More Complex Example

Let’s look at a slightly more complex example where the base case is incorrectly defined:

```python
def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)  # Intended base case, but it will cause RecursionError if n is negative
    # Missing base case for when n is 0 or negative

countdown(5)
countdown(-1)  # This will eventually lead to RecursionError
```

In the above code, if `countdown` is called with a negative number, it will enter an infinite loop, resulting in a `RecursionError`.

## How to Fix

To fix a `RecursionError`, follow these steps:

1. **Identify the Recursive Function**: Locate the function that is causing the recursion.

2. **Define a Base Case**: Ensure that you have a base case that will eventually be reached. This base case should stop the recursion.

3. **Check Logic of Base Case**: Verify that the logic leading to the base case is correct. Ensure that the function will not call itself indefinitely.

4. **Test with Varied Inputs**: Test the function with different inputs to confirm that it behaves correctly and does not exceed the recursion limit.

### Revised Example

Here is the corrected version of the `countdown` function:

```python
def countdown(n):
    if n <= 0:  # Base case to stop recursion
        print("Blast off!")
        return  # Exit the function
    print(n)
    countdown(n - 1)  # Recursive call

countdown(5)  # This will work correctly and print numbers from 5 to 1
```

In this corrected version, the base case is clearly defined. When `n` is less than or equal to zero, the function prints "Blast off!" and returns, thus preventing a `RecursionError`.

## Best Practices

To avoid encountering `RecursionError` in the future, consider the following best practices:

1. **Always Define a Base Case**: Make sure every recursive function has a clear and reachable base case.

2. **Limit Recursive Depth**: If possible, use iterative solutions instead of recursive ones, especially for problems that can involve deep recursion.

3. **Test Recursion with Edge Cases**: Test your recursive functions with edge cases that might lead to unexpected behavior.

4. **Monitor Recursion Depth**: Use `sys.getrecursionlimit()` to understand the default limit and adjust it if necessary, but be cautious as increasing the limit can lead to stack overflow.

5. **Use Debugging Tools**: Leverage debugging tools or print statements to trace the function calls, helping you identify where the recursion goes wrong.

By adhering to these practices, you can create robust recursive functions while minimizing the risk of `RecursionError`.