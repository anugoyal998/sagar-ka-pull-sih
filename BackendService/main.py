from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
origins = [
    'http://localhost:3000/',
    'http://localhost:3000',
]
app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins
)
@app.get("/video")
async def get_video():
    video_path = "../crowd_counter/Rush hour at train station in India.mp4"  
    print("Sending Video")
    return FileResponse(video_path, media_type="video/mp4")

if __name__== "__main__":
    uvicorn.run(app,host = 'localhost',port = 8000, reload = False)