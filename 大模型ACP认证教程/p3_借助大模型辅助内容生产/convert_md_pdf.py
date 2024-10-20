import os
from PIL import Image
import subprocess
from pdf2image import convert_from_path
import argparse
import time

def convert_single_md_to_pdf_and_png(md_file_path, output_base_dir="./Marp/"):
    """
    将单个MD文件转换为PDF和PNG格式，PDF和PNG文件将保存在由MD文件名决定的子目录中。

    :param md_file_path: MD文件的完整路径。
    :param output_base_dir: 输出目录的基路径，将在此目录下创建子目录以保存输出文件。
    """

    if not os.path.exists(output_base_dir):
        os.makedirs(output_base_dir)

    # 获取MD文件名（去掉.md后缀）
    filename = os.path.splitext(os.path.basename(md_file_path))[0]

    # 创建输出目录，目录名与MD文件名相同
    output_dir = os.path.join(output_base_dir, filename)
    os.makedirs(output_dir, exist_ok=True)  # 如果目录已存在，则不会抛出异常

    # 构建Marp CLI命令
    command = ["marp", "--html", "--allow-local-files",
               "--output", os.path.join(output_dir, filename + ".pdf"),
               "--format", "pdf",
               md_file_path]

    try:
        # 执行命令，将MD文件转换为PDF
        print(command)
        subprocess.run(command, check=True)
        print(f"成功将 '{md_file_path}' 转换为PDF并保存至 '{output_dir}'。")

        # 将PDF转换为PNG图像
        pdf_file = os.path.join(output_dir, filename + ".pdf")
        pages = convert_from_path(pdf_file, dpi=300)  # dpi参数可以根据需要调整

        # 遍历每一页并保存为PNG格式
        for i, page in enumerate(pages):
            file_name = os.path.join(output_dir, f"{filename}_{i+1}.png")
            page.save(file_name, 'PNG')
        print(f"成功将 '{pdf_file}' 转换为PNG图像并保存至 '{output_dir}'。")
    except subprocess.CalledProcessError as e:
        print(f"转换 '{md_file_path}' 时发生错误: {e}")
        print("\n尝试另外一种生成方法，先转换为pptx再生成pdf:")
        convert_single_md_to_pptx_pdf_and_png(md_file_path, output_base_dir)        


def convert_single_md_to_pptx_pdf_and_png(md_file_path, output_base_dir="./Marp/"):
    """
    将单个MD文件转换为PDF和PNG格式，PDF和PNG文件将保存在由MD文件名决定的子目录中。

    :param md_file_path: MD文件的完整路径。
    :param output_base_dir: 输出目录的基路径，将在此目录下创建子目录以保存输出文件。
    """

    if not os.path.exists(output_base_dir):
        os.makedirs(output_base_dir)

    # 获取MD文件名（去掉.md后缀）
    filename = os.path.splitext(os.path.basename(md_file_path))[0]

    # 创建输出目录，目录名与MD文件名相同
    output_dir = os.path.join(output_base_dir, filename)
    os.makedirs(output_dir, exist_ok=True)  # 如果目录已存在，则不会抛出异常
    
    command = ["marp", "--html", "--allow-local-files",
               "--output", os.path.join(output_dir, filename + ".pptx"),
               md_file_path]

    try:
        # 执行命令，将MD文件转换为PDF
        # print(command)
        subprocess.run(command, check=True)
        print(f"成功将 '{md_file_path}' 转换为pptx并保存至 '{output_dir}'。")
        
        # 将pptx转换为pdf图像
        pptx_file = os.path.join(output_dir, filename + ".pptx")        
        command = ["libreoffice", "--headless", "--convert-to","pdf:writer_pdf_Export",
               "--outdir", os.path.join(output_dir),
               pptx_file]

        # print(command)
        subprocess.run(command, check=True)
        print(f"成功将 '{md_file_path}' 转换为PDF并保存至 '{output_dir}'。")
        
        time.sleep(5)
        
        # 将PDF转换为PNG图像
        pdf_file = os.path.join(output_dir, filename + ".pdf")
        print("pdf_file:",pdf_file)
        pages = convert_from_path(pdf_file, dpi=300)  # dpi参数可以根据需要调整

        # 遍历每一页并保存为PNG格式
        for i, page in enumerate(pages):
            file_name = os.path.join(output_dir, f"{filename}_{i+1}.png")
            page.save(file_name, 'PNG')
        print(f"成功将 '{pdf_file}' 转换为PNG图像并保存至 '{output_dir}'。")
    except subprocess.CalledProcessError as e:
        print(f"转换 '{md_file_path}' 时发生错误: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="处理文件并输出到指定目录。")
    parser.add_argument("file_path", type=str, help="输入Marp文件的路径。")
    parser.add_argument("output_dir", type=str, help="输出目录的路径。")

    args = parser.parse_args()

    try:
        print(args.file_path)
        print(args.output_dir)
        convert_single_md_to_pdf_and_png(args.file_path, args.output_dir)
    except FileNotFoundError as e:
        print(f"错误: {e}")
    except Exception as e:  # 捕获其他可能的异常
        print(f"发生意外错误: {e}")

