import os
from flask import Flask, render_template
import redis

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def welcome_message():
    return 'Welcome to the flask visit counter'


@app.route('/count')
def web_count():
    count = r.incr('counter')
    return f'This page has been visited {count} times'




if __name__ == '__main__':
    app.run(
        host='0.0.0.0', 
        port=2000
        )

