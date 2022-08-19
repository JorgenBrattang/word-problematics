def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        # Store the val and returns it so the add function works.
        val = func(*args, **kwargs)
        print("Ended")
        return val

    return wrapper


# Decorator that can change the code above
@f1
def f(a):
    print(a)


# Printing the value of this
f("This is nice")


# Decorator that can change the code above
@f1
def add(x, y):
    return x + y


# Printing the value of this
print(add(4, 5))