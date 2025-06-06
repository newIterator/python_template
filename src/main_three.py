import cv2
from ultralytics import YOLO
import pandas as pd
import os
from get_person_step import createPic
#Name: numpy
#Version: 2.2.6

# Get the abs path
file_name = "static" 
absolute_path = os.path.abspath(file_name);
video_path = absolute_path+"/IMG_0530.mp4";
# output file save of folder
output_dir = absolute_path+"/source";
# 加载YOLOv8模型（自动下载预训练权重）
model = YOLO("yolov8n.pt")  # 轻量级模型，可选yolov8s/m/l/x

# 打开视频文件
cap = cv2.VideoCapture(video_path)

# 获取视频的FPS（帧率）和总帧数
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 存储人物出现的时间节点
person_appearances = []

# 逐帧处理
for frame_idx in range(total_frames):
    ret, frame = cap.read()
    if not ret:
        break

    # 用YOLO检测当前帧
    results = model(frame, classes=0)  # classes=0表示只检测"person"（COCO类别）

    # 如果检测到人物，记录时间
    if len(results[0].boxes) > 0:  # 检测到至少一个人
        current_time = frame_idx / fps  # 当前时间（秒）
        person_appearances.append(current_time)
        createPic(output_dir,f"person_{current_time}.jpg",frame)

cap.release()

# 合并连续的时间点，生成时间区间
time_windows = []
if person_appearances:
    start_time = person_appearances[0]
    prev_time = person_appearances[0]

    for time in person_appearances[1:]:
        if time - prev_time > 1.0:  # 如果间隔超过1秒，认为是一个新的区间
            time_windows.append((start_time, prev_time))
            start_time = time
        prev_time = time
    time_windows.append((start_time, prev_time))  # 添加最后一个区间
# 输出结果
print("人物出现的时间区间（秒）：")
for start, end in time_windows:
    if start < 60 and end < 60:
        print(f"{start:.2f} - {end:.2f} +secend")
    elif start < 60 and end > 60:
        print(f"{start:.2f} + secend - {end/60:.2f}+minute")
    elif start > 60 and end > 60 :
        print(f"{start/60:.2f} - {end/60:.2f} + minute")
    elif start > 3600 and end > 3600 :
        print(f"{start/3600:.2f} - {end/3600:.2f} + hour")
    
# 可选：保存到CSV
df = pd.DataFrame(time_windows, columns=["Start Time (s)", "End Time (s)"])
df.to_csv("person_appearances.csv", index=False)