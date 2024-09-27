from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import repositories.config as config
from time import sleep



driver = webdriver.Edge()
driver.implicitly_wait(10)
driver.set_window_size(1280, 720)
driver.minimize_window()


class sel(object):
    def log():
        """Вход"""

        driver.get(config.URL)
        driver.find_element(By.NAME, "USER_LOGIN").send_keys(config.USERNAME)
        driver.find_element(By.NAME, "USER_PASSWORD").send_keys(config.PASSWORD)
        driver.find_element(By.NAME, "USER_PASSWORD").send_keys(Keys.ENTER)
        sleep(2)
        driver.refresh()

    def new_dir(name_dir):
        """Создание папки"""
        driver.find_element(By.CLASS_NAME, "js-disk-add-button").click()
        sleep(1)
        driver.find_element(
            By.XPATH,
            "//div[@id='popup-window-content-menu-popup-popupMenuAdd']/div/div/span[2]/span[2]",
        ).click()
        sleep(1)
        driver.find_element(By.ID, "disk-new-create-filename").send_keys(name_dir)
        sleep(1)
        driver.find_element(
            By.XPATH, "//div[@id='bx-disk-create-folder']/div[3]/span"
        ).click()
        sleep(1)

    def new_file(way): 
        """Создание файла"""
        WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.CLASS_NAME, "js-disk-add-button"))
        ).click()
        sleep(1)
        file_upload = driver.find_element(By.ID, "inputContainerLabelFolderList")
        sleep(2)
        file_upload.find_element(By.ID, "inputContainerFolderList").send_keys(way)
        WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "bx-disk-popup-upload-file-progress-line-end")
            )
        )
        driver.refresh()
        sleep(2)
        

    def search():
        """Список файлов на экране""" 
        dir = []
        sleep(2)

        folders = driver.find_elements(By.CLASS_NAME, "ui-grid-tile-item")
        for folder in folders:
            dir.append(
                {
                    "name": folder.find_element(By.TAG_NAME, "a").text,
                    "link": folder.find_element(By.TAG_NAME, "a").get_attribute("href"),
                }
            )
        return dir

    def check_name(base, name): 
        """Проверка имени"""
        for i in base:
            if i["name"] == name:
                return True

    def get(url): 
        """Переход по ссылке"""#
        driver.get(url)


"""
       def check_folders():  # просерка пути в битриксе
        driver.refresh()
        sleep(2)
        folders = driver.find_elements(By.ID, "breadcrumbs_oydzs")
        for folder in folders:
            print(folder)
            dir = folder.find_element(By.TAG_NAME, "a").text
            print(dir)
        return dir
   
    def get_name(base):  # получение имени с битрикс
        sel = []
        for i in base:
            sel.append(i["name"])
        return i

"""
