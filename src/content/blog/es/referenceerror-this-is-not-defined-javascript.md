---
title: "Fix ReferenceError: this is not defined..."
description: "Learn how to resolve the ReferenceError in JavaScript. Accessing 'this' in a context where it's undefined..."
pubDate: "2026-01-17"
tags: ["javascript", "referenceerror", "debugging"]
---

## The Error
The `ReferenceError: this is not defined` error occurs when the JavaScript interpreter encounters a reference to `this` in a context where it is undefined. In JavaScript, `this` is a keyword that refers to the current execution context of a function. However, in certain situations, such as in strict mode or when using arrow functions, `this` can be undefined, leading to this error.

## Why it occurs
This error commonly occurs in the following scenarios:
* In strict mode, where `this` is not bound to the global object (`window` or `global`) by default.
* When using arrow functions, which do not have their own `this` binding and instead inherit the `this` context from their surrounding scope.
* When a function is called without a specific `this` context, such as when using the `setTimeout` or `setInterval` functions.

## Example Code
The following code example demonstrates how this error can occur:
```javascript
'use strict';

function outer() {
  console.log(this); // refers to the global object in non-strict mode, but undefined in strict mode

  function inner() {
    console.log(this); // refers to the global object in non-strict mode, but undefined in strict mode
  }

  inner();
}

outer();
```
In this example, the `outer` and `inner` functions are defined in strict mode. When `inner` is called, `this` is undefined, resulting in the `ReferenceError`.

Another example using arrow functions:
```javascript
const obj = {
  foo: () => {
    console.log(this); // undefined, because arrow functions do not have their own this binding
  }
};

obj.foo();
```
In this case, the `foo` function is an arrow function, which means it does not have its own `this` binding. When `foo` is called, `this` is undefined, resulting in the `ReferenceError`.

## How to Fix
To fix this error, you need to ensure that `this` is defined in the context where it is being used. Here are the step-by-step solutions:
* For functions defined in strict mode, you can bind `this` explicitly using the `bind` method or by using an arrow function.
* For arrow functions, you can use the surrounding scope's `this` context or define the function as a traditional function expression.
* When using `setTimeout` or `setInterval`, you can pass the `this` context as the second argument to the function.

Example solutions:
```javascript
// Using bind to define this context
function outer() {
  console.log(this);

  function inner() {
    console.log(this);
  }

  inner.bind(this)(); // bind this context to inner function
}

outer.call({ foo: 'bar' }); // define this context for outer function

// Using arrow functions
const obj = {
  foo: function() { // define as traditional function expression
    console.log(this);
  }
};

obj.foo();

// Using setTimeout with this context
setTimeout(function() {
  console.log(this);
}.bind({ foo: 'bar' }), 1000); // pass this context to setTimeout
```
## Best Practices
To avoid this error in the future, follow these best practices:
* Always define the `this` context explicitly when using functions in strict mode.
* Use traditional function expressions instead of arrow functions when you need to access `this`.
* Pass the `this` context as an argument when using `setTimeout` or `setInterval`.
* Use a linter or code analysis tool to detect potential `this` context issues in your code.
* Keep your code organized and modular to minimize the complexity of your `this` context.