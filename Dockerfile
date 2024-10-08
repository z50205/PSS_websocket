FROM python:3.8.2-alpine

LABEL maintainer="z50205 <z50205@yahoo.com.tw>"

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

COPY . /PSS

WORKDIR /PSS

RUN ls -l /PSS  # 檢查文件是否存在

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirement.txt && pip install gevent-websocket && pip install gunicorn && chmod 755 run_server.sh

EXPOSE 8002

ENTRYPOINT ["/PSS/run_server.sh"]