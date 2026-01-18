---
title: "Fix SyntaxError: JSON.parse('{a:1}')..."
description: "Learn how to resolve the SyntaxError in JavaScript. Unexpected token. Keys in JSON must be double-quot..."
pubDate: "2026-01-17"
tags: ["javascript", "syntaxerror", "debugging"]
---

# Understanding and Resolving SyntaxError in JSON.parse

## The Error

The `SyntaxError` encountered when executing `JSON.parse('{a:1}')` indicates that there is an issue with the syntax of the JSON string being parsed. In this context, the error message specifically points out an "Unexpected token," which typically means that the parser encountered a character it did not expect based on the JSON format standards.

## Why it occurs

This error occurs because the JSON format enforces strict syntax rules, where keys must be enclosed in double quotes. The provided string `'{a:1}'` violates this rule, as the key `a` is not quoted. As a result, the JSON parser cannot correctly interpret the input string and throws a `SyntaxError`.

Common causes of this error include:

1. **Incorrectly formatted JSON**: Developers may forget to quote keys or use single quotes instead of double quotes.
2. **Dynamic string generation**: When constructing JSON strings dynamically, it’s easy to miss the quotation marks around keys.
3. **Copying and pasting data**: Data copied from other formats (like JavaScript objects) might not adhere to JSON syntax.

## Example Code

Here’s an example that triggers the `SyntaxError`:

```javascript
try {
    const jsonString = '{a:1}'; // Incorrect JSON format
    const jsonObject = JSON.parse(jsonString); // This line throws a SyntaxError
    console.log(jsonObject);
} catch (error) {
    console.error(error); // Logs: SyntaxError: Unexpected token a in JSON at position 1
}
```

In this code, the JSON string `'{a:1}'` is invalid due to the unquoted key `a`, which leads to the `SyntaxError` when attempting to parse.

## How to Fix

To resolve the `SyntaxError`, you need to ensure that all keys in your JSON strings are double-quoted. Here’s a step-by-step solution:

1. **Identify the error**: Recognize that the key `a` is not correctly formatted.
   
2. **Modify the JSON string**: Update the JSON string to follow the correct syntax by enclosing the key in double quotes.

   Change:
   ```javascript
   const jsonString = '{a:1}'; // Incorrect
   ```
   To:
   ```javascript
   const jsonString = '{"a":1}'; // Correct
   ```

3. **Re-run the code**: After making the changes, re-run the parsing code.

Here’s the corrected version:

```javascript
try {
    const jsonString = '{"a":1}'; // Correct JSON format
    const jsonObject = JSON.parse(jsonString); // Now this works without error
    console.log(jsonObject); // Logs: { a: 1 }
} catch (error) {
    console.error(error);
}
```

## Best Practices

To avoid encountering this `SyntaxError` in the future, consider the following best practices:

1. **Always use double quotes for keys**: When writing JSON, remember that keys must be enclosed in double quotes, e.g., `{"key": "value"}`.

2. **Validate JSON strings**: Use tools or libraries (like JSONLint) to validate your JSON strings before parsing them. This can help catch syntax errors early.

3. **Use JSON methods for object manipulation**: Instead of manually constructing JSON strings, consider using JavaScript objects and then converting them to JSON using `JSON.stringify()`. This ensures proper formatting.

   Example:
   ```javascript
   const obj = { a: 1 }; // Valid JavaScript object
   const jsonString = JSON.stringify(obj); // Converts to valid JSON string: '{"a":1}'
   ```

4. **Be cautious with dynamic JSON generation**: When building JSON strings dynamically, implement safeguards to ensure that keys are properly quoted.

By adhering to these practices, you can minimize the risk of encountering `SyntaxError` in your JSON parsing endeavors.