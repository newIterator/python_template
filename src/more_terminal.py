import os
import subprocess
from pathlib import Path

def open_terminals_for_files(folder_path, script_to_run="analyze.py"):
    """
    为文件夹内每个文件打开一个终端并执行分析脚本
    :param folder_path: 包含待分析文件的文件夹
    :param script_to_run: 分析脚本路径（需接受文件参数）
    """
    files = [f for f in Path(folder_path).rglob("*") if f.is_file()]
    
    for file in files:
        file_path = str(file.resolve())
        
        # 根据不同操作系统构建命令
        if os.name == "nt":  # Windows
            cmd = f'start cmd /k "python {script_to_run} {file_path}"'
        else:  # Linux/macOS
            cmd = f'x-terminal-emulator -e "python3 {script_to_run} {file_path}"'
            # macOS 可选：用 `open -a Terminal.app` 或 `gnome-terminal`（Linux）
        
        subprocess.Popen(cmd, shell=True)

    print(f"已为 {len(files)} 个文件启动终端")

# 使用示例
open_terminals_for_files("/path/to/files", "analyzer.py")