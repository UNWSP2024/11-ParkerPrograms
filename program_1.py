# Nathan Parker
# 04/07/25
# Program #1

import tkinter

class FavVerse:

    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Display a title
        self.main_window.title('2 Corinthians 5:15')

        # Create a label widget
        self.label = tkinter.Label(self.main_window, text = '''And He died for all, that those 
who live might no longer live 
for themselves but for Him who 
for their sake died and was raised.''', borderwidth = 5, relief = 'ridge')

        # pack the label with internal and external padding
        self.label.pack(ipadx=10, ipady=10, padx=20, pady=20)

        # Enter the tkinter main loop
        tkinter.mainloop()

# Create an instance of the FavVerse class
if __name__ == '__main__':
    verse = FavVerse()

