from flask import Flask
from .message_publisher import publish_message
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/test")
def publish_test_message():
    publish_message(dict(text="Hello from Alexa"), 'print')
    return "Successfully enqueued"
