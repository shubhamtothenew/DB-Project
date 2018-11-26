# import external libraries
from tkinter import *

from tkinter import messagebox

def popup():
    """ This function inputs the current INR rate with dollar"""

    # Intialising the rate
    rate = 1

    def validator():
        ''' This function check the user input
            whether it is valid or not'''
        nonlocal rate, window
        # Getting the text from input field
        try:
            rate = float(rate_textfield.get())
            if rate == 0 or rate < 0:
               raise ValueError
        except ValueError:
            messagebox.showwarning('WARNING','Please write valid input in integer or float')
        else:
         window.quit()

    # Creating the Tkinter object
    window = Tk()
    # Resizing the window
    window.geometry('400x200')

    window.title('Input Reader')
    # Label
    Label(window, text='Please Enter The Current INR Rate').pack()
    # input field
    rate_textfield = Entry(window)
    rate_textfield.pack()
    # button
    Button(window, text='ok', command = validator).pack()

    # start mainloop
    window.mainloop()

    return rate