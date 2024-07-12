Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("hello")
hello
// lets start
SyntaxError: invalid syntax
#lets start
"""
dgsgsg
"""
'\ndgsgsg\n'
x="hello"
print(type(x))
<class 'str'>
print(x[1])
e
for x in "banana"
SyntaxError: incomplete input
for x in "banana"    print(x)
SyntaxError: invalid syntax
for x in "banana" :
    print(x)

    
b
a
n
a
n
a
txt =" todays exam was good"
print("exam" not in txt)
False
print("exam" in txt)
True
print(txt[2:5])
oda
print(txt[:5])
 toda
print(isalnum(txt))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(isalnum(txt))
NameError: name 'isalnum' is not defined
b=txt.isalnum()
print(b)
False
a=330
b=34
print("A")  if a>b else print("=") if a==b else print("B")
A
# ignore
if b>a :
    pass

fruits = ["apple" ,"banana" ,"cherry"]
for x in fruits :
    if x==" banana":
        pass
    print(x)

    
apple
banana
cherry
for x in range(6) :
    print(x)

    
0
1
2
3
4
5
for x in range(2,6):
    print(x)

    
2
3
4
5
for x in range(2 , 30 , 3.0)
SyntaxError: incomplete input
for x in range( 2.0 , 30.0 ,3.0) :
    print(x)

    
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    for x in range( 2.0 , 30.0 ,3.0) :
TypeError: 'float' object cannot be interpreted as an integer
for x in range( 0 , 30 , 1):
    print(x)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
i=1
while i<6 :
    print(i)
    if i==3:
        break
    i+=1

    
1
2
3
def fun( c1 , c2 , c3):
    print("the youngest child" + c3)

    
fun(c1="sd" , c2="fdf" , c3="fd")
the youngest childfd
def func(food):
    for i in food :
        print(i)

        
food=["apple" ,"mango" , "cherry"]
func(food)
apple
mango
cherry
class complex_number:
    def _init_(self,real, comple):
        self.real=real
        self.comple=comple

        
class complex_number:
    def _init_(self,real, comple):
        self.real=real
        self.comple=comple
    def repse():
        print(real"+""i"comple)
        
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> class complex_number:
...     def _init_(self,real, comple):
...         self.real=real
...         self.comple=comple
...     def repse():
...         print(real,"+","i",comple)
... 
...         
>>> p1=complex_number(2,5)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    p1=complex_number(2,5)
TypeError: complex_number() takes no arguments
>>> p1=complex_number(2,5)class complex_number:
...     def _init_(self,real, comple):
...         self.real=real
...         self.comple=comple
...     def repse(self):
...         print(real,"+","i",comple)
...         
SyntaxError: invalid syntax
>>> class complex_number:
...     def _init_(self,real, comple):
...         self.real=real
...         self.comple=comple
...     def repse(self):
...         print(real,"+","i",comple)
... 
...         
>>> p1=complex_number(2,5)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    p1=complex_number(2,5)
TypeError: complex_number() takes no arguments
>>> class ComplexNumber:
...     def __init__(self, real, comple):
...         self.real = real
...         self.comple = comple
... 
...     def repse(self):
...         print(self.real, "+", "i", self.comple)
...         
... p1 = ComplexNumber(2, 5)
... p1.repse()
... 
SyntaxError: invalid syntax
