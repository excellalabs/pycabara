from pycabara.Selenium import Selenium

__author__ = 'ruthlesshelp'


class Session(object):
    def __init__(self, mode):
        if mode is None:
            raise AssertionError('Mode is invalid or was not provided.')

        self.current_url = None

        if mode == ':selenium':
            self.driver = Selenium()
        else:
            self.driver = None

    def visit(self, path):
        self.driver.visit(path)
        self.current_url = self.driver.current_url

    def fill_in(self, locator, text=''):
        element = self.driver.find(locator)
        element.set(text)
        return element

    def click_button(self, locator):
        self.driver.click_button(locator)

    def should_have_content(self, content):
        has_content = False
        if self.driver.has_title(content):
            has_content = True
        if self.driver.has_text(content):
            has_content = True
        return has_content
