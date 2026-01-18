---
title: "Fix TypeError: obj is not iterable..."
description: "Learn how to resolve the TypeError in JavaScript. The object is not iterable (cannot use for...of). ..."
pubDate: "2026-01-17"
tags: ["javascript", "typeerror", "debugging"]
---

# The Error: TypeError: obj is not iterable

The `TypeError: obj is not iterable` occurs when an attempt is made to iterate over an object that does not implement the iterable protocol. In JavaScript, the iterable protocol allows objects to be iterated using constructs like `for...of` loops or spread syntax. An object must implement the `Symbol.iterator` method to be considered iterable.

# Why it occurs

This error commonly arises in the following situations:

1. **Using Non-iterable Objects**: Attempting to use `for...of` on objects that are not inherently iterable, such as plain objects, numbers, or `undefined`.
   
2. **Improperly Defined Iterators**: Objects that are expected to be iterable may not have the necessary `Symbol.iterator` method defined.

3. **Handling Non-Array Values**: When a function expects an array or a string but receives a different type, this error can surface.

# Example Code

Consider the following code snippet that causes the `TypeError: obj is not iterable`:

```javascript
const obj = { key1: 'value1', key2: 'value2' };

try {
    for (const value of obj) {
        console.log(value);
    }
} catch (error) {
    console.error(error); // TypeError: obj is not iterable
}
```

In this example, the `obj` is a plain object, which cannot be iterated over as it does not implement the iterable protocol. 

Another example could involve attempting to spread a non-iterable object:

```javascript
const nonIterable = { name: 'John', age: 30 };

const newArray = [...nonIterable]; // TypeError: nonIterable is not iterable
```

# How to Fix

To resolve this error, follow these steps:

1. **Identify the Object Type**: Determine if the object you are trying to iterate over is indeed iterable. Common iterables include Arrays, Strings, Maps, and Sets.

2. **Use the Correct Structure**: If you intended to iterate over the properties of an object, consider using `Object.keys()`, `Object.values()`, or `Object.entries()` which return arrays of the object's keys, values, or entries. 

Here’s how to modify the previous `for...of` example:

```javascript
const obj = { key1: 'value1', key2: 'value2' };

for (const key of Object.keys(obj)) {
    console.log(key); // Outputs: key1, key2
}
```

3. **Implement the Iterator Protocol**: If you are creating a custom object that you want to be iterable, define the `Symbol.iterator` method.

```javascript
const iterableObject = {
    items: ['item1', 'item2', 'item3'],
    [Symbol.iterator]: function* () {
        for (const item of this.items) {
            yield item;
        }
    }
};

for (const item of iterableObject) {
    console.log(item); // Outputs: item1, item2, item3
}
```

# Best Practices

To prevent encountering the `TypeError: obj is not iterable` in the future, consider the following best practices:

1. **Check Object Types Before Iteration**: Always confirm that the object you are attempting to iterate over is of a type that supports iteration (e.g., Array, String, etc.).

2. **Utilize Type Checking**: Use `Array.isArray()` or `typeof` to validate the type of the object. This can help prevent runtime errors.

3. **Leverage Destructuring and Spread Syntax Carefully**: Be cautious when using destructuring or the spread operator, ensuring the target is iterable.

4. **Implement Custom Iterators When Necessary**: If you create custom objects, make sure to implement the iterator protocol if they are intended to be used in iterative contexts.

By following these guidelines, you can avoid the `TypeError: obj is not iterable` and write more robust, error-free JavaScript code.