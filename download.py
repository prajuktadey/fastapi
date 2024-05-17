from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
import os
import json
import yaml
import uvicorn
from datetime import datetime


#upload a JSON file, converts it to a YAML file, and returns the YAML file for download

#specifies the directory to save uploaded files 
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

#initialize the FastAPI app
app = FastAPI()

@app.post("/file/uploadndownload")
async def upload_n_download_file(file: UploadFile):
    #checks if the uploaded file is json or not
    if file.content_type != "application/json":
        raise HTTPException(400, detail="Invalid document type")

    #reads and parses the JSON content of the uploaded file
    json_data = json.loads(await file.read())
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    #creates a new filename with the original name and a timestamp, changing the extension to .yaml
    new_filename = "{}_{}.yaml".format(os.path.splitext(file.filename)[0], timestamp)

    # write the data to a YAML file
    save_file_path = os.path.join(UPLOAD_DIR, new_filename)
    with open(save_file_path, "w") as f:
        yaml.dump(json_data, f)

    # Return the file as a download
    return FileResponse(path=save_file_path, media_type="application/octet-stream", filename=new_filename)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
