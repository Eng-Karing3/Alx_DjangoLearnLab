# Deployment Configuration for HTTPS

## 1. SSL Certificate

To serve the Django app securely over HTTPS, ensure your server has a valid SSL/TLS certificate. Use either:

- **Let's Encrypt (Free)**: Via Certbot
- **Commercial CA**: From providers like DigiCert, GoDaddy, etc.

## 2. Nginx Configuration Example

Here’s a basic HTTPS configuration snippet for Nginx:

```nginx
server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/ssl/certs/your_cert.pem;
    ssl_certificate_key /etc/ssl/private/your_key.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$host$request_uri;
}
