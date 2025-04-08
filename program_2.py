# Nathan Parker
# 04/07/25
# Program #2

import tkinter

class Info:

    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Display a title
        self.main_window.title('Info')

        # Create two frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create a blank label in the top frame
        self.value = tkinter.StringVar()
        self.name_address_label = tkinter.Label(self.top_frame, textvariable = self.value)

        # Create two buttons in the bottom frame
        self.name_address_button = tkinter.Button(self.bottom_frame, text = 'Show Info', command = self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)

        # pack the label
        self.name_address_label.pack()

        # Pack the buttons
        self.name_address_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # define the show_info function
    def show_info(self):
        self.value.set('Nathan Parker\n6383 Hartford Circle\nLino Lakes, MN 55038')

# Create an instance of Info class
if __name__ == '__main__':
    show_info = Info()

