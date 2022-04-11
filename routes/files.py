from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.status import HTTP_200_OK
from model.connection import ConnectionManager
import socket
import base64

app_files = APIRouter()

manager = ConnectionManager()

host_ip_address = socket.gethostbyname(socket.gethostname())

host = "172.19.92.45"

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Upload File</title>
    </head>
    <body>
        <h1>Upload File</h1>
        <form action="/upload-file/" enctype="multipart/form-data" method="post">
            <input name="file" type="file">
            <input type="submit">
        </form>

        <p>Clic here to go <a href="/">home</a>.</p>
    </body>
</html>
"""

@app_files.get(
    path='/',
    status_code=HTTP_200_OK,
    tags=['Upload and sent file'],
    summary='welcome":"Upload files is up.')

async def get():
    return HTMLResponse(html)

'''
    Files stuff
'''

# TODO: Send it as a message in the websocket to the client

@app_files.post(
    path='/',
    status_code=HTTP_200_OK,
    tags=['Sent file'])

async def create_upload_files(
    file: UploadFile = File(..., description="Unique File")
    ):

    content = await file.read()
    encoded_information = base64.b64encode(content).decode('utf-8')
    return JSONResponse(
        {'message': 'Successful operation', 'encoded_file': encoded_information},
        200
    )