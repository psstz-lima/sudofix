---
title: "Fix SyntaxError: await is only valid in async f..."
description: "Learn how to resolve the SyntaxError in JavaScript. Use 'async' keyword on the function containing 'aw..."
pubDate: "2026-01-17"
tags: ["javascript", "syntaxerror", "debugging"]
---

## The Error
The `SyntaxError: await is only valid in async functions` error occurs when the JavaScript engine encounters an `await` expression outside of an `async` function. This error is raised because `await` is a reserved keyword in JavaScript that can only be used within functions declared with the `async` keyword. The `async` keyword is used to declare an asynchronous function, which allows the use of `await` to pause the execution of the function until a promise is resolved or rejected.

## Why it occurs
This error commonly occurs in the following scenarios:
- When a developer attempts to use `await` directly in the global scope or within a non-async function.
- When a function is expected to be asynchronous but has not been declared with the `async` keyword.
- When using `await` in callback functions that are not defined as `async`.

## Example Code
The following example demonstrates a scenario that would cause this error:
```javascript
function example() {
  const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Promise resolved");
    }, 2000);
  });

  // This will cause the SyntaxError because 'await' is used outside an async function
  const result = await promise;
  console.log(result);
}

example();
```
In this example, the `example` function is not declared as `async`, but it attempts to use `await` to wait for the promise to resolve.

## How to Fix
To fix this error, you need to declare the function that contains the `await` expression as `async`. Here's the corrected version of the previous example:
```javascript
async function example() {
  const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Promise resolved");
    }, 2000);
  });

  // Now, 'await' can be used because 'example' is declared as async
  const result = await promise;
  console.log(result);
}

example();
```
By adding the `async` keyword before the `example` function, we've made it an asynchronous function, allowing the use of `await` within it.

## Best Practices
To avoid this error in the future, follow these best practices:
- Always declare a function as `async` if it contains `await` expressions.
- Be mindful of the scope in which `await` is used. It must be directly within an `async` function.
- When working with promises, consider using `.then()` and `.catch()` for handling promise resolutions and rejections if you cannot use `async/await`.
- Keep your asynchronous code organized by ensuring that all asynchronous operations are properly wrapped in `async` functions.