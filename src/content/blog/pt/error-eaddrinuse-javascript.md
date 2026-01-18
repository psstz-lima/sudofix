---
title: "Fix Error: EADDRINUSE..."
description: "Learn how to resolve the Error in JavaScript. Port already in use. Kill the process using the po..."
pubDate: "2026-01-17"
tags: ["javascript", "error", "debugging"]
---

## The Error
The `EADDRINUSE` error in JavaScript is a system error that occurs when a process attempts to bind to a specific port that is already in use by another process. This error is typically encountered when working with network servers, such as HTTP or WebSocket servers, where a specific port is required to listen for incoming connections. The error message `Error: Error` with the context `EADDRINUSE` indicates that the port specified in the code is not available for use due to another process occupying it.

## Why it occurs
This error commonly occurs in the following scenarios:
- **Multiple server instances**: Running multiple instances of the same server or different servers that are configured to use the same port.
- **Previous server instance not terminated**: Failing to properly close a server instance, leaving the port occupied.
- **Other applications using the port**: Other applications or services on the system using the same port, either intentionally or unintentionally.
- **Configuration mistakes**: Incorrectly configuring the port in the server settings or environment variables.

## Example Code
The following is an example of a simple HTTP server in Node.js that might cause this error if another process is using port 3000:
```javascript
const http = require('http');

const port = 3000;

const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World\n');
});

server.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
```
If you attempt to run this server while another process is already using port 3000, you will encounter the `EADDRINUSE` error.

## How to Fix
To resolve the `EADDRINUSE` error, follow these steps:
1. **Identify the process using the port**: Use the command line to find out which process is using the port. On Unix-like systems (including macOS and Linux), you can use the `lsof` command:
   ```bash
   lsof -i :3000
   ```
   On Windows, you can use the `netstat` command:
   ```cmd
   netstat -aon | findstr :3000
   ```
   Note the PID (Process ID) of the process using the port.

2. **Kill the process**: Once you have identified the process, you can terminate it. On Unix-like systems, use the `kill` command:
   ```bash
   kill -9 <PID>
   ```
   Replace `<PID>` with the actual process ID. On Windows, you can use the Task Manager to end the process or use the `taskkill` command:
   ```cmd
   taskkill /F /PID <PID>
   ```
   Again, replace `<PID>` with the actual process ID.

3. **Change the port**: Alternatively, you can change the port your server is listening on. Modify the `port` variable in your server code to use an available port. For example:
   ```javascript
   const port = 3001;
   ```
   Ensure that the new port is not in use by another process.

## Best Practices
To avoid encountering the `EADDRINUSE` error in the future, follow these best practices:
- **Use a port management strategy**: Implement a strategy for managing ports across different projects and servers to avoid conflicts.
- **Automate server termination**: Ensure that servers are properly terminated when they are no longer needed to free up ports.
- **Monitor port usage**: Regularly monitor which ports are in use to quickly identify potential conflicts.
- **Consider using a dynamic port allocation**: For development environments, consider using a dynamic port allocation mechanism that automatically selects an available port, reducing the likelihood of port conflicts.