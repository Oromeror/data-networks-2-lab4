import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from starlette.status import HTTP_200_OK
from routes import app_ws_chat, app_files
from settings import ENVIRONMENT
import socket

app = FastAPI()

logger = logging.getLogger("fastapi")


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
        <h1>Welcome</h1>
        <p>Clic here to open <a href="/chat">chat</a>.</p>
        <p>Clic here to open <a href="/upload-file">upload and sent file</a>.</p>
    </body>
</html>
"""

if ENVIRONMENT == 'live':
    origins = ['']
else:
    origins = ['', 'http://localhost:5000']

@app.get(
    path='/',
    status_code=HTTP_200_OK,
    tags=['Welcome'],
    summary='welcome":"API is working.')
    
async def get():
    return HTMLResponse(html)

def read_root():
    return{"welcome":"server is up."}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Host ip to access
host_ip_address = socket.gethostbyname(socket.gethostname())
print(f'Open {host_ip_address}:5000 in client browser')

# WebSocket Chat
app.include_router(app_ws_chat, prefix='/chat')

# Files
app.include_router(app_files, prefix='/upload-file')


#@app.on_event('startup')
#def connect_db():
    #mysql.sql_conn = mysql.db_connection()