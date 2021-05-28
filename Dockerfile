FROM quay.io/jaycb/fastapi-gunicorn-python3.6
COPY . .
RUN pip install -r requirements.txt
RUN chmod +x ./gunicorn/start-server.sh
ENTRYPOINT ./gunicorn/start-server.sh
