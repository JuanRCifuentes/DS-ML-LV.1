def func1(un_arg, una_func):
    def func2(other_arg):
        return other_arg * 2
    
    value = func2(un_arg)
    return una_func(value)

un_arg = 1

def any_func(any_arg):
    return any_arg + 5

print(func1(un_arg, any_func))