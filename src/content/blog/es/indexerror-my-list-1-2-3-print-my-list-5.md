---
title: "Fix IndexError: my_list = [1, 2, 3]; print(my_..."
description: "Learn how to resolve the IndexError in Python. List index out of range. Check the list length...."
pubDate: "2026-01-17"
tags: ["python", "indexerror", "debugging"]
---

# The Error

An `IndexError` in Python occurs when you attempt to access an index that is not within the bounds of a list (or any other sequence type). This means you are trying to reference an element at a position that does not exist in the list. In Python, list indices start from zero, meaning that for a list of length `n`, the valid indices range from `0` to `n-1`.

## Why it occurs

`IndexError` typically occurs in the following scenarios:

1. **Accessing Beyond the List Length**: Attempting to access an index that is greater than or equal to the length of the list.
2. **Negative Index Out of Bounds**: Using a negative index that exceeds the negative length of the list.
3. **Dynamic Lists**: Trying to access an index after modifying the list (e.g., removing elements) without checking its length.

## Example Code

Consider the following code snippet:

```python
my_list = [1, 2, 3]
print(my_list[5])  # This will raise an IndexError
```

In this example, `my_list` contains three elements, indexed from `0` to `2`. Attempting to access `my_list[5]` results in an `IndexError` because the index `5` is out of range for the list.

## How to Fix

To fix the `IndexError`, follow these steps:

1. **Check the List Length**: Before accessing an index, ensure it is less than the length of the list.
2. **Use Conditional Statements**: Implement checks to handle cases where the index may be out of range.
3. **Accessing Elements Safely**: You can use a try-except block to catch the error and handle it gracefully.

### Example of Fixing the Code

Here’s how you can modify the previous code to avoid the error:

```python
my_list = [1, 2, 3]

index_to_access = 5

# Step 1: Check if the index is within range
if index_to_access < len(my_list):
    print(my_list[index_to_access])
else:
    print(f"Index {index_to_access} is out of range. List length is {len(my_list)}.")
```

In this code, we check if `index_to_access` is less than the length of `my_list` before trying to access it. If it is out of range, we print an informative message instead.

## Best Practices

To avoid encountering `IndexError` in the future, consider the following best practices:

- **Always Check Length**: Before accessing an index, verify that it is within the valid range using `len()`.
- **Use List Slicing**: When retrieving sublists, use slicing (e.g., `my_list[start:end]`) to avoid out-of-range errors.
- **Iterate with Care**: When looping through lists, use `enumerate()` to get both the index and the value safely.
- **Understand Negative Indices**: Remember that negative indices count from the end of the list. Ensure they do not exceed the list's length in the negative direction.
- **Utilize Exception Handling**: Use try-except blocks to gracefully handle potential index errors when accessing list elements, especially in dynamic contexts.

By following these practices, you can write more robust Python code that minimizes the risk of running into `IndexError`.