# External Nginx Configuration Guide

Based on your `docker-compose.yml` and Django settings (`production.py`, `base.py`), here is an analysis and a complete guide to configuring an external (host OS) Nginx server. 

## 1. Analysis of Current Setup

Your Django project is well-configured, but a few things stand out when setting up an external Nginx proxy:
1. **Security / Port Binding:** Your Gunicorn `web` container binds `8000:8000` to `0.0.0.0` (all interfaces). This allows anyone to bypass Nginx and access Gunicorn directly via your server's IP. *(Fixed in your `docker-compose.yml`)*
2. **Static/Media Files:** You are using Docker named volumes (`static_volume` and `media_volume`). If Nginx runs outside of Docker directly on the host, it cannot easily access those volumes. *(Fixed by using `./staticfiles` and `./media` bind mounts in your `docker-compose.yml`)*
3. **WhiteNoise Middleware:** `production.py` includes `whitenoise.middleware.WhiteNoiseMiddleware`. WhiteNoise is great for letting Gunicorn serve static files. However, it **does not** serve media (user-uploaded) files! Therefore, Nginx *must* be configured to serve media files, and while WhiteNoise can serve static files, it is still slightly faster to let Nginx serve both directly.
4. **Django `MEDIA_URL`:** In `base.py`, you had `MEDIA_URL = ""`. This represents a problematic setting because media file URLs won't have a distinct prefix (like `/media/`). This makes it very hard to tell Nginx how to route media requests versus normal Django pages. *(Fixed in `settings/base.py` by making it `"/media/"`)*

## 2. Nginx Configuration

Create a new Nginx configuration file. Usually, this goes in `/etc/nginx/sites-available/kkc`.

Here is the best-practice setup for your `kkc.kg` domain:

```nginx
server {
    listen 80;
    server_name kkc.kg www.kkc.kg;

    # Ignore favicon errors
    location = /favicon.ico { access_log off; log_not_found off; }

    # Serve static files directly through Nginx (bypassing WhiteNoise for speed)
    location /static/ {
        # IMPORTANT: Replace with the actual absolute path to your project on the host OS
        alias /path/to/your/project/Korean_Kollege_1/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, max-age=2592000";
    }

    # Serve media files directly through Nginx (since WhiteNoise doesn't serve media)
    location /media/ {
        # IMPORTANT: Replace with the actual absolute path to your project on the host OS
        alias /path/to/your/project/Korean_Kollege_1/media/;
        expires 30d;
    }

    # Proxy all dynamic requests to Gunicorn inside the Docker container
    location / {
        proxy_pass http://127.0.0.1:8000;
        
        # Best-practice Proxy Headers so Django knows the real client IP & Protocol
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        proxy_redirect off;
    }
}
```

### Steps to enable on the server (Linux):
1. Save the file: `sudo nano /etc/nginx/sites-available/kkc`
2. Enable it: `sudo ln -s /etc/nginx/sites-available/kkc /etc/nginx/sites-enabled/`
3. Test config syntax: `sudo nginx -t`
4. Reload Nginx: `sudo systemctl reload nginx`

## 3. Securing Your Site with a Free SSL Certificate (Let's Encrypt / Certbot)

Securing your site with HTTPS is effectively mandatory in production for protecting user data and securing admin sessions. Let's Encrypt provides free, auto-renewing SSL certificates via a tool called **Certbot**, which seamlessly integrates into Nginx. 

Once your standard HTTP Nginx setup above is confirmed working:

1. **Install Certbot & Nginx plugin**: 
   ```bash
   sudo apt update
   sudo apt install certbot python3-certbot-nginx
   ```
2. **Obtain and Install the Certificate**: Let Certbot modify your configuration to turn on HTTPS. It automatically provisions the cert, sets up port 443 with modern TLS protocols, and adds a port 80-to-443 redirect.
   ```bash
   sudo certbot --nginx -d kkc.kg -d www.kkc.kg
   ```
3. **Verify Auto-Renewal**: Let's Encrypt certificates expire every 90 days, but Certbot installs a background task (cron or systemd timer) to renew them automatically before they expire. You can test that the automatic renewal works using:
   ```bash
   sudo certbot renew --dry-run
   ```
Once Certbot finishes its job, requests to `http://kkc.kg` will redirect automatically to `https://kkc.kg`. It perfectly interoperates with Django, as the `X-Forwarded-Proto` header configured in Nginx ensures Gunicorn understands the incoming connection was secure!

## 4. Final Checklist

- **Host Permissions:** Nginx (running as user `www-data` or `nginx`) MUST have read access to your `/staticfiles` and `/media` folders on the host machine. You might need to adjust permissions so they are world-readable, e.g.:
  ```bash
  chmod -R o+rx /path/to/your/project/Korean_Kollege_1/staticfiles
  chmod -R o+rx /path/to/your/project/Korean_Kollege_1/media
  ```
- Make sure to rebuild/restart your containers after the `docker-compose.yml` changes:
  ```bash
  docker compose down
  docker compose up -d --build
  ```
