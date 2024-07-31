
import json

def merge_json_files(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    new_data = []
    for item in data:
        item["output_image_url"] = item["output_image_url"].split(')')[0]
        new_data.append(item)

    output_filename = json_file
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)

    print(f"Merged JSON data written to {output_filename}")

# Example usage
json_file = '/home/yangyaodong/projects/jiayi/data/8713_7_31.json'  # List your JSON files here
merge_json_files(json_file)
