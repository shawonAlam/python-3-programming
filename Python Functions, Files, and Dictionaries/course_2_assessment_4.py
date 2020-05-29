# 1.Write a function called int_return that takes an integer as input and returns the same integer.

def int_return(i):
    return i

print(int_return(int (input("Enter a number:"))))



# 2.Write a function called add that takes any number as its input and returns that sum with 2 added.

def add(a):
    return a+2

print(add(int(input("Enter a number: "))))




# 3.Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.

def change(ch):
    return (ch +  "Nice to meet you!")

print(change(str(input("Enter your name: "))))



# 4.Write a function, accum, that takes a list of integers as input and returns the sum of those integers.

def accum(li):
    sum = 0
    for item in li:
        sum += int(item)
    return sum
        
print(accum([2,4,6,8]))

        

# 5.Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.

def length(li):
    c = 0
    for item in li:
        c += 1
    if c >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"

print(length([2,4,6,8,4,6,8]))



# 6.You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals. https://github.com/shawonAlam

def divide(x):
    return x/2

def sum(y):
    p = divide(y) + 6
    return p

print(sum(int(input("Enter a num: "))))
