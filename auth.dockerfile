FROM python:alpine
WORKDIR /app
COPY main.py main.py
RUN pip install --no-cache-dir flask
CMD ['python', 'main.py']