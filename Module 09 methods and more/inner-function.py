def do_something():
    print("Inside the function do_something")
    def inner_function():
        print('Insider the Inner function')
    
    return inner_function()

# do_something()

def first_function():
    print('inside the first function')
    def second_function():
        print('inside the inner function')
    return second_function

# my_function = first_function()

# print(my_function)
first_function()()