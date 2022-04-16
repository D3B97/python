import tkinter

gui = tkinter.Tk()
gui.geometry("500x200")
## containt are write here
gui.title("Countdown")
button = tkinter.Button(gui, text="Start", command= gui.destroy)
button.pack()
button.grid()

##

gui.mainloop()