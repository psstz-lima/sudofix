---
title: "Fix SyntaxError: Rest parameter must be last fo..."
description: "Learn how to resolve the SyntaxError in JavaScript. Spread operator (...) must be at the end of functi..."
pubDate: "2026-01-17"
tags: ["javascript", "syntaxerror", "debugging"]
---

## The Error
The `SyntaxError` with the message "Rest parameter must be last formal parameter" is a JavaScript error that occurs when the spread operator (`...`) is used in a function parameter list, but not as the last parameter. This error is raised because the JavaScript language specification dictates that rest parameters, which are denoted by the spread operator (`...`), must be the last formal parameter in a function's parameter list.

## Why it occurs
This error commonly occurs when developers attempt to use the spread operator to collect the rest of the arguments in a function, but place it before other parameters. The spread operator is used to gather the "rest" of the arguments into an array, but JavaScript's syntax rules require it to be at the end of the parameter list. This is a deliberate design choice to maintain clarity and simplicity in function signatures.

## Example Code
The following example illustrates code that would cause this error:
```javascript
function exampleFunc(...args, param1, param2) {
  console.log(args);
  console.log(param1);
  console.log(param2);
}
```
In this example, `...args` is used before `param1` and `param2`, which is not allowed according to JavaScript's syntax rules.

## How to Fix
To fix this error, you need to ensure that the rest parameter (`...args`) is the last formal parameter in the function's parameter list. Here's the corrected version of the example code:
```javascript
function exampleFunc(param1, param2, ...args) {
  console.log(args);
  console.log(param1);
  console.log(param2);
}
```
By moving `...args` to the end, we comply with JavaScript's requirement that rest parameters must be the last formal parameter, thus resolving the `SyntaxError`.

## Best Practices
To avoid this error in the future:
- Always place the spread operator (`...`) at the end of the parameter list when defining functions.
- Be mindful of the order of parameters; if you need to use a rest parameter, ensure it is the last one.
- Keep your function signatures clear and simple. If a function requires a large number of parameters, consider using an options object instead, which can make your code more readable and maintainable.
- Familiarize yourself with JavaScript's syntax rules and best practices to write more robust and compliant code.