'''本代码用于导入图片,生成一个图像对象和它的长宽元组'''
from tkinter import *
from PIL import Image , ImageTk
def image_input (imagePath):
    #本代码用于导入图片,生成一个图像对象和它的长宽元组
    if  not  isinstance(imagePath , str):
        return 'this is not a imagePath'
    image_orinige = Image.open(imagePath)
    image_width, image_height = image_orinige.size
    return image_orinige, image_width, image_height
