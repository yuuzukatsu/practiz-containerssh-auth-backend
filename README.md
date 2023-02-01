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
Sample User : yzk
Sample Password : coba
Image Used : yuuzukatsu/coba:node (Built from image node:latest)
```
ssh yzk@server-ip -p 2222
```
