from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

from pycabara.Element import Element

__author__ = 'ruthlesshelp'


class Selenium(object):
    __browser = None

    def __init__(self, browser_name=':chrome'):
        if browser_name is None:
            raise AssertionError('Browser name is invalid or was not provided.')

        self.browser_name = browser_name
        self.driver_wait = 5
        self.current_url = None

    def get_browser(self):
        if self.__browser is None:
            self.__init_browser()
        return self.__browser

    def visit(self, path):
        self.get_browser().get(path)
        self.__wait_for_load()
        self.current_url = self.get_browser().current_url

    def find(self, locator):
        if self.__find_element_by_name(locator):
            return Element(self)
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
        title = self.get_browser().title

        return text in title

    def has_text(self, text):
        try:
            # look in the body of the page
            element = self.get_browser().find_element_by_tag_name("body")

            if element is None:
                return False
        except NoSuchElementException:
            return False

        body_text = element.text

        return text in body_text

    def click_button(self):
        if self.current_element is not None:
            self.current_element.submit()
        else:
            raise AssertionError('Current element is invalid or not set.')

    def click_button(self, locator):
        if self.__find_element_by_id(locator):
            self.current_element.submit()
            return Element(self)
        if self.__find_element_by_name(locator):
            self.current_element.submit()
            return Element(self)
        else:
            return None

    def quit(self):
        self.get_browser().quit()

    # private helper methods
    def __init_browser(self):
        if self.browser_name == ':chrome':
            self.__browser = webdriver.Chrome('/usr/bin/chromedriver')

    def __wait_for_load(self):
        pass

    # private finder methods
    def __find_element_by_id(self, element_id):
        message = u'Element id=%s was not found after %d seconds' % (element_id, self.driver_wait)
        element = WebDriverWait(self.get_browser(), self.driver_wait) \
            .until(lambda y: y.find_element_by_id(element_id), message)
        if element is None:
            self.current_element = None
            return False
        else:
            self.current_element = element
            return True

    def __find_element_by_name(self, name):
        # search_box = driver.find_element_by_name('q')
        message = u'Element id=%s was not found after %d seconds' % (name, self.driver_wait)
        element = WebDriverWait(self.get_browser(), self.driver_wait) \
            .until(lambda y: y.find_element_by_name(name), message)
        if element is None:
            self.current_element = None
            return False
        else:
            self.current_element = element
            return True

    # testing use only
    # def set_fake_browser(self, fake_browser):
    #     self.__browser = fake_browser
