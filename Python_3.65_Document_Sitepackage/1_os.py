import os
import time

print(os.path)
print(os.getcwd())
print(os.path.dirname(os.getcwd()))
if os.path.exists(os.getcwd() + r'\summary'):
    print('pass')
elif os.path.exists(r'{0}\1_os.py'.format(os.getcwd())):
    print('false')

print(os.path.lexists(os.getcwd()+r'\su'))
#print(type(os.path.getmtime(r'{0}\1_os.py'.format(os.getcwd()))))
localtime = time.localtime(os.path.getmtime(r'{0}\1_os.py'.format(os.getcwd())))
#localtime = time.localtime(os.path.gettime(os.getcwd()))
localcreatetime = time.localtime(os.path.getctime(r'{0}\1_os.py'.format(os.getcwd())))
print('{0}\n{1}'.format(time.strftime('%Y%m%d%H%M%S',localcreatetime),\
time.strftime('%Y%m%d%H%M%S',localtime)))
path = r'{0}\1_os.py'.format(os.getcwd())
print('size:{0}\nisabs:{1}\nisdir:{2}\nisfile:{3}\nisline:{4}'.format(os.path.getsize(path),os.\
path.isabs(path),os.path.isdir(path),os.path.isfile(path),os.path.islink(path)))
