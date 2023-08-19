from tkinter import *
import tkinter.messagebox as msg
import tkinter.font as font

root = Tk()
root.geometry("553x784")
root.resizable(False,False)
bg = PhotoImage(file="python_final_front_page.png")
canvas1 = Canvas(root, width = 553, height = 784)
canvas1.pack()
canvas1.create_image(0,0, image = bg, anchor = "nw")
def openwindow():
    root.destroy()
    import dataset

start_btn = Button(root, text="START", height = 2, width = 16, command = openwindow,bg='#545454',fg='#ffffff')
start_btn_canvas = canvas1.create_window(210,550,anchor="nw", window = start_btn)

root.mainloop()