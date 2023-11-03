# first class objects in python

'''A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …'''

'''@gfg_decorator
def hello_decorator():
    print("Gfg")

Above code is equivalent to -

def hello_decorator():
    print("Gfg")
    
hello_decorator = gfg_decorator(hello_decorator)'''

# code for testing decorator chaining
def decor1(func):
    def inner1():
        print('line 23')
        x = func()
        return x * x
    return inner1
 
def decor(func):
    def inner():
        print('line 30')
        x = func()
        return 2 * x
    return inner
 
@decor1
@decor
def num():
    print('line 38')
    return 10
 
print(num())
# what this basically means is num=decor1(decor(num))
# and then later num() is called
# output is 
'''line 23
line 30
line 38
400'''



# Calling method of a class using decorator
import time
import functools


def test_func(funct24):
    def func2(func1):
        print("Inside func2")

        def call(self, *args, **kwargs):
            print("line 9")
            # funct24 = MyClass.funct24
            try:
                func1(self, *args, **kwargs)
            except Exception as e:
                print(e)
                funct24(self)

        return call

    return func2


class MyClass:
    def __init__(self):
        pass

    def func24(self, a=24):
        print("Inside func24")

    @test_func(func24)
    def func12(self):
        print("Inside func12")
        1 / 0


if __name__ == "__main__":
    my_class = MyClass()
    my_class.func12()
