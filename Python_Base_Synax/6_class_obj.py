#python3 namespace
'''
local namespace
global namespace
build-in namespace
'''

def func(a=1):
    b = 2
    print(locals())
    return a + b

func()
#locals returns local funcs , the returned value is dict
print(globals())
#globals return local moudles, the returned value is dict
#form a import b, import b ,use diff namesapce

'''
moudle :
__name__
__file__
__dict__
__doc__
__package__
__path__
'''

class MyClass(object):
    '''A simple example class'''
    i = 12345
    def f(self):
        return 'hello world'
    @classmethod
    def e(clss):
        return 'this is class method'
    @staticmethod
    def h(a,b):
        return a+b


print(MyClass.i)
print(MyClass.e())
print(MyClass.h(3,5))
u = MyClass()
print(u.f())
print(u.h(1,2))

class Revers:
    '''Iterator for looping over a sequence backwards.'''
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]


rev = Revers('spam')
#iter(rev)

for char in rev:
    print(char)

#generator range,zip,set,max    