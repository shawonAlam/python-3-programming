# Let’s add another method, distanceFromOrigin, to see better how methods work. This method will
# again not need any additional information to do its work, beyond the data stored in the instance variables. It will perform a more complex task.

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 2


p = Point(2,3)
print(p.distanceFromOrigin())


# Check Your Understanding: 

# 	1. Create a class called Animal that accepts two numbers as inputs and assigns them respectively to two instance variables: arms and legs. 
# 	Create an instance method called limbs that, when called, returns the total number of limbs the animal has. 
# 	To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. 
# 	Call the limbs method on the spider instance and save the result to the variable name spidlimbs.

class Animal:
    def __init__(self, a,l):
        self.arms = a
        self.legs = l
    def limbs(self):
        return (self.arms + self.legs)
    
spider = Animal(4, 4)
spidlimbs = spider.limbs()
print(spidlimbs)
