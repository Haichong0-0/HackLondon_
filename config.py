# config.py
def read_api_key(file_path):
    print("正在执行 read_api_key 函数")
    with open(file_path, 'r') as file:
        return file.read().strip()

API_KEY = read_api_key('../openai_key.txt')
