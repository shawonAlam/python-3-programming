# 8. Write a function named same that takes a string as input, and simply returns that string.


def same(y):
    return y 
samme = input("Write something: ")
print(same(samme))


# 9. Write a function called same_thing that returns the parameter, unchanged.

def same_thing(y):
    return y
p = "unchanged"
print(same_thing(p))


# 10. Write a function called subtract_three that takes an integer or any number as input, and returns that number minus three.                                                                                     https://github.com/shawonAlam


def subtract_three(y):
    y = y-3
    return y

item = int(input("Write a number: "))
print(subtract_three(item))


# 11. Write a function called change that takes one number as its input and returns that number, plus 7.                                                                                               https://github.com/shawonAlam


def change(y):
    y = y +7
    return y

item = int(input("write a number: "))
print(change(item))

# 12. Write a function named intro that takes a string as input. Given the string “Becky” as input, the function should return: “Hello, my name is Becky and I love SI 106.”


def intro(name):
    name = "Hello, my name is {} and I love SI 106.".format(name)
    return name

item = str(input("Enter your name: "))
print(intro(item))
    

# 13. Write a function called s_change that takes one string as input and returns that string, concatenated with the string ” for fun.”.


def s_change(word):
    word = word + " for fun."
    return word
    
    
item = str(input("write something: "))
print(s_change(item))

# 14. Write a function called decision that takes a string as input, and then checks the number of characters. If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”. https://github.com/shawonAlam

def decision(value):
    c = len(value)
    #for ch in value:
        #c += 1    
    if c > 17:
        return "This is a long string"
    else:
        return "This is a short string"
    

strValue = str(input("Write something: "))
print(decision(strValue))
        
