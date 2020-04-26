from PIL import Image, ImageDraw
import os
import random

def getBit(n):
    assert n <= 255
    b = []
    while n > 0:
        b.append(n % 2)
        n = n // 2
    while len(b) < 8:
        b.append(0)
    b.reverse()
    return b

def getByte(b):
    res = 0
    for i in b:
        res = res << 1
        res += i
    return res

def getBitList(text, key):
    print("alo")
    text = bytes(text, encoding="utf_8")
    print("alo2")
    text = list(text)
    random.seed(key)

    for i in range(len(text)):
        text[i] = (text[i]+random.randint(5, 255)) % 254+1
    res = []
    for i in text:
        res += getBit(i)
    return res

def getStrFromBit(b,key):
    res=[]
    for i in range(len(b)//8):
        s=[]
        for j in range(8):
            s.append(b[i*8+j])
        s1=getByte(s)
        if s1!=0:
            res.append(s1)
    random.seed(key)
    for i in range(len(res)):
        res[i]=(res[i]-random.randint(5, 255)) % 254-1

    res=bytes(res).decode('utf-8')
    return res

def shifr(imagePut, key, text):
    image = Image.open(imagePut)
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
    width = image.size[0]  # Определяем ширину
    height = image.size[1]  # Определяем высоту
    pix = image.load()  # Выгружаем значения пикселей
    bitText = getBitList(text, key)
    for i in range(32):
        bitText.append(0)
    for x in range(width):
        if len(bitText) <= 0:
            break
        for y in range(height):
           r = getBit(pix[x, y][0]) #узнаём значение красного цвета пикселя
           g = getBit(pix[x, y][1]) #зелёного
           b = getBit(pix[x, y][2]) #синего
           if (len(bitText) > 0):
               r[6]=bitText[0]
               del bitText[0]
           else:
               r[6] = 0
           if (len(bitText) > 0):
               r[7] = bitText[0]
               del bitText[0]
           else:
               r[7] = 0

           if (len(bitText) > 0):
               g[6] = bitText[0]
               del bitText[0]
           else:
               g[6] = 0
           if (len(bitText) > 0):
               g[7] = bitText[0]
               del bitText[0]
           else:
               g[7] = 0

           if (len(bitText) > 0):
               b[6] = bitText[0]
               del bitText[0]
           else:
               b[6] = 0
           if (len(bitText) > 0):
               b[7] = bitText[0]
               del bitText[0]
           else:
               b[7] = 0
           draw.point((x, y), (getByte(r), getByte(g), getByte(b))) #рисуем пиксель
    image.save(imagePut+"res.png", "PNG")  # не забываем сохранить изображение
    return imagePut+"res.png"

def deshifr(imagePut, key):
    image = Image.open(imagePut)
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
    width = image.size[0]  # Определяем ширину
    height = image.size[1]  # Определяем высоту
    pix = image.load()  # Выгружаем значения пикселей
    bitText = []
    triger=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    flagGl=False
    for x in range(width):
        if flagGl:
            break
        for y in range(height):
           flag = True
           for i in range(32):
                if triger[i] == 1:
                    flag = False
                    break
           if flag:
                print("kek")
                flagGl=True
                break

           r = getBit(pix[x, y][0]) #узнаём значение красного цвета пикселя
           g = getBit(pix[x, y][1]) #зелёного
           b = getBit(pix[x, y][2]) #синего
           bitText.append(r[6])
           bitText.append(r[7])
           bitText.append(g[6])
           bitText.append(g[7])
           bitText.append(b[6])
           bitText.append(b[7])
           del triger[0]
           triger.append(r[6])
           del triger[0]
           triger.append(r[7])
           del triger[0]
           triger.append(g[6])
           del triger[0]
           triger.append(g[7])
           del triger[0]
           triger.append(b[6])
           del triger[0]
           triger.append(b[7])
    #print(triger)
    for i in range(32):
        bitText.pop()

    st=getStrFromBit(bitText, key)
    return st    


def handle_uploaded_file(f):  
    with open('decrypt/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)