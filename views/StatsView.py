from Tkinter import *

#Defines the UI of the stats window
class StatsView:
    window = None
    menu = None
    listBox = None
    
    #Called when the UI is initialized
    def __init__(self, window):
        self.window = window
        frame = Frame(window)
        frame.pack()
        #Makes a list box
        self.listBox = Listbox(frame, width=80, height=20)
        self.listBox.pack()
        self.createMenu()
        
    #Creates the menu with the exit button
    def createMenu(self):
        self.menu = Menu(self.window)
        self.menu.add_command(label="Quit", command=self.window.quit)
        self.window.config(menu=self.menu)
     
    #Adds items to the list in the window
    def addListItem(self, string):
        self.listBox.insert(END, string)
        
        