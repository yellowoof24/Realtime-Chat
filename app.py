from flask import Flask, render_template
from flask_socketio import SocketIO
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET KEY'
socketio = SocketIO(app)

@app.route("/")
def chat():
    return render_template("chat.html")

@socketio.on('chat')
def join(data, methods=['GET', 'POST']):
    data["msg"] = re.sub(r'(<([^>]+)>)', "", data["msg"], flags=re.MULTILINE)
    data["name"] = re.sub(r'(<([^>]+)>)', "", data["name"], flags=re.MULTILINE)
    print(data["msg"])
    socketio.emit('chat', data)

@socketio.on('join')
def join(data, methods=['GET', 'POST']):
    data["name"] = re.sub(r'(<([^>]+)>)', "", data["name"], flags=re.MULTILINE)
    socketio.emit('join', data)

if __name__ == '__main__':
    socketio.run(app, debug=True)
