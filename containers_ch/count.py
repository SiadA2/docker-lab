from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def welcome_message():
    return "Welcome to Siad's local webpage"


@app.route('/count')
def web_count():
    count = r.incr('counter')
    return f'This page has been visited {count} times'



if __name__ == '__main__':
    app.run(
        host='0.0.0.0', 
        port=2000
        )

