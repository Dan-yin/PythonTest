# use str.format()

print('I love {}'.format('python'))

#File io
# f = open()
# f.readline() return '' ,this is the file end, if return '\n' this
# f.tell()  f.seek(offset,from_what)  
# with open() as f: this file will be closed after this language



#JSON(javaScript Object Notation) store structured data

import json

json.dumps([1,'simple','list'])
x = [1,'simplel','list']
f = open("test.json",'w')
json.dump(x,f)
f.close()
f = open("test.json")
y = json.load(f)
print(y)