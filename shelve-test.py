import shelve
import os
import config
import utils


#def shelve_create(id):
#    name = 'shelve_' + str(id)
#    try:
#        f = open(name, 'x')
#        f.close()
#        return "Make"
#    except FileExistsError:
#        return "File already exist"
#    except:
#        return None
#
#
#def shelve_remove(id):
#    name = 'shelve_' + str(id)
#    try:
#        os.remove(name)
#        return "removed"
#    except FileNotFoundError:
#        return "404"


#def shelve_write(id, key, state):
#    root_dir = os.getcwd()
#    os.chdir("users_storage")
#    name = 'shelve_' + str(id)
#    with shelve.open(name) as storage:
#        storage[key] = state
#        os.chdir(root_dir)
#
#
#def shelve_read(id, key):
#    root_dir = os.getcwd()
#    os.chdir("users_storage")
#    name = 'shelve_' + str(id)
#    with shelve.open(name) as storage:
#        data = storage.get(key)
#        os.chdir(root_dir)
#        return data

#favs=utils.shelve_read(332761, 'favorites')
#print(favs)
#print(favs.get('Download'))
#print(utils.shelve_read(332761, 'favorites').get('Root'))
#full_path = utils.shelve_read(332761, 'curr_dir')
#print(len(next(os.walk(full_path))[1]))
utils.shelve_write(332761, 'is_expl_on', False)
#print(shelve_read(332761, 'is_expl_on'))
#print(shelve_read(332761, 'favorites'))  
#dict_dirs = dict(shelve_read(332761, 'favorites'))
#print(dict_dirs.get('Root'))
#for item in shelve_read(115934446, 'favorites'):
#    print(item)
    
#print(utils.os_choose())
