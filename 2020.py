

import PIL #加载pillow处理图片库
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import imageio

font = ImageFont.truetype("C:\Windows\Fonts\msyhbd.ttc", 40)#设置所使用的字体


while 1:
    
    word=input("输入您的寄语(5-8个汉字左右长度为宜，可用空格调整居中）：")

    gif_images = []
    path="操作目录/"
    pathn="生成目录/"


    for i in range(1,11):
        pathp=path+str(i)+".jpg"

        #画图
        im1 = Image.open(pathp)
        draw = ImageDraw.Draw(im1)
        if i<6:
           draw.text((140,200),word, (255,105,180), font=font)

        else:
           draw.text((140, 200),word, (255,20,147), font=font)

        print(pathp)

        draw = ImageDraw.Draw(im1)#Just draw it!
        pathq=pathn+str(i)+".jpg"
        im1.save(pathq)
        gif_images.append(imageio.imread(pathq))


    imageio.mimsave("2020.gif",gif_images,fps=10)
