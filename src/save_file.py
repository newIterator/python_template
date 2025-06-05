import os
# find the target folder or file path
file_name = "static";
absolute_path = os.path.abspath(file_name);

# create object of folder name
folder_path = absolute_path+"/folder"

# create the target file
def create_file(target_folder,file):
    file_path = os.path.join(target_folder,file)
    # write the content into the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("这是写入的内容\n第二行内容")
    print(f"文件 {file_path} 写入成功")

# create target folder
def create_folder(folder_name,file):
    
    # 创建文件夹（如果不存在）
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"文件夹 {folder_name} 创建成功")
    else:
        print(f"文件夹 {folder_name} 已存在")
        create_file(folder_name,file);
        

# create_folder(folder_path,"test.pdf")
