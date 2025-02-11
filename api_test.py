import os
from openai import OpenAI
def api_serve(str_content,str_backaround = 'You are a helpful assistant.'):
    str1 = str(str_content)
    str2 = str(str_backaround)
    try:
        client = OpenAI(
            #api应该由用户输入
            api_key="",
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

        completion = client.chat.completions.create(
            model="qwen-turbo",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': str1}
                ]
        )
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content
    except Exception as e:
        print(f"错误信息：{e}")
        print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")

if __name__ == '__main__':
    
    while True:
        print("以下为控制台测试:")
        concent = input("输入内容,按回车确认:")
        api_serve(concent,'You are a helpful assistant.')
