class Person:
    def __init__(self , name ,age):
        self.name=name
        self.age=age
    
    def new_function(self):
        print("hello this is "+self.name) 
           
    @staticmethod
    def sun_of_age(a,b,c):
        print(a.age+b.age+c.age)
    @staticmethod    
    def sum(a,b,c):
        return a.age+b.age+c.age
    
p1=Person("John",36)
p2=Person("Xerox",22)
p3=Person("Rif",34)
Person.sun_of_age(p1,p2,p3)
s=Person.sum(p1,p2,p3)
print(s)