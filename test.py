import tkinter as tk

def assign_variable(event=None):
    global user_input  # 声明为全局变量以便其他函数访问
    user_input = entry.get()
    entry.delete(0, tk.END)  # 清空输入框
    print("当前输入内容：", user_input)  # 演示输出，实际使用时可以替换为其他操作

# 创建主窗口
root = tk.Tk()
root.title("输入框示例")

# 使用Frame容器来排列输入框和按钮
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

# 创建输入框
entry = tk.Entry(input_frame, width=30)
entry.pack(side=tk.LEFT, padx=5)

# 绑定回车键事件
entry.bind("<Return>", assign_variable)

# 创建触发按钮
submit_btn = tk.Button(
    input_frame,
    text="提交",
    command=assign_variable,  # 直接绑定同一个函数
    bg="#4CAF50",  # 绿色背景
    fg="white"     # 白色文字
)
submit_btn.pack(side=tk.LEFT, padx=5)

# 初始化存储变量
user_input = ""

# 提示标签
tk.Label(root, text="输入内容后按回车或点击提交").pack(pady=5)

# 启动主循环
root.mainloop()