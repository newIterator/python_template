import os
import threading
from tkinter import Tk, filedialog
from main import analysisVideo

def select_folder_and_list_files():
    """
    弹出文件夹选择对话框，并列出文件夹内所有文件
    """
    # 创建Tkinter根窗口（隐藏）
    root = Tk()
    root.withdraw()  # 隐藏主窗口

    # 弹出文件夹选择对话框
    folder_path = filedialog.askdirectory(title="选择文件夹")
    if not folder_path:  # 用户取消选择
        print("未选择文件夹")
        return

    # 列出文件夹内所有文件
    all_files = []
    all_file_name = []
    for root_dir, dirs, files in os.walk(folder_path):
        for file in files:
            # print(f"{file.split('.',1)}")
            file_name = file.split('.',1)[0]
            file_path = os.path.join(root_dir, file)
            all_files.append(file_path)
            all_file_name.append(file_name)
    # 启动多线程
    threads = []
    # 打印结果
    # print(f"文件夹路径: {folder_path}")
    # print("文件列表:")
    for index, path in enumerate(all_files):
        # print(f"{index} -- {path}")
        # print(f"{all_file_name[index]}")
        # analysisVideo()
        our_file = folder_path+"/"+all_file_name[index]
        index_file_name = all_file_name[index]
        # analysis the mp4 file,do about the function or target
        # analysisVideo(path,our_file)
        # start threading
        t = threading.Thread(target=analysisVideo(path,our_file), args=(index,))
        t.start()
        threads.append(t)

    # 等待所有线程结束（可选）
    for t in threads:
        t.join()
    return all_files,all_file_name,folder_path

# 调用函数
files = select_folder_and_list_files()
