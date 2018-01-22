import os
import shelve
import sys
#from config import favorites as fav


def create_markup(button_list, sh_id, num=1):

    n_rows = [0, 0, 0]
    blen = len(button_list)
    if blen < 10:
        for i in range(0,blen-1):
            n_rows[i % 3] = n_rows[i % 3] + 1
        n = 0
        keyboard = [[0] * n_rows[0], [0] * n_rows[1], [0] * n_rows[2]]
        for l in range(3):
            j = n_rows[l]
            for k in range(0, j):
                keyboard[l][k] = button_list[n]
                n += 1
    else:
        start = (num-1)*9
        stop = blen if blen <= num*9 else num*9
        for i in range(start//9+1-num, stop%9-1):
            n_rows[i % 3] = n_rows[i % 3] + 1
        n = start
        keyboard = [[0] * n_rows[0], [0] * n_rows[1], [0] * n_rows[2]]
        for l in range(3):
            j = n_rows[l]
            for k in range(0, j):
                keyboard[l][k] = button_list[n]
                n += 1

    if shelve_read(sh_id, "is_expl_on") == True:
        keyboard.append(["Back", "Done", "More"])
    else:
        keyboard.append(['Choose folder', 'Cancel'])
    return keyboard

def explorer(id, ch_dir):
    if shelve_read(id, "curr_dir") is None:
        return "No path"
    else:
        full_path = shelve_read(id, "curr_dir") + '\\' + ch_dir
        print(full_path)
        try:
            dirs_list = next(os.walk(full_path))[1]
            print(dirs_list)
            return dirs_list
        except:
            return None


# def explorer(path="/storage/emulated/0/qpython"):
#     os.chdir(path)
#     path_list = next(os.walk('.'))[1]
#     print(path_list)
#     newPth = input()
#     if newPth in path_list:
#         print("exist")
#         return explorer(path + "/" + newPth)
#     elif newPth == "back":
#         print("backdir")
#         n = path.rfind("/")
#         return explorer(path[:n])
#     elif newPth == "done":
#         print(path_list)
#         return path_list
#     else:
#         print("no path, try again")
#         return explorer(path)


def shelve_create(id):
    name = 'shelve_' + str(id) + '.db'
    try:
        f = open(name, 'x')
        f['is_expl_on'] = False
        f.close()
        return "Make"
    except FileExistsError:
        return "File already exist"
    except:
        return None


def shelve_remove(id):
    root_dir = os.getcwd()
    os.chdir("users_storage")
#    exts=['.db', '.dir', '.dat', '.bak']
    # name = 'shelve_' + str(id) + '.db'
    try:
        for d, dirs, files in os.walk(os.getcwd()):
            for f in files:   
                if str(id) in f:
                        os.remove(f)
        os.chdir(root_dir)
        return "Removed successfully"
    except FileNotFoundError:
        return "404"
    except:
        return sys.exc_info()
    


def shelve_write(id, key, state):
    root_dir = os.getcwd()
    os.chdir("users_storage")
    name = 'shelve_' + str(id)
    with shelve.open(name) as storage:
        storage[key] = state
        os.chdir(root_dir)


def shelve_read(id, key):
    root_dir = os.getcwd()
    os.chdir("users_storage")
    name = 'shelve_' + str(id)
    with shelve.open(name, 'r') as storage:
        try:
            data = storage.get(key)
        except:
            data = sys.exc_info()
        os.chdir(root_dir)
        return data
        
    

def config_setup(id):
    name = 'shelve_' + str(id)
    with shelve.open(name) as storage:
        try:
            return storage.keys()
        except:
            return None
        
def os_choose():  
    if os.name == "nt":
        return {"curr_dir": os.path.expanduser("~"), "Root": "C:/", "Download": os.path.expanduser("~\\Downloads"), "Video": os.path.expanduser("~\\Videos"), "Default folder": os.getcwd()}
    elif os.name == "posix":
        return {"curr_dir": os.path.expanduser("~"), "Root": "/", "Download": os.path.expanduser("~/Download"), "Movies": os.path.expanduser("~/Movies"), "Default folder": os.getcwd()}
    else:
        return {"curr_dir": "/"}
    

    
        
#def get_favs(id):
#    name = 'shelve_' + str(id)
#    with shelve.open(name) as storage:
#        try:
#            return storage['favorites']
#        except:
#            return None
#testlist =[i**3 for i in range(7)]
# testos = explorer("E:/Eclipse/tabel-tele-bot/") #os.listdir("/storage/emulated/0/qpython/scripts")
# print(create_markup(list(fav.keys())))
