__author__ = 'ruthlesshelp'


class Element(object):
    def __init__(self, driver):
        self.driver = driver

    def set(self, text):
        self.driver.set(text)