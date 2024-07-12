class person:
    
    def __init__(self , fname , lname ,age):
        self.__fname=fname
        self.__lname=lname
        self.__age=age
    
    
    def set_fname(self,x):
        self.__fname=x    
    
    
    def get_fname(self):
        return self.__fname   
    
      
    def set_lname(self,x):
        self.__lname=x    
    
    
    def get_lname(self):
        return self.__lname    
    
    def set_age(self,x):
        self.__age=x    
    
    
    def get_age(self):
        return self.__age    


obj=person("Raiyan","BUhiyan",30)
print(obj.get_fname()) 
obj.set_fname("fahad") 
print(obj.get_fname()) 

