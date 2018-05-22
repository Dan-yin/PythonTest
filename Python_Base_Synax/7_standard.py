import os 

print(os.getcwd())
#os.system('mkdir today') this is linux comman
import shutil
#shutil.copyfile  shutil.move
import glob
print(glob.glob('*.py'))
import sys
#sys.exit()
os.chdir(os.getcwd() + '\\Python_Base_Synax')
print(glob.glob('*.py'))

#sys.exit()

import re
import math
import random

from datetime import date
now  = date.today()
print(now.strftime('%m-%d-%y. %d %b %Y'))

#data zip
#zlib,gzip,bz2,lzma,zipfile,tarfile

'''
xmlrpc.client       xmlrpc.server
email
smtplib     poplib
xml.dom     xml.sax

'''

#struct  for rb

import threading
#multithreading