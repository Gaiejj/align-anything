import json
from collections import Counter

def count_cases(data):   
    # 提取所有 'case' 键的值
    case_values = [item['case'] for item in data]
    
    # 统计不同 'case' 键的种类及其数量
    case_counts = Counter(case_values)
    
    return case_counts

with open('/home/yangyaodong/projects/jiayi/data/30000_answer_generation.json', 'r') as file:
    data = json.load(file)

case_counts = count_cases(data)
print(case_counts)
