import time

import core
import core.utils.drivers as drivers


_DRIVER = drivers.get_driver()


@drivers.handle_driver_error(driver=_DRIVER)
def get_text_like_file(path: str):
    _DRIVER.get(url=core.URL + path)
    return _DRIVER.find_element_by_xpath('//pre').text


@drivers.handle_driver_error(driver=_DRIVER)
def get_image(path: str):
    _DRIVER.get(url=core.URL + path)
    return _DRIVER.find_element_by_xpath('//img').screenshot_as_png


@drivers.handle_driver_error(driver=_DRIVER)
def get_svg(path: str):
    _DRIVER.get(url=core.URL + path)
    return _DRIVER.find_element_by_xpath("//*[local-name() = 'svg']").screenshot_as_png


@drivers.handle_driver_error(driver=_DRIVER)
def get_page_content(path: str):
    """ Get selenium driver and make a request to specified url and get content """
    _DRIVER.get(url=core.URL + path)
    # wait for react ddos protection stuff end
    time.sleep(5)
    return _DRIVER.page_source
