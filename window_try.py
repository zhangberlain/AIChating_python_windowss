# -*- coding:'utf-8' -*-
import tkinter
from PIL import Image , ImageTk
import tkinter.test
from image_input import image_input
from api_test import *
import threading

def main():
    global root
    root = tkinter.Tk()
    root.title(string= "this is title")
    root.geometry(newGeometry="800x600+500+50")
    root.resizable(width=True,height=True)
    root.config(bg = "white")
    '''
    label_1001 = tkinter.Label(
        root,
        text="this is Label",
        relief= 'groove',
        bg= 'light green',
        bd = 3,anchor='nw'
        )
    label_1001.anchor('nw')
    label_1001.pack(pady= 20)
    #tkinter.mainloop()
    label_1001.config(text="this is new label")
    label_1001.pack()


    s_words_1002 = 'this is changable words'
    label_1002 = tkinter.Label(root, text = s_words_1002, font= ('黑体',20 ))
    label_1002.pack()

    label_1003 = tkinter.Label(root, text= 'what can i say, man!', anchor='w', height= 2, fg='green', bg = 'light green', width= 50)
    label_1003.pack()

    '''
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
    #frame2启动
    frame_1002 = tkinter.Frame(root)
    global text_1001
    text_1001 = tkinter.Text(frame_1002,width=80,height = 300)
    text_1001.pack(pady=10)
    text_1001.insert("1.0",'{user},您好,这是调用qwen的ai助手,请在上面输入框中输入问题\n\n'.format(user = "用户"))

    scrolllbar_1001 = tkinter.Scrollbar(frame_1002)
    scrolllbar_1001.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    scrolllbar_1001.config(command=text_1001.yview)
    frame_1002.pack(pady=5)
    #frame2结束
    tkinter.mainloop()
    return 0

def click1001():
    print('what can i say?')
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
    response =  api_serve(text1)
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


    '''todu:1.上下文功能,2. apikey输入才能使用,不要写死,3.'''