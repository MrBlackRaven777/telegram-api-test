import os
token = "345248007:AAF4R8mKESAnqBn_jXOReMLbatqMzz8TMwc"
#favorites = {"Root": "/", "Download": "/storage/emulated/0/Download",
             #"Eclipse": "E:/Eclipse", "Default folder": "E:/"}
is_expl_on = False
full_path = "E:/"
shelve_name = 'shelve.db'
if os.name == "nt":
    start_path = "C:/"
    favorites = ("Root": "C:/", "Download": "C:\\Users\d.voskresenskiy\Downloads", "Video": "C:\\Users\d.voskresenskiy\Videos", "Default folder": os.getcwd())
elif os.name == "posix":
    start_path = "/home/"
    favorites = ("Root": "/", "Download": "/storage/emulated/0/Download", "Eclipse": "E:/Eclipse", "Default folder": os.getcwd())
else:
    start_path = "/"