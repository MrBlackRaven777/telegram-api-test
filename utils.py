import os
import shelve
#from config import favorites as fav


def create_markup(button_list, sh_id, num=1):

    n_rows = [0, 0, 0]
    blen = len(button_list)
    if blen < 10:
        for i in range(blen):
            n_rows[i % 3] = n_rows[i % 3] + 1
        n = 0
        keyboard = [[0] * n_rows[0], [0] * n_rows[1], [0] * n_rows[2]]
        for l in range(3):
            j = n_rows[l]
            for k in range(0, j):
                keyboard[l][k] = button_list[n]
                n += 1
    else:
        print(">9")

    if shelve_read(sh_id, "is_expl_on") == True:
        keyboard.append(["Back", "Done", "More"])
    else:
        keyboard.append(['Choose folder', 'Cancel'])
    return keyboard

def explorer(id, ch_dir):
    if shelve_read(id, "curr_dir") is None:
        return "No path"
    else:
        full_path = shelve_read(id, "curr_dir") + '/' + ch_dir
        dirs_list = next(os.walk(full_path))[1]
        return dirs_list


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
    exts=['.db', '.dir', '.dat', '.bak']
    # name = 'shelve_' + str(id) + '.db'
    try:
        for i in exts:
            os.remove('shelve_' + str(id) + exts[i])
        return "removed"
    except FileNotFoundError:
        return "404"


def shelve_write(id, key, state):
    name = 'shelve_' + str(id)
    with shelve.open(name) as storage:
        storage[key] = state


def shelve_read(id, key):
    name = 'shelve_' + str(id)
    with shelve.open(name) as storage:
        try:
            return storage[key]
        except:
            return None


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
