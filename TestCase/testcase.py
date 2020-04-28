from time import sleep

from selenium import webdriver

from Page.search import SearchPage


class TestCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()

    def test_search(self):
        c = SearchPage(self.driver)
        try:
            c.get_new()
            c.send_search_text()
            c.click_submit_element()
            sleep(3)
            c.close()
        except Exception as e:
            print(e)
            c.close()


def test_main():
    c = TestCase()
    c.test_search()
    assert 1 == 2
