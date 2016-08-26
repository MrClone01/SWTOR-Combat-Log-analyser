import re
#This is a class that represents each line of the log file
class EventModel:
    
    rex = re.compile("\[@(.*?)\]")
    #The source player in the log line
    source = None
    #The target player in the log line
    target = None
    
    def __init__(self, line=None):
        if(line != None):
            rexRes = self.rex.finditer(line)
            if(rexRes == None):
                return
            matches = list(rexRes)
            #If there is anything wrong with what was matched then don't set the value
            if(len(matches) != 2):
                return
            self.source = self.__trimTag(matches[0].group(0))
            self.target = self.__trimTag(matches[1].group(0))
     
    #Remove [@ from the start and ] from the end of the player names
    def __trimTag(self, string):
        string = string[2:-1]
        return string