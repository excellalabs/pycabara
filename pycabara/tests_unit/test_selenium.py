import unittest
from hamcrest import *
from pycabara.Selenium import Selenium

__author__ = 'ruthlesshelp'


class SeleniumTest(unittest.TestCase):
    def test_init_GivenBrowserNameIsNone_ThenExpectAssertionError(self):
        # arrange
        exception_thrown = False

        # act
        actual = ''
        try:
            Selenium(None)
        except AssertionError, actual:
            exception_thrown = True

        # assert
        if not exception_thrown:
            self.fail('Expected exception was not thrown')

        assert_that(actual, instance_of(AssertionError))

    def test_init_GivenBrowserNameIsFake_ThenExpectBrowserIsNone(self):
        # arrange
        # act
        selenium = Selenium(':fake')

        # assert
        assert_that(selenium.get_browser(), is_(None))

    def test_visit_GivenUrlIsPassed_ThenCurrentUrlShouldBeValuePassed(self):
        # arrange
        selenium = Selenium(':fake')
        selenium.set_fake_browser(FakeBrowser())

        # act
        selenium.visit(r'http://example.com')

        # assert
        assert_that(selenium.current_url, is_(r'http://example.com'))


class FakeBrowser(object):
    def __init__(self):
        self.title = None
        self.current_url = None

    def get(self, path):
        self.current_url = path

    def quit(self):
        pass

    def find_element_by_tag_name(self, param):
        pass
