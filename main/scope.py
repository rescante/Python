# global scope
x = 'global x'

def my_func():
    # local scope
    x = 'local x'
    print(x)

my_func()
print(x)

######################

# global
name = 'Mehmet'

def changeName(new_name):
    global name
    name = new_name
    print(name)

changeName('Alper')
print(name)

######################

name = 'global string'

def greeting():
    # name = 'Mehmet'

    def hello():
        # name = 'Alper'
        print('hello ' + name)

    hello()

greeting()

######################

x = 50

def test():
    global x
    print(f'x : {x}')

    x = 100
    print(f'changed x to {x}')

test()
print(x)