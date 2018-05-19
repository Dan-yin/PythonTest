import os

for i in range(0,10,2):
    print(i)

a = 'this is python'
m = u = a

print(id(a),id(m),id(u))

if m == a :
    print(u)
elif m == u:
    print(a)
else :
    print(m)
'''
num = int(input())
print(num)
'''
'''
def ask_ok(prompt,retries = 4, complaint = 'Yes or No,please'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries = retries -1
        if retries < 0:
            raise OSError('uncooperative usr')
        print(complaint)

ask_ok('yy')
'''

def get(a,l=[]):
    l.append(a)
    return l

print(get(1))
print(get(2))
print(get(3))

def cheeseshop(kind,*arguments,**keywords):
    print("-- Do you have any ", kind)
    print("-- I'm sorry, we're all  out of ", kind)
    for arg in arguments:
        print(arg)
    keys = sorted(keywords.keys())
    for ke in keys:
        print(ke,":",keywords[ke])

cheeseshop('liam',"it's very hot",'not at all', usa = 'american',cn = 'china',jp = 'jpanse')

args = [3,6]
print(list(range(*args)))
#print(list(range(args)))
#TypeError: 'list' object cannot be interpreted as an integer
# this also can be used for dict by **args

#lambad x : x+1
ms = list(range(0,20,2))
for i, u in enumerate(ms):
    print(i,u)

lis = list('qwertyuiop')
for i,u in zip(ms,lis):
    print(i,u)

for i in reversed(range(10)):
    print(i)

for i in sorted(range(20,0,-2)):
    print(i)

test = range(20,0,-2)

for i in test[:]:
    print(i)    

'''
in/not in 
is/is not
and/or
not
a < b ==c  means b > a and b == c
'''