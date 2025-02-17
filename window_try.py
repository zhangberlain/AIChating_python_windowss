# -*- coding:'utf-8' -*-
import tkinter
from tkinter import ttk
from PIL import Image , ImageTk
import tkinter.test
from image_input import image_input
from api_test_WithoutHistory import *
from api_test_withHistory import *

import threading

def main():
    global root
    root = tkinter.Tk()
    root.title(string= "哇,是AI,我们有救了")
    root.geometry(newGeometry="800x600+500+50")
    root.resizable(width=True,height=True)
    root.config(bg = "white")

    image1001,width1001,height1001 = image_input(r'.\photos\1012.png')
    max_width = 150
    max_height = 200
    ratio = min(max_width/width1001,max_height/height1001)
    width_new = int(width1001 * ratio)
    height_new = int(height1001 * ratio)

    resized_image1001 = image1001.resize((width_new,height_new),Image.Resampling.LANCZOS)
    tk_image1001 = ImageTk.PhotoImage(resized_image1001)
    label_1004 = tkinter.Label(root , image=tk_image1001)
    label_1004.pack()

    bottom_1001 = tkinter.Button(root, text = 'bottom', command = click1001)
    bottom_1001.pack()

    #Frame1开始
    frame_1001 = tkinter.Frame(master=root)
    global entry_1001
    entry_1001 = tkinter.Entry(
        frame_1001,
        bg= 'white',
        bd= 4
        )
    entry_1001.bind("<Return>",send_1001)
    entry_1001.pack(side=tkinter.LEFT, pady=3 )

    bottom_1002 = tkinter.Button(
        frame_1001, 
        bg= 'light blue',
        text= '发送',
        command= send_1001
        )
    bottom_1002.pack(side=tkinter.RIGHT,pady= 4)

    frame_1001.pack(pady= 5)
    #Frame1结束

    #frame1.1启动
    frame_10011 = tkinter.Frame(root)
    label_1005 = tkinter.Label(frame_10011,text=r"请将'钥匙'/api_key粘贴进灰色框")
    label_1005.pack(side=tkinter.LEFT,padx=1,pady=1)

    global api_keyyyyy
    api_keyyyyy = tkinter.StringVar()
    entry_1002 = tkinter.Entry(frame_10011, bg= 'gray',textvariable=api_keyyyyy,show='**')
    entry_1002.pack(side=tkinter.RIGHT,padx=1)
    frame_10011.pack()
    #frame1.1结束
    global historyOrNot
    historyOrNot = tkinter.IntVar()#默认不需要上下文
    historyOrNot.set(0)
    #frame1.2启动
    frame_10012 = tkinter.Frame(root)
    bottom_1003 = tkinter.Radiobutton(frame_10012,text="需要上下文",variable=historyOrNot, value=1)
    bottom_1004 = tkinter.Radiobutton(frame_10012,text="不需要上下文", variable=historyOrNot, value=0  )
    bottom_1003.pack(side=tkinter.LEFT)
    bottom_1004.pack(side=tkinter.RIGHT)
    frame_10012.pack()
    #frame1.2结束


    #frame2启动
    frame_1002 = tkinter.Frame(root)
    global text_1001
    text_1001 = tkinter.Text(frame_1002,width=80,height = 300)
    text_1001.pack(pady=10)
    text_1001.insert("1.0",'{user},您好,这是调用qwen的ai助手,请在上面白色输入框中输入问题\n\n'.format(user = "用户"))

    scrolllbar_1001 = tkinter.Scrollbar(frame_1002)
    scrolllbar_1001.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    scrolllbar_1001.config(command=text_1001.yview)
    frame_1002.pack(pady=5)
    #frame2结束
    tkinter.mainloop()
    return 0

def click1001():
    print('what can i say?')
    print(api_keyyyyy.get())
    return 0

def send_1001(text = None):
    global inputText
    inputText = ''
    inputText = entry_1001.get()
    if inputText == '':
        print('输入不能为空')
        return 0
    entry_1001.delete(0, tkinter.END)
    print('输入为:',inputText,'\n')
    shuaxinText()

    return 0

def shuaxinText():
    text_1001.delete("2.0",tkinter.END)
    text_1001.insert("2.0",'\n您:{}\nAI:思考中...\n'.format(inputText))
    #另开线程!
    threading.Thread(target=sedToAI, args=(inputText,)).start()
    return 0

def sedToAI(text1):
    #插入root中
    if historyOrNot.get() == 0:
        response =  api_serve_withoutHistory(text1,api_keyyy=api_keyyyyy.get())
    elif historyOrNot.get() == 1:
        response =  api_serve_withHistory(text1,api_keyyy=api_keyyyyy.get())
    root.after(0, update_response, response)
    return 0

def update_response(response):
    # 删除"正在处理"的临时提示
    text_1001.delete("end-2l linestart", "end-1c")
    text_1001.insert(tkinter.END, "AI: " + response + "\n\n")  # 插入AI的响应
    text_1001.see(tkinter.END)  # 滚动到底部
    return 0



if __name__ == '__main__':
    main()


    '''
        todo:1.上下文功能,
            2.背景设定,各类参数调节
            3.输出结果日志,
            4.流式交互功能,
            5.图片输入功能
            6.移植安卓
    '''