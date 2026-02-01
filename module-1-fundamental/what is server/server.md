# Server — Definition

**Definition:**

A server is a computer program or a physical/virtual device that provides services, resources, or data to other programs or devices (clients) over a network. Servers listen for incoming requests, process those requests, and return responses or perform actions on behalf of clients.

**Key responsibilities:**

- Accept and manage network requests.
- Process requests and run application logic.
- Store, retrieve, and serve data.
- Enforce access control, logging, and security.

**Common types:**

- Web server (e.g., Nginx, Apache)
- Application server (e.g., Node.js, Tomcat)
- Database server (e.g., MySQL, PostgreSQL)
- File server, Mail server, DNS server

**Typical components:**

- Hardware or virtual machine / container
- Operating system and networking stack
- Server software (service/process)
- Storage, logging, and monitoring

**Example (simple HTTP server in Node.js):**

```js
const http = require('http');
const server = http.createServer((req, res) => {
	res.writeHead(200, {'Content-Type': 'text/plain'});
	res.end('Hello from server');
});
server.listen(3000, () => console.log('Server listening on port 3000'));
```

**Short summary:** A server provides services to clients over a network, handling requests and delivering responses or resources.

