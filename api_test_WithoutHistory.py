import os
from openai import OpenAI
def api_serve_withoutHistory(str_content,api_keyyy,str_backaround = 'You are a helpful assistant.'):
    str1 = str(str_content)
    str2 = str(str_backaround)
    
    try:
        client = OpenAI(
            #api应该由用户输入
            api_key=api_keyyy,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

        completion = client.chat.completions.create(
            model="qwen2.5-1.5b-instruct",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            messages=[
                {'role': 'system', 'content': str2},
                {'role': 'user', 'content': str1},
                
                ]
        )
        print(completion.choices[0].message.content)
        print(completion)
        return completion.choices[0].message.content
    except Exception as e:
        print(f"错误信息：{e}")
        print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")



if __name__ == '__main__':
    apiKey = input("输入测试key")
    while True:
        print("以下为控制台测试:")
        concent = input("输入内容,按回车确认:")
        api_serve_withoutHistory(concent,apiKey,'You are a helpful assistant.')
