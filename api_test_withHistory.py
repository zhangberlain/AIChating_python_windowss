import os
from openai import OpenAI

messages_input = []

def api_serve_withHistory(str_content,api_keyyy,str_backaround = 'You are a helpful assistant.'):
    str1 = str(str_content)
    str2 = str(str_backaround)
    global messages_input
    if messages_input == []:
        messages_input = [{'role': 'system', 'content': str2}]
    messages_input.append({'role': 'user', 'content': str1})
    try:
        client = OpenAI(
            #api应该由用户输入
            api_key=api_keyyy,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

        completion = client.chat.completions.create(
            model="qwen2.5-1.5b-instruct",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            messages=messages_input
        )
        print(completion.choices[0].message.content)
        messages_input.append({'role':'assistant','content':completion.choices[0].message.content})
        print('\n')
        print(messages_input)
        print('\n')
        print(completion)
        print('\n')

        return completion.choices[0].message.content
    except Exception as e:
        print(f"错误信息：{e}")
        print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")

def clear_content_history():
    global messages_input
    messages_input = []


if __name__ == '__main__':
    apiKey = input("输入测试key")
    while True:
        print("以下为控制台测试:")
        concent = input("输入内容,按回车确认:")
        api_serve_withHistory(concent,apiKey,'You are a helpful assistant.')
