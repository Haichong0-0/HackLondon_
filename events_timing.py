import openai
import json
import user_request_processor

# 碰到有 or 的情况, 进行事件选择或拆分

PROMPT