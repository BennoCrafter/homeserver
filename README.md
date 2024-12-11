# homeserver
A self-hosted web server running personal websites and applications.

```bash
docker build -t homeserver .
```

```bash
docker run -d --restart unless-stopped -p 8000:8000 homeserver
```
