class Queue:

    def __init__(self):
        self.container = []
        
    def __is_empty(self):
        if len(self.container)==0:
            return True
        else:
            False

    def addItem(self,data):
        self.container.append(data)    

    def removeItem (self):
        if not self.__is_empty():
            
            self.container.pop(0)   
        else:
            print ("Queue is empty")     

    def containeSize(self):
        numberofnumbers = len (self.container)
        return numberofnumbers
    def biggestNumber(self):
        number = max(self.container)
        return number

newlist = Queue()
for i in range(0,100,5):
    newlist.addItem(i)
newlist.containeSize()
print(newlist.containeSize())
print(newlist.container)
