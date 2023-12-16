"""if  it looks like a duck and quacks like a duck"""

class Duck:    #duck class
    def sound(self):
        print("quack quack")

class Dog:   #dog class
    def sound(self):
        print("bhow bhow")

class Cat:
    def sound(self):
        print("meww meww")

#i take(define) one function
#its tke one argument
def anysound(obj):
    obj.sound()    #sound function

x=Duck()
anysound(x)
y=Dog()
anysound(y)
z=Cat()
anysound(z)
