import shelve
import os
from config import shelve_name


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


# shelve_write(123, True)
# print(shelve_read('is_on'))
print(shelve_create(123))
print(shelve_remove(123))
print(shelve_remove(123))
