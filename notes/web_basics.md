# Web Basics – HTTP & URLs

## Overview

Web communication is primarily handled using **HTTP (HyperText Transfer Protocol)**.

It defines how browsers and servers communicate.

---

# HTTP (HyperText Transfer Protocol)

## Definition
HTTP is a set of rules that allows a **client (browser)** to communicate with a **server**.

---

## How It Works

1. User opens a website  
2. Browser sends an HTTP request  
3. Server processes the request  
4. Server sends an HTTP response  
5. Browser renders the page  

---

## Where HTTP Fits (OSI Model)

- **Application Layer** → HTTP operates here  
- **Transport Layer** → uses TCP  
- **Network Layer** → uses IP  
- **Data Link Layer** → uses MAC addresses  

---

## Role of TCP in HTTP

TCP ensures reliable communication by:
- Breaking data into segments
- Adding port numbers
- Ensuring ordered delivery
- Handling retransmission if needed

---

# HTTP Requests

## Definition
An HTTP request is sent by the browser to the server.

---

## Key Components

### Method
Defines what action to perform:

- GET → retrieve data  
- POST → send data  
- PUT → update data  
- DELETE → remove data  

---

### URL
Specifies where the request is sent.

---

### Headers
Provide extra information:
- Browser type
- Content type
- Authentication data

---

### Body (Optional)
- Contains data being sent (e.g. form input)

---

# HTTP Responses

## Definition
Sent by the server back to the client.

---

## Key Components

### Status Code
Indicates result of the request

### Headers
Metadata about the response

### Body
Actual content:
- HTML
- JSON
- Images

---

# HTTP Status Codes

## 2xx – Success
- 200 OK → request successful  
- 201 Created → resource created  

---

## 3xx – Redirection
- 301 Moved Permanently  
- 302 Found (temporary redirect)  

---

## 4xx – Client Errors
- 400 Bad Request  
- 401 Unauthorized  
- 403 Forbidden  
- 404 Not Found  

---

## 5xx – Server Errors
- 500 Internal Server Error  
- 502 Bad Gateway  
- 503 Service Unavailable  

---

# URLs (Uniform Resource Locators)

## Definition
A URL is the address of a resource on the internet.

---

## Example
https://www.example.com:443/path/page?name=alex#section1

---

## Breakdown

- **Protocol** → `https://`  
  - Defines how communication happens  

- **Domain** → `www.example.com`  
  - The server address  

- **Port** → `:443`  
  - Default for HTTPS  

- **Path** → `/path/page`  
  - Specific resource  

- **Query String** → `?name=alex`  
  - Extra data sent to server  

- **Fragment** → `#section1`  
  - Section within the page  

---

# Full Request Flow

1. User enters URL  
2. Browser sends HTTP request  
3. Server processes request  
4. Server sends HTTP response  
5. Browser renders content  

---

# Key Takeaways

- HTTP enables communication between browsers and servers  
- Requests and responses form the core of web communication  
- TCP ensures reliable delivery of HTTP data  
- URLs define where and how requests are sent  
