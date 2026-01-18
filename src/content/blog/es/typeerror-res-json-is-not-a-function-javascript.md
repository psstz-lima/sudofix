---
title: "Fix TypeError: res.json is not a function..."
description: "Learn how to resolve the TypeError in JavaScript. Response object doesn't have .json(). Check if usi..."
pubDate: "2026-01-17"
tags: ["javascript", "typeerror", "debugging"]
---

## The Error
The error `TypeError: res.json is not a function` indicates that the `res` object, which is typically an instance of the HTTP response object in a Node.js web application, does not have a `json()` method. This method is commonly used to send a JSON response back to the client. The absence of this method suggests that the `res` object is not what the developer expects it to be, or it has been modified in a way that removes or overrides the `json()` method.

## Why it occurs
This error commonly occurs in the context of Express.js or similar frameworks where the `res` object is expected to have certain methods like `json()`, `send()`, `render()`, etc. The error can arise due to several reasons:
- The response object has been overwritten or modified inadvertently.
- The middleware or the route handler function is not properly defined or is not correctly using the response object.
- There's a mismatch between the expected and actual types of the response object, possibly due to incorrect usage of async/await or callbacks.

## Example Code
Consider the following example where we might inadvertently cause this error:
```javascript
const express = require('express');
const app = express();

app.get('/example', (req, res) => {
    // Simulating an error by overwriting the res object
    res = {};
    try {
        res.json({ message: 'Hello, World!' }); // This will throw the TypeError
    } catch (error) {
        console.error(error);
    }
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
```
In this example, overwriting the `res` object with an empty object (`{}`) removes all its methods, including `json()`, leading to the `TypeError`.

## How to Fix
To fix this issue, ensure that the `res` object is not modified and that you are using the correct response object provided by the framework (e.g., Express.js). Here’s a step-by-step solution:
1. **Verify Middleware**: Make sure all middleware functions are properly defined and are not accidentally overwriting the `res` object.
2. **Check Route Handlers**: Ensure that route handler functions are correctly using the `res` object without modifying it in a way that would remove its methods.
3. **Use Async/Await Correctly**: If using async/await, verify that the `res` object is accessed within the correct scope and not after it has been potentially modified or goes out of scope.
4. **Inspect the res Object**: Before calling `res.json()`, inspect the `res` object to see if it indeed has the `json` method. This can be done using `console.log(res)` or a debugger.

Corrected example:
```javascript
const express = require('express');
const app = express();

app.get('/example', (req, res) => {
    // Ensure res is not modified
    try {
        res.json({ message: 'Hello, World!' });
    } catch (error) {
        console.error(error);
    }
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
```

## Best Practices
To avoid this error in the future:
- **Be Mindful of Scope**: Ensure that the `res` object is accessed within the correct scope.
- **Avoid Overwriting**: Never intentionally overwrite the `res` object or its methods within your route handlers or middleware.
- **Use Logging and Debugging**: Regularly use logging and debugging tools to inspect objects and variables, especially when encountering unexpected errors.
- **Follow Framework Documentation**: Adhere to the documentation and guidelines of the framework you are using (e.g., Express.js) for handling requests and responses.