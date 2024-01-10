import cv2

from flask import Flask,Response

app  = Flask(__name__)

def generate_frames():
  cap = cv2.VideoCapture(0)
  while True:
    ret,frame = cap.read()
    
    #将当前帧转换为字节流
    ret,buffer = cv2.imencode(".jpg",frame)
    frame_bytes = buffer.tobytes()

    # 通过生成器返回视频流
    yield(b'--frame\r\n'b'Content-Type:image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/')
def video_feed():
  return Response(generate_frames(),mimetype= 'mutipart/x-mixed-replace;boundary=frame') 

if __name__ == '__main__':
  app.run(port="6009")  



