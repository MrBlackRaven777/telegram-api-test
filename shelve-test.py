import shelve
import os
import config


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
    with shelve.open(name, flag = "r") as storage:
        try:
            return storage[key]
        except:
            return None


# shelve_write(123, True)
# print(shelve_read('is_on'))
#print(shelve_create(123))
#shelve_write(123,"key1","State1")
print(shelve_read(332761,"curr_dir"))
with shelve.open("shelve_332761") as storage:
    print(list(storage.items()))
    storage['favorites'] = config.favorites
    print(list(storage.items()))
#    print(storage.pop('favorites').values())
#    print(list(storage.items()))
#print(shelve_remove(123))
#print(shelve_remove(123))
