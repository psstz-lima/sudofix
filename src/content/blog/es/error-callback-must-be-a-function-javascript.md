---
title: "Fix Error: Callback must be a function..."
description: "Learn how to resolve the Error in JavaScript. Expected a callback function but got something els..."
pubDate: "2026-01-17"
tags: ["javascript", "error", "debugging"]
---

## The Error
The "Error: Error" with the context "Callback must be a function" is a JavaScript error that occurs when a function expects a callback function as an argument, but receives something else instead. A callback function is a function passed into another function as an argument, to be executed by that function. This error indicates that the provided argument is not a function, which prevents the code from executing as expected.

## Why it occurs
This error commonly occurs due to one of the following reasons:
- Passing a non-function value (e.g., a string, number, object, etc.) as a callback.
- Passing an undefined or null value when a function is expected.
- Forgetting to define or initialize a function before passing it as a callback.
- Incorrectly using an arrow function or a traditional function definition in a context where one is not expected.

## Example Code
The following example demonstrates a scenario where this error might occur. Consider a simple asynchronous operation, `performAsyncOperation`, which expects a callback function to handle the result:
```javascript
function performAsyncOperation(callback) {
  // Simulate an asynchronous operation
  setTimeout(() => {
    // Attempt to call the callback function
    callback(null, "Operation result");
  }, 1000);
}

// Incorrect usage: Passing a string instead of a callback function
performAsyncOperation("not a function");

// Incorrect usage: Passing an object instead of a callback function
performAsyncOperation({});

// Incorrect usage: Passing undefined instead of a callback function
let callbackFunction;
performAsyncOperation(callbackFunction);

// Correct usage: Passing a function as the callback
performAsyncOperation((error, result) => {
  if (error) {
    console.error(error);
  } else {
    console.log(result);
  }
});
```
In the incorrect usage examples, `performAsyncOperation` will throw an error because it expects a function as the callback, but receives something else.

## How to Fix
To fix this error, ensure that you pass a valid function as the callback argument. Here are the steps:
1. **Verify the callback argument**: Before calling the function that expects a callback, ensure that the argument you are passing is indeed a function.
2. **Define the callback function**: If you haven't already, define the callback function before passing it. This could be an anonymous function (as in the correct usage example) or a named function.
3. **Check for typos and syntax errors**: Make sure there are no typos or syntax errors in your function definitions or when passing the callback.
4. **Use type checking**: If possible, use type checking mechanisms (like TypeScript) to ensure that the callback argument is of the correct type.

## Best Practices
To avoid this error in the future:
- **Always verify the type of callback arguments**: Before calling a function that expects a callback, ensure the argument is a function using `typeof callback === 'function'`.
- **Use default values or optional parameters**: Consider using default values for callback parameters or making them optional to handle scenarios where a callback might not be provided.
- **Implement robust error handling**: Ensure that your functions handle potential errors gracefully, including the case where a callback is not a function.
- **Follow established coding standards and patterns**: Adhere to widely accepted coding standards and patterns for callbacks and asynchronous programming to minimize the chance of errors.