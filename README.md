# sentry-redis-nodestore
A Sentry extension to add Redis as a NodeStore backend


[Sentry](https://github.com/getsentry/sentry) extension implementing the
NodeStorage interface for [Redis](https://redis.io/)

# Installation

```bash
$ pip install https://github.com/negashev/sentry-redis-nodestore/releases/download/v1.0.0/sentry-redis-nodestore-1.0.0.tar.gz
```

# Configuration

```python
SENTRY_NODESTORE = 'sentry_redis_nodestore.backend.RedisNodeStorage'
SENTRY_NODESTORE_OPTIONS = {
    'host': 'redis',
    'port': 6379,
    'db': 0, 
    'password': 'passw0rd'
}
```
