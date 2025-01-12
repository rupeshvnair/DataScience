def deco_func(mod_func):
    def func_1(*args):
        print('Decorator Function started')
        val = mod_func(*args)
        print('Decorator Function ended')
        return val
    return func_1

@deco_func
def add_func(x,y):
    return x+y

value = add_func(1,2)
print(value)