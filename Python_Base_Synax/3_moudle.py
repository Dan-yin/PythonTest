import fibo

# from fibo import *

print(fibo.fib(1000))
print(fibo.fib2(100))
print(fibo.__name__)

#Python use .pyc file to improve module running speed
#A.B
#__init__.py file can be used when sys.path search file
print(dir(fibo))

# when use from package import *, if __init__.py has __all__ list action, these list file will be import