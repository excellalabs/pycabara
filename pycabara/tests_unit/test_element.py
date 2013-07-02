import unittest
from hamcrest import *
from pycabara.Element import Element

__author__ = 'ruthlesshelp'


class ElementTest(unittest.TestCase):
    def test_set_WhenValidTextIsSet_ThenDriverSetsProperText(self):
        # arrange
        stub_driver = FakeDriver()

        element = Element(stub_driver)

        # act
        element.set('valid text')

        # assert
        assert_that(stub_driver.stub_set, is_('valid text'))


class FakeDriver(object):

    def __init__(self):
        self.current_url = None

        # setup behavior
        self.stub_has_title = False
        self.stub_has_text = False
        self.stub_set = ''

    def visit(self, path):
        self.current_url = path

    def find(self, locator):
        element = Element(self)
        element.id = locator
        return element

    def set(self, text):
        self.stub_set = text

    def has_title(self, text):
        return self.stub_has_title

    def has_text(self, text):
        return self.stub_has_text
