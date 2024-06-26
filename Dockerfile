FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 53535/udp

CMD ["python", "dns_tls_proxy.py"]
