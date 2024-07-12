import datetime
class LiberaryItem:
    def __init__(self, Title , Author_artist ,Itemid , onloan ):
        
        self.__Title=Title
        self.__Author_Artist=Author_artist
        self.__ItemId=Itemid
        self.__OnLoan=onloan
        self.__Duedate=datetime.date.today()
        
    def gettitle(self):
            return self. __Title
        
    def getartist(self):
        return self.__Author_Artist
    
    def getitemid(self):
        return self.__ItemId
    
    def getonloan(self):
        return self.__OnLoan
    
    def Borrowing(self):
        self.__OnLoan=True
        self.__Duedate+=datetime.timedelta(weeks=3)
    
    def Returning(Self):
        self.__OnLoan=False
        
                  
        