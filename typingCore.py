from tkinter import *


root = Tk()

sample_buff = StringVar()
sample_buff.set("default")

sample = Label(root, textvariable = sample_buff)
sample.pack()

typing_buff = StringVar()
typing_buff.set("")

def check_input(event):
    print("pressed", repr(event.char))
    sample_text = sample_buff.get()
    typing_text = typing_buff.get()
    type_over = len(typing_text)
    print(type_over)
    if(sample_text[type_over] == event.char):
        typing_text += event.char
        typing_buff.set(typing_text)

typing = Label(root, textvariable = typing_buff)
typing.focus_set()
typing.pack()
typing.bind("<Key>", check_input)



root.mainloop()
