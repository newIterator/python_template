import cv2
import os
from ultralytics import YOLO

def extract_person_frames(video_path, output_dir="output_frames", conf_threshold=0.5):
    """
    提取视频中包含人物的关键帧并保存为图片
    :param video_path: 输入视频路径
    :param output_dir: 输出目录
    :param conf_threshold: 检测置信度阈值
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # 加载YOLOv8人物检测模型
    model = YOLO("yolov8n.pt")  # 使用轻量级模型
    
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 每隔N帧检测一次（提高效率）
        if frame_count % int(fps) == 0:  # 每秒检测1次
            results = model(frame, classes=0, conf=conf_threshold)  # classes=0表示只检测人

            # 如果检测到人物，保存帧
            if len(results[0].boxes) > 0:
                output_path = os.path.join(output_dir, f"person_{frame_count}.jpg")
                cv2.imwrite(output_path, frame)
                saved_count += 1

        frame_count += 1

    cap.release()
    print(f"已保存 {saved_count} 张含人物的关键帧到 {output_dir}")

# 使用示例
# 输入的video
file_name = "static" 
absolute_path = os.path.abspath(file_name);
input_video = absolute_path+"/IMG_0530.mp4";
# 输出图片的目录
output_dir = absolute_path+"/source";

# extract_person_frames(input_video,output_dir)
def createPic(output_dir,file_name,frame):
    output_path = os.path.join(output_dir, file_name)
    cv2.imwrite(output_path, frame)