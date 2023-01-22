from functools import wraps
from typing import Callable, Any

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver

import core
from core.utils import exceptions


def _get_chrome_driver() -> webdriver.Chrome:
    """ Configure and return driver object """
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')

    return webdriver.Chrome(options=options)


# mapping from browser name to driver getter function
_BROWSER_2_SETTINGS = {'CHROME': _get_chrome_driver}


def get_driver() -> WebDriver:
    """ Search for driver for browser specified """
    try:
        return _BROWSER_2_SETTINGS[core.BROWSER]()
    except KeyError:
        raise exceptions.NoSuchBrowser(f"Available browsers are: {list(_BROWSER_2_SETTINGS)}")


def handle_driver_error(driver: WebDriver):
    """ Catch webdriver errors and close webdriver if caught """
    def outer_wrapper(function: Callable[..., Any]):
        @wraps(function)
        def inner_wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except WebDriverException as ex:
                driver.close()
                raise exceptions.BrowserFault from ex
        return inner_wrapper
    return outer_wrapper

