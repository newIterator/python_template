import os
from save_file import create_folder
# find the target folder or file path
file_name = "static";
absolute_path = os.path.abspath(file_name);

# create object of folder name
folder_path = absolute_path+"/楼下监控数据"
#
file_name = "2025_6_5person在视频出现的时间片段.pdf"

create_folder(folder_path,file_name)

