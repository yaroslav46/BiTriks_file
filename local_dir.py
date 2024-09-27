import os
from repositories import config

def GGet_info_dir():
    """Получение данных о папках, файлах из локальной директории"""
    dir_info = []
    id = 0
    for dirname, dirnames, filenames in os.walk(config.DIR_NAME):

        for subdirname in dirnames:
            dir_info.append(
                {
                    "parent": os.path.basename(
                        os.path.dirname(os.path.join(dirname, subdirname))
                    ),
                    "ob_name": subdirname,
                    "ob_tree": os.path.join(dirname),
                    "fuull": os.path.join(dirname, subdirname),
                    "type": "Dir",
                },
            )
            id += 1
        
        for filename in filenames:
            dir_info.append(
                {
                    "parent": os.path.basename(
                        os.path.dirname(os.path.join(dirname, filename))
                    ),
                    "ob_name": filename,
                    "ob_tree": os.path.join(dirname),
                    "fuull": os.path.join(dirname, filename),
                    "type": "File",
                    "way":os.path.abspath(dirname) +'\\'+ filename
                },
            )
            
    print(dir_info)
    return dir_info
