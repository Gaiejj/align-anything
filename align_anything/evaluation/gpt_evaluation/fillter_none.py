import json

def filter_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    filtered_data = [item for item in data if all(value is not None for value in item.values())]

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, ensure_ascii=False, indent=4)

def filter_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    filtered_lines = []
    for line in lines:
        item = json.loads(line)
        if all(value is not None for value in item.values()):
            filtered_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(filtered_lines)

def main(input_file, output_file):
    if input_file.endswith('.json'):
        filter_json(input_file, output_file)
    elif input_file.endswith('.jsonl'):
        filter_jsonl(input_file, output_file)
    else:
        print("Unsupported file format. Please provide a .json or .jsonl file.")

if __name__ == "__main__":
    input_file = "/home/yangyaodong/projects/jiayi/data/5000_full.json"  # 替换为你的输入文件名
    output_file = "/home/yangyaodong/projects/jiayi/data/5000_full_filltered_new.json"  # 替换为你的输出文件名
    main(input_file, output_file)
