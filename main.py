from repositories.Selenium import sel
import local_dir
from time import sleep



sel.log()
loc_dir_info = local_dir.GGet_info_dir()
search_info = sel.search()

for i in local_dir.GGet_info_dir():
    a =i['ob_tree']
    a = a.replace(" ","%20")
    a ='https://team.alabuga.ru/company/personal/user/9333/disk/path/Отчётная%20документация%20ЛКДС/'+a
    sel.get(a)
    sleep(1)
    
    if not sel.check_name(sel.search(),i["ob_name"]): 
        if i["type"] == "Dir":
            sel.new_dir(i["ob_name"])
        else:
           sel.new_file(i['way'])
    


