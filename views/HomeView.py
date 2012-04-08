from Tkinter import *
from controllers.HomeController import *

#This class generates the UI of home (the first) page of the program
class HomeView:
    #This stores an instance of the program window
    window = None
    #This stores an instance of the program menu
    menu = None
    
    #This function is called when the class is made
    def __init__(self, window):
        self.window = window
        #Make an inner frame (like a box) inside the main window
        frame = Frame(window)
        frame.pack()
        #Make a label inside that box
        helloLabel = Label(frame, text="Hello world", width=80, height=20)
        helloLabel.pack()
        self.createMenu()
        
    #Add the menu at the top with quit and load file
    def createMenu(self):
        self.menu = Menu(self.window)
        self.menu.add_command(label="Quit", command=self.window.quit)
        self.menu.add_command(label="Load file")
        self.window.config(menu=self.menu)
      
    #Sets the action of the load file button, must be passed a lambda function
    def setLoadFileAction(self, function):
        self.menu.entryconfig(2, command=function)
        
        