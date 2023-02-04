FROM python:alpine
WORKDIR /app
COPY main.py main.py
RUN pip install --no-cache-dir flask
CMD ['python3', 'main.py']