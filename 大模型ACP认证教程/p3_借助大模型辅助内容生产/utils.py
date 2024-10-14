import os

def create_directory(file_path):
    """
    创建文件目录。
    :param file_path: 完整的文件路径
    """
    # 获取目标文件的目录
    output_dir = os.path.dirname(file_path)
    print(f"目标目录：{output_dir}")  # 打印目录
    # 确保目标目录存在
    os.makedirs(output_dir, exist_ok=True)

def save_file(content, file_path):
    """
    保存文件到指定路径。
    :param content: 文件内容（字符串格式或列表格式）
    :param file_path: 完整的文件路径
    """
    create_directory(file_path)  # 创建目录
    print(f"文件路径：{file_path}")  # 打印完整文件路径

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"文件已成功保存为：{file_path}")

def read_text_from_file(file_path):
    """
    从指定文件路径读取文本内容，并返回文本。

    :param file_path: str，文件的路径。
    :return: str，文件的内容。如果文件不存在或读取失败，则返回空字符串。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()  # 读取文件内容
            print(f"成功读取文件：{file_path}")  # 打印成功信息
            return content  # 返回读取的内容
    except Exception as e:
        print(f"读取文件失败: {e}")  # 打印错误信息
        return ""  # 在发生异常时返回空字符串