import tkinter as tk

#create a window
root = tk.Tk();
width,height = 400,400
dis_width = root.winfo_screenwidth()
dis_heigth = root.winfo_screenheight()

left = int(dis_width/2 - width/2)
top = int(dis_heigth/2 - height/2)
root.geometry(f'{width}x{height}+{left}+{top}')  #width*heigth + LEFT+TOP

root.title("hello world")
root.resizable(True,False); #only can resizeable from laft to rigth 
root.iconbitmap('one-finger-click-black-hand-symbol_icon-icons.com_64350.ico')
#run the window
root.mainloop();
print("Hello hello!")