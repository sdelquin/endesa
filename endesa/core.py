import datetime
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import settings

from .utils import init_webdriver


class Scraper:
    def __init__(
        self,
        headless=settings.SELENIUM_HEADLESS,
        downloads_dir=settings.DOWNLOADS_DIR,
        webdriver_timeout=settings.WEBDRIVER_TIMEOUT,
        privatearea_url=settings.PRIVATEAREA_URL,
        form_class=settings.LOGIN_FORM_CLASS,
        username_id=settings.LOGIN_USERNAME_ID,
        password_id=settings.LOGIN_PASSWORD_ID,
        username=settings.ENDESA_USERNAME,
        password=settings.ENDESA_PASSWORD,
        consumption_link1_xpath=settings.CONSUMPTION_LINK1_XPATH,
        consumption_link2_xpath=settings.CONSUMPTION_LINK2_XPATH,
        consumption_download_button_xpath=settings.CONSUMPTION_DOWNLOAD_BUTTON_XPATH,
        published_date_xpath=settings.PUBLISHED_DATE_XPATH,
        published_consumption_xpath=settings.PUBLISHED_CONSUMPTION_XPATH,
    ):
        self.webdriver_timeout = webdriver_timeout
        self.driver = init_webdriver(headless=headless, downloads_dir=downloads_dir)
        self.login(
            privatearea_url, form_class, username_id, password_id, username, password
        )
        self.navigate_to_consumption_panel(consumption_link1_xpath, consumption_link2_xpath)
        self.download_consumption(consumption_download_button_xpath)
        self.get_published_date(published_date_xpath)
        self.get_published_consumption(published_consumption_xpath)

    def login(
        self, privatearea_url, form_class, username_id, password_id, username, password
    ):
        self.driver.get(privatearea_url)

        form = WebDriverWait(self.driver, timeout=self.webdriver_timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, form_class))
        )

        username_input = form.find_element('id', username_id)
        password_input = form.find_element('id', password_id)
        button = form.find_element('tag name', 'button')

        username_input.send_keys(username)
        password_input.send_keys(password)
        button.click()

    def navigate_to_consumption_panel(self, link1_xpath, link2_xpath):
        element = WebDriverWait(self.driver, timeout=self.webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, link1_xpath))
        )
        element.click()

        element = WebDriverWait(self.driver, timeout=self.webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, link2_xpath))
        )
        element.click()

    def download_hourly_consumption(self, button_xpath):
        download_button = WebDriverWait(self.driver, timeout=self.webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, button_xpath))
        )
        download_button.click()

    def get_published_date(self, date_xpath):
        date = WebDriverWait(self.driver, timeout=self.webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, date_xpath))
        )
        self.published_date = datetime.datetime.strptime(
            date.text.strip(), '%d-%m-%Y'
        ).date()

    def get_published_consumption(self, consumption_xpath):
        consumption = WebDriverWait(self.driver, timeout=self.webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, consumption_xpath))
        )
        self.published_consumption = float(
            re.search(r'[\d,]+', consumption.text.strip()).group().replace(',', '.')
        )
