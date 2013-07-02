import unittest
from hamcrest import *

from pycabara.Session import Session
from pycabara.Selenium import Selenium
from pycabara.tests_unit.fakes.FakeDriver import FakeDriver

__author__ = 'ruthlesshelp'


class SessionTest(unittest.TestCase):
    def test_init_GivenModeIsNone_ThenExpectAssertionError(self):
        # arrange
        exception_thrown = False

        # act
        actual = ''
        try:
            Session(None)
        except AssertionError, actual:
            exception_thrown = True

        # assert
        if not exception_thrown:
            self.fail('Expected exception was not thrown')

        assert_that(actual, instance_of(AssertionError))

    def test_init_GivenModeIsSelenium_ThenExpectDriverIsSelenium(self):
        # arrange
        # act
        session = Session(':selenium')

        # assert

        assert_that(session.driver, instance_of(Selenium))


    def test_init_GivenModeIsFake_ThenExpectDriverIsNone(self):
        # arrange
        # act
        session = Session(':fake')

        # assert
        assert_that(session.driver, is_(None))

    def test_visit_GivenUrlIsPassed_ThenCurrentUrlShouldBeValuePassed(self):
        # arrange
        session = Session(':fake')
        session.driver = FakeDriver()

        # act
        session.visit(r'http://example.com')

        # assert
        assert_that(session.current_url, is_(r'http://example.com'))

    def test_fill_in_GivenAnElementWithIdOnPage_ThenFindsTheElement(self):
        # arrange
        session = Session(':fake')
        session.driver = FakeDriver()

        # act
        element = session.fill_in('q', 'any text')

        # assert
        assert_that(element.id, is_('q'))

    def test_should_have_content_GivenTextVisibleOnPage_ThenHasContentTrue(self):
        # arrange
        stubDriver = FakeDriver()
        stubDriver.stub_has_text = True

        session = Session(':fake')
        session.driver = stubDriver

        # act
        actual = session.should_have_content('text visible on page')

        # assert
        assert_that(actual, is_(True))

    def test_should_have_content_GivenTextInPageTitle_ThenHasContentTrue(self):
        # arrange
        stubDriver = FakeDriver()
        stubDriver.stub_has_title = True

        session = Session(':fake')
        session.driver = stubDriver

        # act
        actual = session.should_have_content('text in page title')

        # assert
        assert_that(actual, is_(True))

    def test_should_have_content_GivenNoTextOnPageOrInTitle_TheExpectFalse(self):
        # arrange
        stubDriver = FakeDriver()

        session = Session(':fake')
        session.driver = stubDriver

        # act
        actual = session.should_have_content('text in page title')

        # assert
        assert_that(actual, is_(False))
