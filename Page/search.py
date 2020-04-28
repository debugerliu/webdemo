from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Base.base import BaseAction


class SearchPage(BaseAction):

    # 搜索框的定位
    input_element = By.CSS_SELECTOR, '[id="kw"]'
    # 提交按钮的定位
    submit_element = By.CSS_SELECTOR, '[id="su"]'
    # 需要搜索的内容
    content = 'selenium'
    # 链接
    url = 'http://www.baidu.com'

    def get_new(self):
        self.get_new_link(self.url)

    def send_search_text(self):
        self.send_text(self.input_element, text=self.content)

    def click_submit_element(self):
        self.click_button(self.submit_element)

    def close(self):
        self.driver.close()


# 测试方法
if __name__ == '__main__':
    driver = webdriver.Chrome()
    c = SearchPage(driver)
    try:
        c.get_new()
        c.send_search_text()
        c.click_submit_element()
        sleep(3)
        c.close()
    except Exception as e:
        c.close()
