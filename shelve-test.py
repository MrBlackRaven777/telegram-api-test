import shelve
import os
import config
import utils


def shelve_create(id):
    name = 'shelve_' + str(id) + '.db'
    try:
        f = open(name, 'x')
        f.close()
        return "Make"
    except FileExistsError:
        return "File already exist"
    except:
        return None


def shelve_remove(id):
    name = 'shelve_' + str(id) + '.db'
    try:
        os.remove(name)
        return "removed"
    except FileNotFoundError:
        return "404"


def shelve_write(id, key, state):
    name = 'shelve_' + str(id) + ".db"
    with shelve.open(name) as storage:
        storage[key] = state


def shelve_read(id, key):
    root_dir = os.getcwd()
    os.chdir("users_storage")
    name = 'shelve_' + str(id) 
    with shelve.open(name, 'r') as storage:
        os.chdir(root_dir)
        try:
            return storage.get(key)
        except:
            return None


print(utils.shelve_read(115934446, 'favorites'))
#print(shelve_read(115934446, 'favorites'))
print(utils.os_choose())
