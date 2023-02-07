1. Run Docker Compose
```
docker compose -f docker-compose.yaml up -d
```

2. Install python3 and pip
```
apt install python3 python3-pip
```

3. Install flask
```
pip install flask
```

4. Run Auth Server
```
python3 main.py
```

5. SSH to port 2222

```
Sample User : node
Sample Password : coba
Image Used : yuuzukatsu/coba:node (Built from image node:latest)
```
```
Sample User : nix
Sample Password : coba
Image Used : yuuzukatsu/coba:nix (Built from image nix:latest)
```
```
Sample User : ubuntu
Sample Password : coba
Image Used : yuuzukatsu/coba:ubuntu (Built from image ubuntu:latest)
```
```
Sample User : docker
Sample Password : coba
Image Used : yuuzukatsu/coba:dind (Built from image docker:dind)
```

```
ssh user@server-ip -p 2222
```
