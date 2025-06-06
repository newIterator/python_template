import os
from tkinter import Tk, filedialog

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
    for root_dir, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root_dir, file)
            all_files.append(file_path)

    # 打印结果
    print(f"文件夹路径: {folder_path}")
    print("文件列表:")
    for file in all_files:
        print(f"{file}")

    return all_files

# 调用函数
files = select_folder_and_list_files()