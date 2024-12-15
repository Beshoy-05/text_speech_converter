from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gtts import gTTS
import os

def text_to_speech():
    text=myinput.get().strip()
    if text:
        speech=gTTS(text=text,lang="en")
        filename="converted_text.mp3"
        speech.save(filename)
        os.system(f"start {filename}")
        messagebox.showinfo(title="Success",message="convert complete")
    else:
        messagebox.showerror(title="failed",message="Error,enter some text")    

def exit_app():
    root.quit()

def clear_text(): 
    
    if myinput.get():
        myinput.delete("0",END) 
        messagebox.showinfo("Info", "Text cleared")
    else:
        messagebox.showerror("wrong", "enter text to clear")
 

root = Tk()
root.title("Text to Speech Converter")
root.geometry("500x300")
root.config(bg="black")

mylabel = Label(root, text="Text to Speech",fg="white",bg="black", font=("Arial", 20, "bold"))
mylabel.pack(pady=10)

my_sec_label = Label(root, text="Enter your text",fg="white",bg="black", font=("Arial", 14))
my_sec_label.pack(pady=10)

myinput = Entry(root, width=45,font=("Arial", 10))
myinput.pack(pady=20)
mybtn_play =ttk.Button(root, text="Play", command=text_to_speech)
mybtn_play.place(rely=0.6,x=110)

mybtn_exit = Button(root, text="Exit",pady=3, bg="red",padx=25, command=exit_app)
mybtn_exit.place(rely=0.6,x=210)

mybtn_set = ttk.Button(root, text="Set",command=clear_text)
mybtn_set.place(rely=0.6,x=310)
root.mainloop()
