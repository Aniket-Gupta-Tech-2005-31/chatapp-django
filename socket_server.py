import socketio
import eventlet
import eventlet.wsgi
from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproject.settings')

django_app = get_wsgi_application()

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, django_app)

@sio.event
def connect(sid, environ):
    print("User connected:", sid)

@sio.event
def disconnect(sid):
    print("User disconnected:", sid)

@sio.event
def message(sid, data):
    # data = { user: "", message: "" }
    sio.emit("message", data)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8000)), app)
