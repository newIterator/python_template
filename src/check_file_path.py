import os

file_name = "static" 
absolute_path = os.path.abspath(file_name);
print(absolute_path)
video_path = absolute_path+"/IMG_0530.mp4";
if os.path.exists(absolute_path):
    print("File exists")
else:
    print("File does not exist")