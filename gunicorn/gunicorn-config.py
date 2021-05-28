
bind = '0.0.0.0:8000'
backlog = 2048

workers = 5
worker_class = 'uvicorn.workers.UvicornWorker'
worker_connections = 5000
timeout = 3600
keepalive = 20

spew = False
