
---

## ✅ STEP 3: Write the Security Review

**File to create:**  
📄 `LibraryProject/security_review.md`

### Paste this content:

```markdown
# Security Review: Django HTTPS Configuration

## Configured Settings

- `SECURE_SSL_REDIRECT = True`: Enforces HTTPS, ensuring secure transmission.
- `SECURE_HSTS_SECONDS = 31536000`: Activates HSTS for one year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Ensures HSTS also applies to subdomains.
- `SECURE_HSTS_PRELOAD = True`: Enables HSTS preload inclusion in browsers.
- `SESSION_COOKIE_SECURE = True`: Secures session cookies.
- `CSRF_COOKIE_SECURE = True`: Secures CSRF protection cookies.
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking attacks.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Blocks MIME-type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables XSS filtering in modern browsers.

## Deployment Configuration

- HTTPS enabled using SSL via Nginx reverse proxy.
- HTTP requests are redirected to HTTPS.
- Certificates are securely stored and regularly renewed.

## Potential Improvements

- Implement **Content Security Policy (CSP)** headers.
- Set `SECURE_REFERRER_POLICY`.
- Use tools like [Mozilla Observatory](https://observatory.mozilla.org/) or [SecurityHeaders.com](https://securityheaders.com/) for further security audits.
