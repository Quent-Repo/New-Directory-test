import time
import os
import datetime
x = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
print(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
#os.mkdir(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
if(os.path.exists("tset") != True):
    os.mkdir("tset")
else:
    print(" ")
Main_Locatoion = os.path.join("tset",x)
os.mkdir(os.path.join("tset",x))
#f = open("test.txt", "w")
location = os.getcwd()
print(location)
os.chdir(os.path.join("tset",x))
f = open("test.txt" , "w")
f.write(x)
print(os.getcwd())
f.close()
os.chdir(location)
print(os.getcwd())
