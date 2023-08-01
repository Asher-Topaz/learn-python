#function is defined
def print_lyrics():
    print("I'm a lumberjack, and I'm strong")
    print("I work hard all day and sleep all night")
#function def creates variables of the same name
#value of the variable is a function object with type function
print(print_lyrics) 
print(type(print_lyrics))

#function called inside another function
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()






