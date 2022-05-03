import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


def init_webdriver(headless=True, downloads_dir=os.getcwd()):
    options = Options()
    options.headless = headless
    options.set_preference('browser.download.folderList', 2)
    options.set_preference('browser.download.dir', str(downloads_dir))
    service = Service(log_path=os.devnull)
    return webdriver.Firefox(options=options, service=service)
