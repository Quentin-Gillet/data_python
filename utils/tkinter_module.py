from tkinter import *


def init_main_window():
    window = Tk()

    topFrame = Frame(window)
    topFrame.pack()
    
    bottomFrame = Frame(window)
    bottomFrame.pack(side=BOTTOM)

    button1 = Button(topFrame, text="Submit 1", fg="red")
    button1.pack(side=LEFT)
    button2 = Button(topFrame, text="Submit 2", fg="green")
    button2.pack(side=LEFT)

    button3 = Button(bottomFrame, text="Submit 3", fg="blue")
    button3.pack(side=BOTTOM)
    
    window.mainloop()


if __name__ == '__main__':
    init_main_window()

