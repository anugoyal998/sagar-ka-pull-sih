import cv2
from model.crowd2 import draw_bbox_crowd2
from model.fire_smoke import draw_bbox_fire_smoke
from PIL import Image
from ultralytics import YOLO
from pathlib import Path
from fastapi import FastAPI, WebSocket
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np

app = FastAPI()
origins = [
    'http://localhost:5173'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
)


# from super_gradients.training.models.detection_models.yolo_base import YoloXPostPredictionCallback
# from model.crowd import crowd_model, draw_bbox_crowd
# from model.crowd import draw_bbox_crowd
video_path = "examples/crowd.mp4"
fire_video_path2 = "examples/fire.mp4"
model_path = "weights/crowd.pt"
fire_model_path = "weights/fire-smoke-yolov8.pt"


@app.get("/stream_video")
async def stream_video():
    cap = cv2.VideoCapture(video_path)
    model = YOLO(model_path, "v8")

    async def generate_frames():
        frame_count = 0
        while True:
            ret, frame = cap.read()
            frame_count += 1
            if ret == True:
                frame, count = draw_bbox_crowd2(model, frame)
                global crowd_count
                crowd_count = count
                frame_encoded = cv2.imencode(".jpg", frame)[1].tobytes()
                yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame_encoded + b"\r\n")
            else:
                break

    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")


@app.get("/stream_video2")
async def stream_video2():
    cap = cv2.VideoCapture(fire_video_path2)
    fire_model = YOLO(fire_model_path)

    async def generate_frames():
        frame_count = 0
        while True:
            ret, frame = cap.read()
            frame_count += 1
            if ret == True:
                results = fire_model(frame)
                fire_bool, frame = draw_bbox_fire_smoke(results, frame)
                global fire
                fire = fire_bool
                frame_encoded = cv2.imencode(".jpg", frame)[1].tobytes()
                yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame_encoded + b"\r\n")
            else:
                break

    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")


@app.websocket("/crowd-count")
async def crowd_count_handler(websocket: WebSocket):
    await websocket.accept()
    while True:
        await websocket.send_text(str(crowd_count))


@app.websocket("/fire")
async def fire_handler(websocket: WebSocket):
    await websocket.accept()
    while True:
        if fire == True:
            await websocket.send_text("True")
        else:
            await websocket.send_text("False")

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
