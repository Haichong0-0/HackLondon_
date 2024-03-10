# config.py
def read_api_key(file_path):
    print("execcuting `read_api_key` function")
    with open(file_path, 'r') as file:
        return file.read().strip()


API_KEY = read_api_key('../openai_key.txt')
