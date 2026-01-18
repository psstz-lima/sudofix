---
title: "Fix TypeError: super constructor may only be ..."
description: "Learn how to resolve the TypeError in JavaScript. Subclass constructor called super() multiple times..."
pubDate: "2026-01-17"
tags: ["javascript", "typeerror", "debugging"]
---

## The Error
The `TypeError: super constructor may only be called once` error occurs when a subclass constructor calls the `super()` method more than once. This error is raised because the `super()` method is used to call the constructor of the parent class, and it can only be called once in a subclass constructor.

In JavaScript, when a subclass constructor is called, it must call the `super()` method to initialize the parent class. If `super()` is called multiple times, it can lead to unexpected behavior and errors, as the parent class's constructor is executed multiple times.

## Why it occurs
This error commonly occurs when a subclass constructor calls `super()` multiple times, either directly or indirectly, through other methods or conditional statements. It can also occur when a subclass constructor calls `super()` after the `this` keyword has been used, which can lead to the `super()` method being called multiple times.

Another common cause is when a subclass constructor is called recursively, either directly or indirectly, through other methods or functions. This can lead to the `super()` method being called multiple times, resulting in the error.

## Example Code
The following example demonstrates a subclass constructor that calls `super()` multiple times:
```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);
    if (breed) {
      super(name); // Error: super constructor may only be called once
    }
    this.breed = breed;
  }
}

const myDog = new Dog('Fido', 'Golden Retriever');
```
In this example, the `Dog` subclass constructor calls `super()` twice, once directly and once conditionally. This results in the `TypeError: super constructor may only be called once` error.

## How to Fix
To fix this error, you need to ensure that the `super()` method is only called once in the subclass constructor. Here's the corrected code:
```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name); // Call super() only once
    this.breed = breed;
  }
}

const myDog = new Dog('Fido', 'Golden Retriever');
```
In this corrected version, the `super()` method is only called once, and the `breed` property is assigned after the `super()` call.

## Best Practices
To avoid this error in the future, follow these best practices:

* Always call `super()` only once in a subclass constructor.
* Avoid calling `super()` conditionally or recursively.
* Use the `this` keyword only after the `super()` method has been called.
* Use a linter or code analyzer to detect and prevent this error.
* Test your code thoroughly to ensure that the `super()` method is called correctly.

By following these best practices and understanding the causes of the `TypeError: super constructor may only be called once` error, you can write more robust and error-free JavaScript code.