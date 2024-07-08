def myFun(arg1, *argv):
    print("First arguement :", arg1)
    for arg in argv:
        print("Next argument comes through *argv:", arg)

myFun("Hello", 'I am', 'a', 'software','engineer')
