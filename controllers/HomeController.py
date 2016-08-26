from views.HomeView import *
from views.StatsView import *
from models.EventModel import *
import tkFileDialog
import tkMessageBox

#This class handles all the main controllers of the program
class HomeController:
    
    #Called to generate the first window of the program
    @staticmethod
    def homeAction():
        root = Tk()
        view = HomeView(root)
        view.setLoadFileAction(lambda: HomeController.loadFileAction())
        root.mainloop()
        
    #Shows the select file dialogue
    @staticmethod
    def loadFileAction():
        file = tkFileDialog.askopenfile(mode="r", title="Choose a file")
        if(file == None):
            tkMessageBox.showwarning("Open file", "Cannot open this file or no file selected")
            return
        events = list()
        #Read every line of the log file
        for line in file:
            model = EventModel(line)
            if((model.source != None) and (model.target != None)):
                events.append(model)
        file.close()
        HomeController.viewStatsAction(events)
      
    #Shows another window with a list of all the events in the file
    @staticmethod
    def viewStatsAction(events):
        root = Tk()
        view = StatsView(root)
        for event in events:
            view.addListItem(event.source + " > " + event.target)
        root.mainloop()
        