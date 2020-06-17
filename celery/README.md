### 安装RabbitMQ
```
# Ubuntu或Debian
sudo apt-get install rabbitmq-server

# Docker
docker run -d -p 5672:5672 rabbitmq
```

### 安装redis
```
docker run -d -p 6379:6379 redis
```


### 常用命令
```
celery -A tasks worker --loglevel=info

celery worker --help
```
