URL = 'https://team.alabuga.ru/company/personal/user/9333/disk/path/Отчётная%20документация%20ЛКДС/Логистический%20комплекс%20им.%20Дэн%20Сяопина%20железнодорожная%20инфраструктура/'

file = open("conf.txt", "r")
content = file.readlines()
file.close()
USERNAME = content[0]
PASSWORD = content[1]
DIR_NAME = content[2]