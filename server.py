from flask import Flask, render_template
from flask_socketio import SocketIO
import motor


app = Flask(__name__)
socket = SocketIO(app)

motor = Motor()

@app.route('/')
def send_index():
    return render_template('index.html')

@socket.on('move')
def move(data):
    direction = data['direction']
    if direction == 'right':
        motor.right()
    elif direction == 'left':
        motor.left()
    elif direction == 'forward':
        motor.forward()
    elif direction == 'reverse':
        motor.reverse()

@socket.on('stop')
def stop():
    motor.stop()

if __name__ == '__main__':
    socket.run(app)
