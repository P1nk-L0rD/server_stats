# Server_stats

Simple project to get basic system stats of your server via FastAPI.

Based on psutil, fastapi, pydantic.

## Request example

```python
import requests

headers = {"token": "your_secret_token"}
answer = requests.get("domain.com/server_stats/", headers=headers)
print(answer)
```

## Answer example

```json
{
  "cpu_cores": 8,
  "cpu_current_usage": 16.2,
  "cpu_average_usage": 18.9,
  "memory_total": 928375423,
  "memory_percent_usage": 14.1,
  "disc_total": 92837542398,
  "disc_percent_usage": 13.6,
  "current_network_usage": 98324,
  "boot_time": 1725877431
}
```

# DEPLOYMENT

## Installing via docker (recommended)

```bash
git clone https://github.com/P1nk-L0rD/server_stats.git
cd server_stats
echo "SERVER_STATS_TOKEN=TOKEN" > .env
docker-compose up -d
```

## Installing via commands

```bash
git clone https://github.com/P1nk-L0rD/server_stats.git
```

Download python 3.10 env:

```bash
apt install python3.10-venv -y
```

Create and activate venv:

```bash
cd server_stats/
python3.10 -m venv venv
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

Create .env with SERVER_STATS_TOKEN

```bash
touch .env
vim .env
```

!!! Important: If you do not create .env, stats will be available without a token.

## Daemon

Create daemon:

```bash
sudo vim /etc/systemd/system/server_stats.service
```

Copy daemon.txt to created file. Save it and exit.

Reload daemon service:

```bash
sudo systemctl daemon-reload
```

Enable and start daemon:

```bash
sudo systemctl enable server_stats.service
sudo systemctl start server_stats.service
```

## NGINX

Add code to your nginx default (/etc/nginx/sites-enabled/default):

```nginx
location /server_stats/ {
  proxy_pass http://127.0.0.1:8110;
}
```

Full nginx default may look like this:

```nginx
server {
  listen 443;
  server_name domain.com;

  ssl_certificate      /etc/letsencrypt/live/domain.com/fullchain.pem;
  ssl_certificate_key  /etc/letsencrypt/live/domain.com/privkey.pem;

  location /server_stats/ {
    proxy_pass http://127.0.0.1:8110;
  }
}

```

Restart nginx:

```bash
systemctl reload nginx
```

### Ready

## Extra

To update server:

```bash
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y
```

To update server_stats:

```bash
cd server_stats/
git pull
systemctl restart server_stats
```

To use without nginx, via port replace 127.0.0.1 -> 0.0.0.0 in daemon.
