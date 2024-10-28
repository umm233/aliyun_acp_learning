import os
from openai import OpenAI
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"), # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def invoke(user_message, model_name="qwen-plus"):
    completion = client.chat.completions.create(
        model=model_name, # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[{"role": "user", "content": user_message}]
    )
    # 生产环境建议考虑调用异常的处理
    return completion.choices[0].message.content
