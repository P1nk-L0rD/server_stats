# Server_stats

Simple project to get basic system stats of your server via FastAPI.
Based on psutil, fastapi, pydantic.

## Request example:
```python
import requests

headers = {"token": "your_secret_token"}
answer = requests.get("domain.com/server_stats", headers=headers)
print(answer)
```

## Answer example:
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

```bash
git clone git@github.com:P1nk-L0rD/server_stats.git
```

Create daemon:
```bash
sudo vim /etc/systemd/system/server_stats.service
```

Reload daemon service:
```bash
sudo systemctl daemon-reload
```

Enable and start daemon:
```bash
sudo systemctl enable server_stats.service
sudo systemctl start server_stats.service
```

Add code to your nginx default:
```nginx
location /server_stats/ {
  proxy_redirect off;
  proxy_pass http://127.0.0.1:8110;
  proxy_set_header Host $host;
}
```

Ready!
