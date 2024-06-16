# n26-dns-tls-proxy

## Introduction

This project creates a proxy server that listens for regular DNS queries on port 53535 and forwards them over a secure TLS connection to a DNS-over-TLS server (Cloudflare). The proxy then sends the responses back to the client.

## About

The proxy is written in Python. It uses the `socket` module for network communication and `ssl` for encryption. The main script, `n26_dns_tls_proxy.py`, sets up a UDP server that listens for DNS queries and forwards them to Cloudflare's DNS-over-TLS server.

## Security

- **Data Encryption**: TLS certificates should be valid.
- **Access Control**: Only trusted clients should be allowed to access.
- **Logging**: Need to add logging.
- **Rate Limiting**: To Prevent DDoS Attack Rate Limiting should be implemented.

## Infrastructure Integration

- **Microservices Architecture**: Deploying the proxy as microservice and using Kubernetes the service can be managed and sclaed.
- **Load Balancing**: Use load balancers to distribute incoming DNS queries across multiple instances of the proxy service.

## Improvements

1. **Multi-threading**: The proxy already handles multiple requests using threading.
2. **Better Logging**: Detailed logging can be implemented.
3. **Config Management**: Use environment variables or config files to manage server settings.

## Running the Proxy

### Prerequisites

- Docker installation on local Machine.

### Building the Docker Image

1. Navigate to the project directory:
   ```sh
   cd n26_dns_tls_proxy
   ```
   2.Build the Docker image:
   ```sh
   docker build -t n26-dns-tls-proxy .
   ```

### Running the Docker Container

1. Run the Docker container:
   ```sh
   docker run -p 53535:53535/udp n26-dns-tls-proxy
   ```

### Testing the Proxy

```sh
dig @127.0.0.1 -p 53535 www.example.com
```

Alternative tools like nslookup, drill can also be used to test the proxy
