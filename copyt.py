from tkinter import *
def copytext():# it helps in extracting text just by taking a snip from screen
    x1,y1,x2,y2=None,None,None,None;from os import remove
    def getcord():#tkinter function
        op=Tk()
        op.geometry("1600x900");op.state('zoomed')#so that full screen will be covered
        op.overrideredirect(True);op.attributes('-topmost', True)#no button allowances
        op.attributes('-alpha', 0.2)#making translucent
        canvas = Canvas(op,cursor="cross")#canvas to draw rectangle
        canvas.pack( expand=True,fill=BOTH)
        rect = None
        start_x = None
        start_y = None#starting coords of rect
        def key_press(event):#recording starting coords
            nonlocal start_x,start_y,rect,x1,y1
            x1=event.x*(1920/1535);y1=event.y*(1080/864)
            start_x =canvas.canvasx(event.x)
            start_y =canvas.canvasy(event.y)
            rect=canvas.create_rectangle(start_x,start_y,start_x,start_y,outline='red',width=2)
        def press_move(event):#drawing rectangle
            curX = canvas.canvasx(event.x)
            curY = canvas.canvasy(event.y)
            canvas.coords(rect,start_x,start_y,curX,curY) 
        def key_released(event):#get last coords
            nonlocal x2,y2
            x2=event.x*(1920/1535);y2=event.y*(1080/864)
            op.destroy()   
        canvas.bind("<ButtonPress-1>",key_press)
        canvas.bind("<B1-Motion>",press_move)
        canvas.bind("<ButtonRelease-1>",key_released)
        op.mainloop()
    def gettext():#extracting text
        from PIL import ImageGrab,Image;from pytesseract import image_to_string,pytesseract
        try:#check each condition of rect drawing and take ss
            image=ImageGrab.grab(bbox=(x1,y1,x2,y2))
            image.save('sc.png')
        except:
            try:
                image=ImageGrab.grab(bbox=(x2,y1,x1,y2))
                image.save('sc.png')
            except:
                try:
                    image=ImageGrab.grab(bbox=(x2,y2,x1,y1))
                    image.save('sc.png')
                except:
                    image=ImageGrab.grab(bbox=(x1,y2,x2,y1))
                    image.save('sc.png')
        image=Image.open('sc.png')
        pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"#using tesseract
        image_to_text=image_to_string(image,lang='eng')
        remove("sc.png")
        from pyperclip import copy
        copy(image_to_text)
    getcord()
    try:
        gettext()
    except:
        from os import path#just a precaution that ss should not be left
        if path.exists("sc.png"):
            remove("sc.png")
        copytext()
from keyboard import is_pressed;
while True:
    # It records all the keys until escape is pressed
    if is_pressed('c+t'):
        copytext()   
    if is_pressed('esc'):
        exit()    