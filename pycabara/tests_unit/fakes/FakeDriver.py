from pycabara.Element import Element

__author__ = 'ruthlesshelp'


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
