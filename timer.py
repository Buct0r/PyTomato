from tkinter import *
from tkinter import messagebox
from threading import Timer
import webbrowser

window = Tk()

def timer(label):
    global t
    global t2

    def work():
        global t2
        #print("Timer is up")
        messagebox.showinfo(title="Work", message="Work is up!\nEnjoy your break!")
        t2 = Timer(300, lambda : pause(label))
        #print("Pause started")
        t2.start()

    def pause(label):
        #print("Break is up")
        messagebox.showinfo(title="Pause", message="Break is up!\n Timer finished")
        label.config(text="Timer stopped")

    t = Timer(1500, work)
    #print("Timer started")
    label.config(text="Timer started")
    t.start()


def stop(label):
    if messagebox.askyesno(message="Do you really want to stop the timer?\n You will have to restart it again!"):
        try:
            t.cancel()
            t2.cancel()
            #print("Timer stopped")
            messagebox.showinfo(message="Timer stopped")
            label.config(text="Timer stopped")
        except NameError:
            try:
                t.cancel()
                #print("Time stopped")
                messagebox.showinfo(message="Timer stopped")
                label.config(text="Timer stopped")
            except NameError:
                messagebox.showinfo(message="There is no timer active right now")
    else:
        messagebox.showinfo(message="The timer will not be stopped")

#def pause():
#    pass                                IMPORTANTE implementare il tasto pausa

def infoWindow():

    info_window = Toplevel()
    info_window.title("Info")
    info_window.geometry("600x600")
    info_window.config(bg="green")
    info_window.resizable(False, False)

    def callback(url):
        webbrowser.open_new(url)

    def callback2(url):
        webbrowser.open_new(url)

    link1 = Label(info_window, text="GitHub repo", fg="blue", cursor="hand2")
    link1.bind("<Button-1>", lambda e: callback("https://github.com/Buct0r/PyTomato")) 
    link2 = Label(info_window, fg="blue", cursor="hand2", text="Wikipedia")
    link2.bind("<Button-1>", lambda e: callback2("https://en.wikipedia.org/wiki/Pomodoro_Technique"))
    link2.config(bg="green", font=("Arial"))
    link1.config(bg="green", font=("Arial"))

    info_label = Label(info_window)
    info_label.config(text="PyTomato: A pomodoro timer made with Python.\n Developed by Buct0r\nThank you for downloading", justify="center", bg="green", font=("Arial", 20))
    info_label.pack(side=TOP)
    info_label2 = Label(info_window)
    info_label2.config(bg="green", font=("Arial", 10), justify="center", text="The Pomodoro Technique is a time management method developed by Francesco Cirillo\n in the late 1980s. It uses a kitchen timer to break work into intervals,\n typically 25 minutes in length, separated by short breaks. Each interval is known as a pomodoro,\n from the Italian word for tomato, after the tomato-shaped kitchen timer\n Cirillo used as a university student.")
    info_label2.pack()
    info_label2.place(relx=0.5, rely=0.5, anchor=CENTER)
    link2.pack()
    link2.place(relx=0.5, rely=0.6, anchor=CENTER)
    link1.pack(side=BOTTOM)
    info_window.mainloop()


buttonStart = Button(window)
buttonAbort = Button(window)
#buttonPause = Button(window)
buttonInfo = Button(window)
label = Label(window)

icon = PhotoImage(file="logo.png")


window.title("PyTomato")
window.iconphoto(True, icon)
window.geometry("500x500")
window.config(bg="#0dd8fc")
window.resizable(False, False)
buttonStart.config(text="Start", command= lambda: timer(label), height=20, width=30, font=("Arial",10), bg="green", activebackground="green")
buttonAbort.config(text="Abort timer", command= lambda: stop(label),  height=20, width=34, font=("Arial", 10), bg="red", activebackground="red")
buttonInfo.config(command=infoWindow, text="Info", bg="black", fg="white", activebackground="black", activeforeground="white", font=("Arial"))
buttonInfo.pack(side=RIGHT)
buttonInfo.place(y=0)
label.config(bg="#0dd8fc", font=("Arial", 10, "bold"))
buttonStart.pack(side=LEFT)
buttonAbort.pack(side=RIGHT)
label.pack()
label.place(x=210)
window.mainloop()