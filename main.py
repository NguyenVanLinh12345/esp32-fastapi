from fastapi import FastAPI, HTTPException
from fastapi import WebSocket,Request

app = FastAPI()

@app.get("/")
def create_email():
    return {"message": "hello world"}

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     print('Accepting client connection...')
#     await websocket.accept()
#     while True:
#         try:
#             # Wait for any message from the client
#             data=await websocket.receive_text()
#             print(data)
#             # Send message to the client

#             await websocket.send_text("resp")
#             print("Sending")
#             # print(data)
#         except Exception as e:
#             print('error:', e)
#             break
#     print('Bye..')

listSocket  = []
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    listSocket.append(websocket)
    while True:
        try:
            # Wait for any message from the client
            data=await websocket.receive_text()
            print(data)
            # Send message to the client
            for socket in listSocket:
                await socket.send_text(data)
        except Exception as e:
            listSocket.remove(websocket)
            break

import os
image_directory = "images/"
@app.websocket("/image-ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            # Nhận dữ liệu ảnh từ client
            image_data = await websocket.receive_bytes()
            # Xác định đường dẫn lưu trữ tệp ảnh
            save_path = os.path.join(image_directory, "anh.jpg")
            
            # Lưu dữ liệu ảnh vào tệp ảnh tương ứng
            with open(save_path, "wb") as image_file:
                image_file.write(image_data)
            # print("da nhan anh")
            await websocket.send_text("anh oke nhe")
        except Exception as e:
            print('error:', e)
            break