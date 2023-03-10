from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET_KEY"] = "123"

socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("message")
def handler_message(message):
    send(message, broadcast=True)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app)