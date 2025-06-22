import os
import sys
from pathlib import Path


def count_lines_in_file(file_path: Path) -> int:
    """统计单个文件的行数"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except Exception as e:
        print(f"无法读取文件 {file_path}: {e}", file=sys.stderr)
        return 0


def count_code_lines(root_dir: str, exclude_dirs: list = None, exclude_exts: list = None) -> dict:
    """
    统计目录下所有代码文件的行数

    参数:
    root_dir: 根目录路径
    exclude_dirs: 要排除的目录名称列表
    exclude_exts: 要排除的文件扩展名列表

    返回:
    包含总文件数、总行数和各扩展名统计的字典
    """
    if exclude_dirs is None:
        exclude_dirs = ['.git', 'node_modules', '__pycache__', 'venv']
    if exclude_exts is None:
        exclude_exts = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.pdf', '.zip', '.gz', '.tar']

    total_lines = 0
    file_count = 0
    extension_stats = {}

    for root, dirs, files in os.walk(root_dir):
        # 排除指定目录
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            file_path = Path(root) / file
            ext = file_path.suffix.lower()

            # 排除指定扩展名
            if ext in exclude_exts:
                continue

            lines = count_lines_in_file(file_path)
            total_lines += lines
            file_count += 1

            # 更新扩展名统计
            if ext in extension_stats:
                extension_stats[ext]['files'] += 1
                extension_stats[ext]['lines'] += lines
            else:
                extension_stats[ext] = {'files': 1, 'lines': lines}

    return {
        'total_files': file_count,
        'total_lines': total_lines,
        'extension_stats': extension_stats
    }


def print_statistics(stats: dict):
    """打印统计结果"""
    print(f"总文件数: {stats['total_files']}")
    print(f"总行数: {stats['total_lines']}")
    print("\n各类型文件统计:")

    # 按行数排序
    sorted_exts = sorted(
        stats['extension_stats'].items(),
        key=lambda x: x[1]['lines'],
        reverse=True
    )

    for ext, data in sorted_exts:
        print(f"{ext}: {data['files']} 个文件, {data['lines']} 行")


if __name__ == "__main__":
    # 默认统计当前目录
    target_dir = sys.argv[1] if len(sys.argv) > 1 else '.'

    print(f"正在统计目录: {os.path.abspath(target_dir)}")
    stats = count_code_lines(target_dir)
    print_statistics(stats)