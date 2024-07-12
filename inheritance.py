class person:
    
    def __init__(self,fname,lname):
        self.__fname=fname
        self.__lname=lname
        
    def printa(self):
        print(self.fname,self.lname)
    
class student(person):
    def __init__(self , fname ,lname ,year):
        super().__init__(fname,lname)
        self.year=year
    
    def printa(self):
        print(self.fname,self.lname,self.year)    
    
@staticmethod
def sum(a,b):
    return a.fname+b.fname    
    
    
obj=person("lkkk","llklk")
x=student("ggggg","dgdfdf",2024)
obj.printa()        
x.printa()
y=sum(obj,x)
print(y)