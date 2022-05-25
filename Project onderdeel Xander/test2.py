from tkinter import *

def submit():
    test = answer.get()
    if (test != ''):
        print(test)
    else:
        print('nothing')

def delete():
    answer.delete(0, 'end')

interface = Tk()
interface.geometry("800x480")
interface.config(background='grey')

question = Label(interface, text="Off which city do you want to know the weather?", background="grey", foreground="white", font=("BloomSpeak Body", 20))
question.pack(anchor="center")
answer = Entry(interface)
answer.config(font=("BloomSpeak Body", 25), width=40)
answer.pack(anchor="center")

deleteButton = Button(interface, text="delete", command=delete, font=("BloomSpeak Body", 25), width= 25)
deleteButton.pack(anchor="center")

submitButton = Button(interface, text="submit", command=submit, font=("BloomSpeak Body", 25), width= 25)
submitButton.pack(anchor="center")

interface.mainloop()