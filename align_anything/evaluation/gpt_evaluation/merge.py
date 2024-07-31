import os
import json

def merge_json_files(json_files):
    merged_data = []
    total_count = 0

    for file in json_files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            merged_data.extend(data)
            total_count += len(data)

    output_filename = f"/home/yangyaodong/projects/jiayi/data/{total_count}_7_31.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=4)

    print(f"Merged JSON data written to {output_filename}")

# Example usage
json_files = [
    '/home/yangyaodong/projects/jiayi/data/5000_full_filltered.json', 
    '/home/yangyaodong/projects/jiayi/data/5000_full_filltered_new.json', 
    ]  # List your JSON files here
merge_json_files(json_files)
