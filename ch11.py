import math
result = math.gcd(255, 300)
print(result)

from math import *
result = gcd(255, 300)
print(result)

from tkinter import *
window = Tk()

# 구성요소 작성

window.mainloop()

from tkinter import *
window = Tk()

button = Button(window, text= '클릭하세요')
button.pack()

window.mainloop()


# 윈도우 배치 관리자
# 절대 위치 배치 관리자
from tkinter import *
window = Tk()

w = Label(window, text='박스 #1', bg='red', fg='white')
w.place(x=0, y=0)
w = Label(window, text='박스 #2', bg='green', fg='black')
w.place(x=20, y=20)
w = Label(window, text = '박스 #3', bg = 'blue', fg='white')
w.place(x=40, y=40)

window.mainloop()


# 격자 배치 위치 관리자
from tkinter import *

window = Tk()

l1 = Label(window, text = '화씨')
l2 = Label(window, text = '섭씨')
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text='화씨 -> 섭씨')
b2 = Button(window, text='섭씨 -> 화씨')
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

window.mainloop()


# 버튼 이벤트 처리
from tkinter import *
def process():
    print('안녕하세요?')

window = Tk()

button = Button(window, text='클릭하세요', command=process)
button.pack()

window.mainloop()

# 버튼 이벤트처리
from tkinter import *
def process():
    e2.insert(0, '100')
window = Tk()

l1 = Label(window, text = '화씨')
l2 = Label(window, text = '섭씨')
l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

b1 = Button(window, text = '화씨 -> 섭씨',command = process)
b2 = Button(window, text = '섭씨 -> 화씨')
b1.grid(row = 2, column=0)
b2.grid(row = 2, column=1)

window.mainloop()

# 버튼 이벤트처리2
from tkinter import *

def process():
    temperature = float(e1.get())
    mytemp = (temperature -32)*5/9
    e2.insert(0, str(mytemp))

window = Tk()
l1 = Label(window, text = '화씨')
l2 = Label(window, text = '섭씨')
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text='화씨->섭씨', command=process)
b2 = Button(window, text='섭씨->화씨')
b1.grid(row = 2, column = 0)
b2.grid(row = 2, column = 1)

window.mainloop()



#####
from tkinter import *
def process():
    temperature = float(e1.get())
    mytemp = (temperature-32)*5/9
    e2.insert(0, str(mytemp))

def process2():
    temperature = float(e2.get())
    mytemp = (temperature*9/5)+32
    e1.insert(0, str(mytemp))

window = Tk()

l1 = Label(window, text='화씨', font= 'helvetica 16 italic')
l2 = Label(window, text='섭씨', font= 'helvetica 16 italic')
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window, bg = 'green', fg = 'yellow')
e2 = Entry(window, bg = 'green', fg = 'yellow')
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text='화씨->섭씨',command = process)
b2 = Button(window, text='섭씨->화씨', command = process2)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

window.mainloop()


#####
# 윈도우 창 메뉴 만들기
###
import tkinter as tk

def open():
    pass

def quit():
    window.quit()

window = tk.Tk()

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)

filemenu.add_command(label = '열기', command = open)
filemenu.add_command(label = '닫기', command = quit)

menubar.add_cascade(label = '파일', menu = filemenu)

window.config(menu = menubar)
window.mainloop()

#####
# MyPaint
###
from tkinter import *

def paint(event):
    x1, y1 = (event.x-1), (event.y+1)
    x2, y2 = (event.x-1), (event.y+1)
    canvas.create_oval(x1, y1, x2, y2)

window = Tk()
canvas = Canvas(window)
canvas.pack()
canvas.bind('<B1-Motion>', paint)
window.mainloop()


#####
# image
###
from PIL import Image, ImageTk
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width= 500, height = 500)
canvas.pack()

img = Image.open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/lenna.png')

tk_img = ImageTk.PhotoImage(img)

canvas.create_image(250, 250, image=tk_img)

window.mainloop()


from PIL import Image, ImageTk
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width = 500, height = 500)
canvas.pack()

im = Image.open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/lenna.png')

out = im.rotate(45)
tk_img = ImageTk.PhotoImage(out)

canvas.create_image(250, 250, image=tk_img)
window.mainloop()

from PIL import Image, ImageTk, ImageFilter 
import tkinter as tk

window = tk.Tk( )
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack( )

im = Image.open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/lenna.png')

out = im.filter(ImageFilter.BLUR) #이미지를 흐리게 합니다.

tk_img = ImageTk.PhotoImage(out)

canvas.create_image(250, 250, image=tk_img)
window.mainloop( )


###
from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from tkinter import filedialog as fd

im = None
tk_img = None

def open():
    global im, tk_img
    fname = fd.askopenfilename()
    im = Image.open(fname)
    tk_img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

def quit():
    window.quit()

def image_rotate():
    global im, tk_img
    out = im.rotate(45)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

def image_blur():
    global im, tk_img
    out = im.filter(ImageFilter.BLUR)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

window = tk.Tk()
canvas = tk.Canvas(window, width = 500, height = 500)
canvas.pack()

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
ipmenu = tk.Menu(menubar)

filemenu.add_command(label='열기', command = open)
filemenu.add_command(label = '종료', command = quit)
ipmenu.add_command(label = '영상회전', command = image_rotate)
ipmenu.add_command(label = '영상 흐리게', command = image_blur)

menubar.add_cascade(label = '파일', menu = filemenu)
menubar.add_cascade(label = '영상처리', menu = ipmenu)

window.config(menu=menubar)
window.mainloop()




#####
# Matplotlib
###
from matplotlib import pyplot as plt

x=[1,2,3]
y=[1,2,3]

plt.plot(x,y,marker='o')
plt.title('My Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(['test'])
plt.show()

from matplotlib import pyplot as plt
import csv
from matplotlib import font_manager, rc
#font_name = font_manager.FontProperties(fname='').get_name()
rc('font', family='AppleGothic')

infile = open('/Users/heechankang/projects/pythonworkspace/sigansoonsak/weather_input.csv', 'r')
data = csv.reader(infile)

x = []
y = []

for line in data:
    x.append(line[0])
    y.append(float(line[2]))

plt.plot(x, y, marker = 'o')
plt.title('2009년 대관령 월평균 강수랑')
plt.xlabel('월')
plt.ylabel('강수량(mm)')
plt.show()
infile.close()