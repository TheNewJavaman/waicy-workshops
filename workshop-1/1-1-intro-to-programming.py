# 1-1-intro-to-programming.py
# Teaches the basics of programming

# 1. Storing information with variables
#    In Python, create a new variable like so:
#        [name] = [value]
#    There are a few types of variables; each holds a different type of information
#    Programmers can also create their own types, but we'll only deal with primitives (the built-in types)
#        integer/int  : holds a non-fraction number; can be positive, negative, or zero
#        float        : holds a fraction number, but can also represent an integer without a fraction
#        string/str   : holds text; will always be surrounded by quotes (' or ") in the code
#        boolean/bool : holds a binary (true-or-false) value
#        list/array   : holds multiple variables, usually of the same type
#        dict/map     : holds named pairs, kind of like nested variables
age = 10
price = 7.85
name = "Gabriel"
likes_tomatoes = False
favorite_games = ["Overwatch", "Minecraft", "Portal"]
mount_everest = {
    "tallest_mountain": True,
    "height_meters": 8848.86,
    "countries": ["Nepal", "China"]
}

# 2. Manipulating variables
#    The value of a variable can be changed by reassigning it
#    What if tax needs to be added to the variable `price`? 
#    Just multiply the taxrate against the original price
price = 1.08 * price
#    Or what if `price` needs to be stored in human-readable form (i.e. as a string)?
price = str(price)

# 3. Using built-in functionality
#    Many functions (reusable pieces of code) are included with Python
#    Programmers also write their own functions and can distribute them as packages
#    Today, we'll use a few packages in 1-2
#    We will only use a few built-in functions today
#        list_variable[index] : gets the variable at that index; in coding, we start counting from zero
#        print([variable])    : outputs (shows) the value of the variable 
print("Price is: " + price)

# 4. Flow control
#    Several keywords allow programmers to direct the flow of a program,
#    either by looping (repeating code) or using conditionals (if this, then that)
#        for     : for each element in a list, do something
#        while   : while a condition is true, do something
#        if/else : if a condition is true, do something; if not, do something else
fruits = ["apple", "orange", "banana", "guava", "persimmon"]
for fruit in fruits:
    print(fruit)
found_fruit = False
fruit_index = 0
while not found_fruit:
    if fruits[fruit_index] == "guava":
        print("Found guava at index: " + str(fruit_index))
        found_fruit = True
    else:
        fruit_index = fruit_index + 1
