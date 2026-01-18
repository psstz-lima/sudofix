---
title: "Fix ReferenceError: document is not defined..."
description: "Learn how to resolve the ReferenceError in JavaScript. Accessing DOM 'document' in Node.js environment...."
pubDate: "2026-01-17"
tags: ["javascript", "referenceerror", "debugging"]
---

## The Error
The `ReferenceError: document is not defined` error occurs when the JavaScript interpreter encounters a reference to the `document` object, which is not defined in the current execution context. This error is a type of `ReferenceError`, which is thrown when the JavaScript engine cannot find a variable or property that is being referenced.

## Why it occurs
This error commonly occurs when trying to access the DOM (Document Object Model) `document` object in a Node.js environment. Node.js is a server-side runtime, and as such, it does not have a DOM. The `document` object is a part of the browser's DOM, and it is not available in Node.js. When you try to access `document` in a Node.js environment, the JavaScript engine cannot find it, resulting in a `ReferenceError`.

## Example Code
The following code will cause the `ReferenceError: document is not defined` error when run in a Node.js environment:
```javascript
// example.js
console.log(document); // ReferenceError: document is not defined
```
Similarly, trying to access any property or method of the `document` object will also result in an error:
```javascript
// example.js
console.log(document.body); // ReferenceError: document is not defined
document.addEventListener('DOMContentLoaded', () => {
  console.log('Document loaded');
}); // ReferenceError: document is not defined
```
## How to Fix
To fix this error, you need to ensure that you are not trying to access the `document` object in a Node.js environment. If you need to access the DOM, you should run your code in a browser environment. However, if you need to run your code in a Node.js environment, you can use a library like `jsdom` to simulate a browser environment.

Here are the steps to fix the error:

1. **Install jsdom**: Run the following command in your terminal to install `jsdom`:
```bash
npm install jsdom
```
2. **Require jsdom**: In your JavaScript file, require `jsdom` and create a new `JSDOM` instance:
```javascript
const jsdom = require('jsdom');
const { JSDOM } = jsdom;
const dom = new JSDOM(`<!DOCTYPE html><html><body></body></html>`);
const document = dom.window.document;
```
3. **Use the simulated document object**: You can now use the simulated `document` object to access the DOM:
```javascript
console.log(document.body); // Output: <body></body>
document.addEventListener('DOMContentLoaded', () => {
  console.log('Document loaded');
});
```
## Best Practices
To avoid this error in the future, follow these best practices:

* **Check your environment**: Before trying to access the `document` object, make sure you are running your code in a browser environment.
* **Use environment-specific code**: Use conditional statements to check the environment and run environment-specific code.
* **Use libraries like jsdom**: If you need to access the DOM in a Node.js environment, use a library like `jsdom` to simulate a browser environment.
* **Test your code**: Thoroughly test your code in different environments to ensure it works as expected.