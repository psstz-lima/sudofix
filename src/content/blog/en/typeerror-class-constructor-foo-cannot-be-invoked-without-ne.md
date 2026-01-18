---
title: "Fix TypeError: class constructor Foo cannot b..."
description: "Learn how to resolve the TypeError in JavaScript. Classes must be instantiated with 'new'...."
pubDate: "2026-01-17"
tags: ["javascript", "typeerror", "debugging"]
---

## The Error
The `TypeError: class constructor Foo cannot be invoked without 'new'` error occurs when a class constructor is called as a regular function, without using the `new` keyword. This error is thrown because classes in JavaScript are designed to be instantiated with the `new` operator, which creates a new instance of the class.

## Why it occurs
This error typically occurs when a developer forgets to use the `new` keyword when creating a new instance of a class, or when they are used to working with functions and try to call a class constructor in the same way. It can also happen when trying to invoke a class constructor as a function, without understanding the implications of using classes in JavaScript.

## Example Code
The following example demonstrates how this error can occur:
```javascript
class Foo {
  constructor(name) {
    this.name = name;
  }
}

// Incorrect usage: calling the class constructor as a function
Foo('John'); // TypeError: class constructor Foo cannot be invoked without 'new'

// Incorrect usage: assigning the class constructor to a variable and calling it
const Bar = Foo;
Bar('John'); // TypeError: class constructor Foo cannot be invoked without 'new'

// Correct usage: using the new keyword to instantiate the class
const foo = new Foo('John');
console.log(foo.name); // John
```
In this example, calling `Foo('John')` directly or assigning `Foo` to a variable `Bar` and then calling `Bar('John')` will both result in the `TypeError`.

## How to Fix
To fix this error, you need to use the `new` keyword when creating a new instance of a class. Here's a step-by-step solution:

1. Identify the line of code where the error is occurring.
2. Check if the class constructor is being called as a function, without the `new` keyword.
3. Add the `new` keyword before the class constructor call.
4. Verify that the class is being instantiated correctly and that the `new` keyword is being used correctly.

Using the example from above, the corrected code would be:
```javascript
const foo = new Foo('John');
console.log(foo.name); // John
```
By adding the `new` keyword, we ensure that the class constructor is called correctly and a new instance of the class is created.

## Best Practices
To avoid this error in the future, follow these best practices:

* Always use the `new` keyword when creating a new instance of a class.
* Be aware of the differences between classes and functions in JavaScript.
* Use a linter or code analysis tool to detect potential errors and enforce coding standards.
* Use a consistent coding style throughout your codebase to make it easier to identify and fix errors.
* When working with classes, make sure to understand the implications of using the `new` keyword and how it affects the creation of new instances.