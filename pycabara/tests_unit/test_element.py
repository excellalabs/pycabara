import unittest
from hamcrest import *
from pycabara.Element import Element
from pycabara.tests_unit.fakes.FakeDriver import FakeDriver

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