#This FastAPI application defines an endpoint /file/upload that accepts POST requests for uploading files. It checks if the uploaded file is a JSON file (application/json), raising a 400 HTTP error for invalid file types. If the file is valid, it reads and parses the JSON content, returning it along with the filename. The application runs on 127.0.0.1 at port 8000 using the Uvicorn ASGI server.

from fastapi import FastAPI, UploadFile
from fastapi.exceptions import HTTPException
import uvicorn 
import json

# Init App
app = FastAPI()

@app.post("/file/upload")
def upload_file(file: UploadFile):
    if file.content_type != "application/json":
        raise HTTPException(400,detail="Invalid document type")
    else:
        data = json.loads(file.file.read())
    return {"content":data ,"filename":file.filename}


if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=8000)