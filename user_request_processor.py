import events_categorizing
import events_enumerating
import events_timing
import events_formatting

def read_api_key(file_path):
    """
    从给定的文件路径读取 OpenAI 的 API 密钥。
    
    参数:
    - file_path: 包含 API 密钥的文件的路径。
    
    返回:
    - 文件中的 API 密钥字符串。
    """
    with open(file_path, 'r') as file:
        api_key = file.read().strip()  # 读取文件内容并去除可能的前后空格
    return api_key

# 使用示例
api_key_file_path = '../openai_key.txt'  # 修改为你的文件路径
api_key = read_api_key(api_key_file_path)

# 现在可以使用 api_key 变量来配置你的 OpenAI API 调用
