
from unicodedata import name
from edupage_api import Edupage
import json
import os
import datetime
from zipfile import ZipFile
import pandas as pd
import random
from random import seed
from os import listdir
from os.path import isfile, join
from os.path import exists
edupage = Edupage()
seed = random.randint(0,2365489645)
 
file_exists = exists(r"userinfo.json")
file_exists1 = exists(r"fileinfo.json")
if(file_exists==True):
    with open('userinfo.json', 'r') as openfile:
        json_object = json.load(openfile)
        readusername =str(json_object["username"])
        readpassw =str(json_object["passw"])
        readsubd = str(json_object["subd"])
        
        edupage.login(str(json_object["username"]), str(json_object["passw"]), str(json_object["subd"]))
else:
    username = input("Username: ")
    passw = input("password: ")
    subd = input("subdomain: ")
    dictionary = {
    "username": username,
    "pass": passw,
    "subdomain": subd
}
    with open("userinfo.json", "w") as outfile:
        json.dump(dictionary, outfile)

        edupage.login(username, passw, subd)
direxists=os.path.isdir('cloud')
if(direxists==True):
    pass
else:
    os.mkdir("cloud")


while(True):
    command = str(input("Command: "))
    if(command == "upload"):
        path1 = input("Insert path of file filename included and no qoutes: ")
        filename = str(os.path.basename(path1))
        if(file_exists1==False):
            create = open("fileinfo.json","x")
            print("Please go into your user folder and insert in file fileinfo.json")
            print("text from this link https://textbin.net/xqboppoq56")
        namezip = str(random.randint(0,851525784541))+".zip"
        with ZipFile(namezip, "w") as newzip:
            newzip.write(path1)
        with open(namezip, "rb") as fp:
            uploaded  =edupage.cloud_upload(fp)
            print(uploaded)
            link="https://"+readsubd+".edupage.org"+str(uploaded.file)
            print(link)

        with open("fileinfo.json", "r") as fp:
            dictObj = json.load(fp)
            print(dictObj)
            dictObj.update({filename: link})
            print(dictObj)
        with open("fileinfo.json", "w") as fp:
            json.dump(dictObj, fp)
    elif(command == "getlink"):
        with open('fileinfo.json', 'r') as openfile1:
            json_object1 = json.load(openfile1)
            nameoffile= json_object1[input("Enter name of file: ")]
            print(nameoffile)
    elif(command == "help"):
        print("blablabla")
    else:
        print("invalid command")
