# OpenReason Protocol Documentation Site

Built with [Nextra](https://nextra.site/) - a Next.js-based documentation framework.

## Development

```bash
npm install
npm run dev
```

Site runs at http://localhost:3000

## Building

```bash
npm run build
```

Static files are generated in `out/` directory.

## Deployment Options

### Option 1: Docker (Recommended for DigitalOcean)

Build and run:
```bash
docker build -t orp-docs .
docker run -d --name orp-docs -p 8080:80 --restart unless-stopped orp-docs
```

The site will be available at http://localhost:8080

### Option 2: GitLab Pages

Add to `.gitlab-ci.yml`:
```yaml
pages:
  stage: deploy
  image: node:18
  script:
    - cd docs-site
    - npm ci
    - npm run build
    - mv out ../public
  artifacts:
    paths:
      - public
  only:
    - main
```

### Option 3: Nginx (Static Files)

After building:
```bash
npm run build
cp -r out/* /var/www/publicreasonproject.org/
```

Nginx config:
```nginx
server {
    listen 80;
    server_name publicreasonproject.org;
    root /var/www/publicreasonproject.org;
    index index.html;
    
    location / {
        try_files $uri $uri.html $uri/ /404.html;
    }
}
```

## Deployment on DigitalOcean (alongside API)

### Prerequisites
- Docker installed on server
- DNS configured: publicreasonproject.org → your server IP

### Steps

1. **SSH into server:**
```bash
ssh root@your-server-ip
```

2. **Upload and extract docs:**
```bash
cd /opt
tar xzf orp-docs.tar.gz
cd orp-docs
```

3. **Build Docker image:**
```bash
docker build -t orp-docs .
```

4. **Run container:**
```bash
docker run -d \
  --name orp-docs \
  -p 8080:80 \
  --restart unless-stopped \
  orp-docs
```

5. **Configure nginx reverse proxy:**
```nginx
# /etc/nginx/sites-available/orp-docs
server {
    listen 80;
    server_name publicreasonproject.org;
    
    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

6. **Enable site and get SSL:**
```bash
ln -s /etc/nginx/sites-available/orp-docs /etc/nginx/sites-enabled/
nginx -t && systemctl reload nginx
certbot --nginx -d publicreasonproject.org
```

7. **Verify:**
```bash
curl -I https://publicreasonproject.org
```

### Updating the site

```bash
cd /opt/orp-docs
git pull origin main
docker stop orp-docs
docker rm orp-docs
docker build -t orp-docs .
docker run -d --name orp-docs -p 8080:80 --restart unless-stopped orp-docs
```

## Structure

```
docs-site/
├── pages/           # Documentation pages (MDX)
│   ├── index.mdx    # Home page
│   ├── getting-started/
│   ├── protocol/
│   ├── tools/
│   ├── examples/
│   └── community/
├── styles/          # Global CSS
├── public/          # Static assets
├── theme.config.tsx # Nextra theme config
└── next.config.mjs  # Next.js config
```

## Adding Content

1. Create `.mdx` files in `pages/`
2. Add navigation in `_meta.js` files
3. Use MDX for rich content (React components in Markdown)

Example:
```mdx
# Page Title

Regular markdown content.

<div className="orp-card">
  Custom component
</div>
```

## Tech Stack

- **Next.js 14** - React framework
- **Nextra 3** - Documentation framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Docker** - Containerization
- **Nginx** - Web server

## License

MIT
