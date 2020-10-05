from PIL import Image,ImageDraw, ImageFont, ImageFilter

def font_select():
    x=random.randint(1,3)
    if x==1:
        a=ImageFont.truetype('f:\\Kunj\\computer project\\ariblk.ttf',40)
    elif x==2:
        a=ImageFont.truetype('f:\\Kunj\\computer project\\segoesc.ttf',40)
    else:
        a=ImageFont.truetype('f:\\Kunj\\computer project\\seguili.ttf',40)
    return (a)

def color_select():
    a=random.randint(0,225)
    b=random.randint(0,225)
    c=random.randint(0,225)
    x='rgb('+str(a)+','+str(b)+','+str(c)+')'
    return (x)

import random

st=''
s="qwertyuioplkjhgfdsazxcvbnm1209873654QWERTYUIOPASDFGHJKLZXCVBNM"
for i in range(8):
    a=random.randint(0,61)
    st=st+s[a]

image=Image.open('f:\\Kunj\\computer project\\captcha_pic.jpg')
draw=ImageDraw.Draw(image)
position=150
for i in st:    
    color=color_select()    
    #color='rgb(0,0,0)'
    font=font_select()    
    draw.text((position,60), i, fill=color, font=font)
    position=position+33

#image.show()
blur=image.filter(ImageFilter.BLUR)
blur.show()
