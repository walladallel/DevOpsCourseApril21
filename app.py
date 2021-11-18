from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>", 200


@app.route("/healthy")
def healthy():
    return "healthy", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
