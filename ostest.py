import os
import shelve
#from config import favorites as fav
import config

def shelve_test(chat_id):
    sh = shelve.open(chat_id, flag='n')
    #sh[is_on] = True
    print(sh)


def explorer(path):
    os.chdir(path)
    path_list = os.listdir(path)
    print(path_list)
    newPth = input()
    if newPth in path_list:
        print("exist")
        explorer(path + "/" + newPth)
    elif newPth == "back":
        print("backdir")
        n = path.rfind("/")
        explorer(path[:n])

    else:
        # print("no path, try again")
        explorer(path)

print(os.getcwd())
# explorer("E:/#")\
#shelve_test(111)
