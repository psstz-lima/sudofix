---
title: "Fix FileExistsError: os.makedirs('existing_dir')..."
description: "Learn how to resolve the FileExistsError in Python. File exists: 'existing_dir'. Handle existence or u..."
pubDate: "2026-01-17"
tags: ["python", "fileexistserror", "debugging"]
---

# The Error

`FileExistsError` is a built-in exception in Python that is raised when an operation attempts to create a file or directory that already exists. This error is a subclass of the `OSError` exception and specifically indicates that the target entity already exists, preventing the operation from proceeding.

# Why it occurs

This error commonly occurs when using file or directory creation functions such as `os.makedirs()` or `open()` in write mode when the specified path already exists. It indicates that the program is trying to create a directory or file that is already present in the filesystem, leading to a conflict. 

For example, if you attempt to create a directory named `existing_dir` using `os.makedirs("existing_dir")`, and that directory already exists, Python will raise a `FileExistsError`.

# Example Code

Here's a simple example that demonstrates how this error can be raised:

```python
import os

# Attempting to create a directory that already exists
try:
    os.makedirs("existing_dir")  # This will raise FileExistsError if 'existing_dir' exists
except FileExistsError as e:
    print(f"Error: {e}")
```

In this example, if the directory `existing_dir` is already present in the current working directory, running this code will produce the following output:

```
Error: [Errno 17] File exists: 'existing_dir'
```

# How to Fix

To handle the `FileExistsError`, you have a couple of options:

### Option 1: Check for existence before creating

You can check if the directory already exists before attempting to create it. This can be done using `os.path.exists()`:

```python
import os

directory_name = "existing_dir"

# Check if the directory exists before creating it
if not os.path.exists(directory_name):
    os.makedirs(directory_name)
else:
    print(f"The directory '{directory_name}' already exists.")
```

### Option 2: Use `exist_ok` parameter

Starting from Python 3.2, the `os.makedirs()` function has an optional parameter called `exist_ok`. If set to `True`, it allows the function to succeed even if the target directory already exists:

```python
import os

# Create a directory with exist_ok set to True
os.makedirs("existing_dir", exist_ok=True)
```

In this case, if `existing_dir` already exists, the function will not raise an error, and your program can continue running smoothly.

# Best Practices

1. **Use `exist_ok=True`**: If you are using Python 3.2 or later, prefer using the `exist_ok` parameter to avoid handling exceptions manually, especially when the existence of the directory is an expected condition.

2. **Error Handling**: If you choose not to use `exist_ok=True`, always implement error handling when performing file or directory operations. This ensures your program can handle unexpected conditions gracefully.

3. **Check Existence**: When it makes sense for your application, check if the directory or file exists before attempting to create it. This approach can prevent unnecessary exceptions and make your code more robust.

4. **Use Context Managers**: When working with files, use context managers (the `with` statement) to ensure files are properly handled, which can reduce the chances of running into `FileExistsError` when opening files.

By following these best practices, you can minimize the chances of encountering `FileExistsError` and ensure your Python code is more resilient and user-friendly.