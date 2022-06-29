from tkinter import *
import time


root = Tk()
root.title("amirali")
width = 600
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2)- (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="light green")


def tick():
    setTime = time.strftime('%I: %M %S %p ')
    clock.config(text=setTime )
    clock.after(200, tick)


Top = Frame(root, width=600, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=600)
Mid.pack(side=TOP, expand=1)


lbl_title = Label(Top, text="Digital Clock", width=600, font=("Titr", 25))
lbl_title.pack(fill=X)

clock = Label(Mid, font=('times', 50 , 'bold'), fg="red", bg="light blue")
clock.pack()



if __name__ == '__main__':
    tick()
    root.mainloop()
