from tkinter import * # import tkinter 

root = Tk() # creates tkinter windows and sets it to the root variable
def printhi(): # Creates a defintion (A definiton is a code which can be called on)
	print("Hi") # The code in the definition in this case it prints Hi
title_label = Label(root,text="This is a test") # creates a Label for the root windows and sets the text
title_label.pack() # displays the label with the pack function

hi_button = Button(root,text="Click Me!",command=printhi)# Creates a button and applies it to the root window, the text arg sets the text on the button and the command arg sets the function to call when pressed.
hi_button.pack()# Displays The Button
