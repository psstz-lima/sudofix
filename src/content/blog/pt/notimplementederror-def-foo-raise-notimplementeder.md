---
title: "Fix NotImplementedError: def foo(): raise NotImplemente..."
description: "Learn how to resolve the NotImplementedError in Python. This method is not implemented yet...."
pubDate: "2026-01-17"
tags: ["python", "notimplementederror", "debugging"]
---

# The NotImplementedError

## The Error
`NotImplementedError` is a built-in exception in Python that indicates that a method or function has not been implemented yet. It is typically used in abstract base classes or methods to signal that any subclass or implementation must override the method to provide the actual functionality. When this error is raised, it halts the execution of the program unless it is caught by an exception handler.

## Why it occurs
This error occurs when you attempt to call a function or method that has been defined to raise `NotImplementedError`. This is a signal from the developer that the function is a placeholder and that implementation is expected in the future. This is particularly common in the context of:

- Abstract classes or interfaces where a method is intended to be overridden.
- Stubs for future implementations during development.
- Incomplete code where certain functionalities are not yet developed.

## Example Code
The following example illustrates how `NotImplementedError` can be encountered:

```python
class BaseClass:
    def method_to_implement(self):
        raise NotImplementedError("This method is not implemented yet.")

class DerivedClass(BaseClass):
    pass

obj = DerivedClass()
obj.method_to_implement()  # This will raise NotImplementedError
```

In this example, `BaseClass` defines a method `method_to_implement` that raises `NotImplementedError`. The `DerivedClass` inherits from `BaseClass` but does not implement the `method_to_implement` method. When we create an instance of `DerivedClass` and call `method_to_implement`, it raises `NotImplementedError`, indicating that the method is not yet implemented.

## How to Fix
To resolve the `NotImplementedError`, you need to implement the method defined in the base class. Here’s a step-by-step guide:

1. **Identify the Method**: Look at the traceback to find which method is causing the error.
2. **Implement the Method**: Provide a concrete implementation of the method in the derived class.
3. **Test the Implementation**: After implementing the method, run the code to ensure that the error is resolved.

Here’s how you can modify the previous example to provide an implementation:

```python
class BaseClass:
    def method_to_implement(self):
        raise NotImplementedError("This method is not implemented yet.")

class DerivedClass(BaseClass):
    def method_to_implement(self):
        print("This method has been implemented.")

obj = DerivedClass()
obj.method_to_implement()  # This now works and will print the message
```

In this fixed version, `DerivedClass` provides an implementation for the `method_to_implement`, and calling this method no longer raises `NotImplementedError`.

## Best Practices
To avoid encountering `NotImplementedError` unintentionally in the future, consider the following best practices:

1. **Use Abstract Base Classes**: When defining interfaces, use Python's `abc` module to create abstract base classes. This clearly communicates that subclasses must implement certain methods.

2. **Document Method Expectations**: Clearly document any methods that are intended to be overridden. This can prevent confusion for other developers.

3. **Implement Stubs**: If you plan to implement a method later, consider leaving a comment or a TODO note instead of raising `NotImplementedError`. This can help others understand your intent without causing the program to fail.

4. **Unit Testing**: Write unit tests to ensure that all methods are implemented and behave as expected. This helps catch any instances where a method may not have been implemented.

By following these practices, you can create more robust code and reduce the likelihood of encountering `NotImplementedError` in your applications.