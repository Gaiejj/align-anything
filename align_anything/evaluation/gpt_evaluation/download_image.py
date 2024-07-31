import os
import json
import requests

def download_image(url, folder_path, file_name):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(os.path.join(folder_path, file_name), 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded: {file_name}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def download_images_from_json(json_file_path, download_folder):
    # 创建下载文件夹（如果不存在）
    os.makedirs(download_folder, exist_ok=True)
    
    # 读取JSON文件
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 遍历JSON中的每一项并下载图片
    for item in data:
        image_url = item.get('output_image_url')
        if image_url:
            file_name = os.path.basename(image_url)
            download_image(image_url, download_folder, file_name)
        else:
            print("No 'output_image_url' found for item:", item)

# 使用示例
json_file_path = '/home/yangyaodong/projects/jiayi/data/8713_7_31.json'
download_folder = '/raid/jiayi/image_dataset/7_31'
download_images_from_json(json_file_path, download_folder)
