from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pycabara.Element import Element

__author__ = 'ruthlesshelp'


class Selenium(object):
    __browser = None

    def __init__(self, browser_name=':chrome'):
        self.browser_name = browser_name
        self.driver_wait = 5

    def get_browser(self):
        if self.__browser is None:
            self.__init_browser()
        return self.__browser

    def find(self, locator):
        if self.__find_element_by_id(locator):
            return Element(self)
        else:
            return None

    def set(self, text):
        if self.current_element is not None:
            # Sends keys to an element by id.
            self.current_element.send_keys(text)
            return self.current_element
        else:
            return None

    def has_title(self, text):
        title = self.get_browser().get_title()
        if title == text:
            return True
        else:
            return False

    def has_text(self, text):
        body_text = self.get_browser().get_body_text()
        if text in body_text:
            return True
        else:
            return False

    def __init_browser(self):
        if self.browser_name == ':chrome':
            self.__browser = webdriver.Chrome()

    # Finder methods
    def __find_element_by_id(self, element_id):
        message = u'Element id=%s was not found after %d seconds' % (element_id, self.driver_wait)
        element = WebDriverWait(self.get_browser(), self.driver_wait)\
            .until(lambda y: y.find_element_by_id(element_id), message)
        if element is None:
            self.current_element = None
            return False
        else:
            self.current_element = element
            return True

