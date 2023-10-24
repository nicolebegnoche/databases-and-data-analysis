import os
import json
import requests


def quit_msg(msg=None):
    if msg: print(f'Quit msg: {msg}')
    quit()


# def path_exists(path, doesnt_exist=None, msg=None):
#     if os.path.exists(path): return True
#     match doesnt_exist:
#         case 'create': create_path(path)
#         case 'quit': quit_msg(msg)            
#         case _: return False

# def create_path(path):
#     # quit if empty
#     if not path: quit_msg(f'Can\'t create empty path {path}')

#     # split filename from directories
#     folders = path.split('/')
#     file = folders[-1] if '.' in folders[-1] else None
#     folders = '/'.join(folders[:-1]) if file else '/'.join(folders)

#     # create directories and/or file
#     if folders and not os.path.exists(folders): os.makedirs(folders)
#     if file and not os.path.exists(path): open(path, 'w')


# ''' JSON Methods '''
# def json_read_from_file(filepath):
#     path_exists(filepath, f"{filepath} doesn't exist.")
#     try:
#         with open(filepath) as file:
#             return json.load(file)
#     except Exception as error:
#         quit_msg("Failed to read from file.", error)

# def json_write_to_file(data, filepath, indent=1):
#     try:
#         with open(filepath, 'w+') as file:
#             json.dump(data, file, indent=indent)
#             file.close()
#     except Exception as error:
#         quit_msg("Failed to write to file", error)

# ''' HTTP '''
# def get_request(URL=None, HEADERS=None):
#     # True if status code is between 200 and 400
#     if not (r := requests.get(URL, headers=HEADERS)):
#         msg =  f'Error accessing {r.url}\n'
#         msg += f'{r.status_code}: {r.reason}'
#         quit_msg(msg)
#     else:
#         return r.json()

