from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseAction(object):

    # 初始化方法，接受外部传入的driver浏览器的参数
    def __init__(self, driver):
        self.driver = driver

    # 封装定位方法,传入数组类型的定位信息，显示等待，最大等待3秒，0.1秒钟查找一次
    def find_element(self, element):
        try:
            # 保证元素可见
            WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_all_elements_located((element[0], element[1])))
            return self.driver.find_element(element[0], element[1])
        except Exception as e:
            print('页面没有该元素', e)

    # 封装定位，传入数组类型的定位信息，显示等待，最大等待3秒，0.1秒钟查找一次
    # def find_element(self, element):
    #     return WebDriverWait(self.driver, 3, 0.1).until(EC.visibility_of_element_located((element[0], element[1])))

    # 封装find_elements的定位，返回一个数组，不可直接操作，是一个数组哦
    def find_elements(self, element):
        return WebDriverWait(self.driver, 3, 0.1).until(EC.visibility_of_element_located((element[0], element[1])))

    # 封装点击事件
    def click_button(self, element):
        self.find_element(element).click()

    # 封装输入事件
    def send_text(self, element, text):
        self.find_element(element).send_keys(text)

    # 封装获取所有句柄的方法
    def get_all_handles(self):
        return self.driver.window_handles

    # 封装切换浏览器句柄的方法，输入几就是切换到第几个句柄
    def exchange_driver_handel(self, i):
        all_handles = self.get_all_handles()
        self.driver.switch_to.window(all_handles[i])

    # 封装浏览器退出的方法
    def driver_quit(self):
        self.driver.quit()

    # 封装浏览器获取该标签的文字的方法
    def get_element_text(self, element):
        return self.find_element(element).text

    # 封装清除输入的方法
    def clear_input(self, element):
        self.find_element(element).clear()

    # 封装鼠标悬浮的方法，只需要传入element
    def mouse_element(self, element):
        move = self.find_element(element)
        ActionChains(self.driver).move_to_element(move).perform()

    # 封装关闭当前浏览器的方法
    def close(self):
        self.driver.close()

    # 封装打开网页的方法
    def get_new_link(self, link):
        self.driver.get(link)
