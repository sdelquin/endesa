from pathlib import Path

from prettyconf import config

PROJECT_DIR = Path('.').resolve()
PROJECT_NAME = PROJECT_DIR.name

SELENIUM_HEADLESS = config('SELENIUM_HEADLESS', default=True, cast=lambda v: bool(int(v)))
PRIVATEAREA_URL = config(
    'PRIVATEAREA_URL', default='https://zonaprivada.edistribucion.com/areaprivada/'
)
WEBDRIVER_TIMEOUT = config('WEBDRIVER_TIMEOUT', default=10, cast=int)  # seconds
DOWNLOADS_DIR = config('DOWNLOADS_DIR', default=PROJECT_DIR / 'downloads', cast=Path)

# Login
LOGIN_FORM_CLASS = config('LOGIN_FORM_CLASS', default='main-tablet')
LOGIN_USERNAME_ID = config('LOGIN_USERNAME_ID', default='input-5')
LOGIN_PASSWORD_ID = config('LOGIN_PASSWORD_ID', default='input-6')
ENDESA_USERNAME = config('ENDESA_USERNAME')
ENDESA_PASSWORD = config('ENDESA_PASSWORD')

# Consumption
CONSUMPTION_LINK1_XPATH = config(
    'CONSUMPTION_LINK1_PATH',
    default='/html/body/div[3]/div[3]/div/div[2]/div[1]/div/div/span/ul/li[3]/span/button',
)
CONSUMPTION_LINK2_XPATH = config(
    'CONSUMPTION_LINK2_PATH',
    default=(
        '/html/body/div[3]/div[3]/div/div[2]/div/div/div/div/article/section[2]/div/'
        'div[1]/lightning-datatable/div[2]/div/div/table/tbody/tr/td[4]/'
        'lightning-primitive-cell-factory/span/div/lightning-primitive-cell-button/'
        'lightning-button/button'
    ),
)
CONSUMPTION_DOWNLOAD_BUTTON_XPATH = config(
    'CONSUMPTION_DOWNLOAD_BUTTON_XPATH',
    default=(
        '/html/body/div[3]/div[3]/div/div[2]/div/div/div/div/article/section[3]/'
        'section/div/div/button'
    ),
)

# Current measurements
CURRENT_DATE_XPATH = config(
    'CURRENT_DATE_XPATH',
    default=(
        '/html/body/div[3]/div[3]/div/div[2]/div/div/div/div/article/'
        'section[2]/div/h4/span'
    ),
)
CURRENT_CONSUMPTION_XPATH = config(
    'CURRENT_CONSUMPTION_XPATH',
    default=(
        '/html/body/div[3]/div[3]/div/div[2]/div/div/div/div/article/'
        'section[2]/div/div/span[2]/span'
    ),
)
