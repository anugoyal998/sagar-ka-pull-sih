from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(debug=True)
origins = [
    'http://localhost:3000/',
    'http://localhost:3000',
]
app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins
)

    
import cv2    
from ultralytics import YOLO
from PIL import Image
# from super_gradients.training.models.detection_models.yolo_base import YoloXPostPredictionCallback
# from model.crowd import crowd_model, draw_bbox_crowd
from model.fire_smoke import draw_bbox_fire_smoke
# from model.crowd import draw_bbox_crowd
from model.crowd2 import draw_bbox_crowd2
video_path = "examples/video4.mp4"
fire_video_path2 = "examples/Apartment Fire in Selah, WA Yakima County.mp4"
model_path = "weights/crowd.pt"
fire_model_path = "weights/fire-smoke-yolov8.pt"

@app.get("/stream_video")
async def stream_video():
    cap = cv2.VideoCapture(video_path)
    model = YOLO(model_path,"v8")
    async def generate_frames():
        frame_count = 0
        while True:
            ret, frame = cap.read()
            frame_count += 1
            if ret == True:
                # if frame_count > 1:
                    # break
                # results = fire_model(frame)
                # annotated_frame = results[0].plot()
                frame,count = draw_bbox_crowd2(model,frame)
                # print("The people in the frame is",count)
                # predictions = crowd_model.predict(frame)
                # crowd_count = draw_bbox_crowd(predictions,annotated_frame)
                # frame = cv2.putText(annotated_frame,str(crowd_count*2),(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
                # frame_encoded  = cv2.imencode(".jpg", annotated_frame)[1].tobytes()
                frame_encoded  = cv2.imencode(".jpg", frame)[1].tobytes()
                yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame_encoded + b"\r\n")
            else:
                break
            
    
    return StreamingResponse(generate_frames(),media_type="multipart/x-mixed-replace; boundary=frame")

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
                # if frame_count > 1:
                    # break
                # results = fire_model(frame)
                # annotated_frame = results[0].plot()
                results = fire_model(frame)
                draw_bbox_fire_smoke(results,frame)
                # print("The people in the frame is",count)
                # predictions = crowd_model.predict(frame)
                # crowd_count = draw_bbox_crowd(predictions,annotated_frame)
                # frame = cv2.putText(annotated_frame,str(crowd_count*2),(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
                # frame_encoded  = cv2.imencode(".jpg", annotated_frame)[1].tobytes()
                frame_encoded  = cv2.imencode(".jpg", frame)[1].tobytes()
                yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame_encoded + b"\r\n")
            else:
                break
            
    
    return StreamingResponse(generate_frames(),media_type="multipart/x-mixed-replace; boundary=frame")        

if __name__== "__main__":
    uvicorn.run(app,host = 'localhost',port = 8000)