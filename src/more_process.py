from multiprocessing import Pool
from pathlib import Path
from open_select import select_folder_and_list_files
# 
select_static = select_folder_and_list_files()
print(f"{select_static[2]}")

def analyze_file(file_path):
    """单个文件的分析函数"""
    print(f"处理文件: {file_path}")
    # 在此处调用你的分析逻辑
    # 例如: os.system(f"python analyzer.py {file_path}")

if __name__ == "__main__":
    folder_path = select_static[2]
    files = [str(f) for f in Path(folder_path).rglob("*") if f.is_file()]
    
    # 启动多进程池
    with Pool(processes=min(4, len(files))) as pool:  # 限制最大进程数
        pool.map(analyze_file, files)