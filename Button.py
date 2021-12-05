from tkinter import *

window = Tk()
window.title('QUIZ GAME')
window.configure(bg='purple')
heading = Label(window, text="QUIZ GENERATOR", bg='purple', fg='yellow').pack()

def play():
	myLabel = Label(window, text="Loading....", bg='purple', fg='yellow')
	myLabel.pack()

myButton = Button(window, text="PLAY NOW!", command=play, pady=50, padx=50, bg='yellow', fg='purple')
myButton.pack()

window.mainloop()