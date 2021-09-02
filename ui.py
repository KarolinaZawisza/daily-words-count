from tkinter import *

BG = '#9ea3b4'
FG = '#6193ac'
AC = '#FFE3E3'
LC = '#E4D8DC'
FONT_NAME = 'courier'

class AppInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title('Words Tracker')
        self.window.config(padx=20, pady=20, bg=LC)

        self.words_label = Label(text='Words:')
        self.words_label.config(font=(FONT_NAME, 13, 'bold'), bg=LC, fg=FG)
        self.words_label.grid(column=0, row=0)

        self.words_entry = Entry()
        self.words_entry.grid(column=1, row=0, padx=(3, 10))

        self.add_button = Button(text='  Add  ')
        self.add_button.config(border=0, bg=AC, fg=FG, font=(FONT_NAME, 10, 'bold'))
        self.add_button.grid(column=2, row=0)

        self.date_label = Label(text='Date')
        self.date_label.config(font=(FONT_NAME, 13, 'bold'), bg=LC, fg=BG)
        self.date_label.grid(column=1, row=1, pady=(10, 5))

        self.log_label = Label(text=' ')
        self.log_label.config(font=(FONT_NAME, 5, 'bold'), bg=LC, fg=BG)
        self.log_label.grid(column=1, row=2)

        self.window.mainloop()
