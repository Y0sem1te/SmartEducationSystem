from fastapi import Depends, FastAPI, HTTPException, Query,WebSocket,UploadFile,File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import cv2
import asyncio
import os
import shutil
class Test(BaseModel):
    id: int
origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              # 允许的源
    allow_methods=["*"],                # 允许所有方法：GET、POST等
    allow_headers=["*"],                # 允许所有请求头
)
@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.post('/test', response_model=Test)
async def test1(test: Test):
    print(test.model_dump())
    return test

@app.websocket("/ws/video")
async def video_stream(websocket: WebSocket):
    await websocket.accept()
    cap = cv2.VideoCapture(0)  # 使用默认摄像头
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # 编码为 JPEG
            frame = cv2.resize(frame, (870,500))
            _, buffer = cv2.imencode('.jpg', frame)
            # 发送二进制帧
            await websocket.send_bytes(buffer.tobytes())
            await asyncio.sleep(0.01)  # 控制帧率约为30fps
    except Exception as e:
        print(f"连接关闭：{e}")
    finally:
        cap.release()
        print("摄象头已关闭")

@app.post("/upload_video/")
async def upload_video(file: UploadFile):
    if not file.filename.lower().endswith((".mp4",".mov",".avi",".webm",".m4v")):
        return {"message":"shabi"}
    os.makedirs('video', exist_ok=True)
    file_location = os.path.join('video', os.path.basename(file.filename))
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}


