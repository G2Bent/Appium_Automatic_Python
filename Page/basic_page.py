from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import time
import logging


class Basic_page(object):
    def __init__(self, driver):
        self.driver = driver
        self.log = Log(self)
        # 获取当前手机屏幕大小X,Y
        self.X = self.driver.get_window_size()['width']
        self.Y = self.driver.get_window_size()['height']

    def find_element(self, *loc):
        try:
            # 元素可见时，返回查找到的元素；以下入参为元组的元素，需要加*
            WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)

        except NoSuchElementException:
            logging.warning('Can not find element: %s' % loc[1])
            self.log.myloggger('Can not find element: %s' % loc[1], flag=2)
            raise
        except TimeoutException:
            self.log.myloggger('Can not find element: %s' % loc[1], flag=2)
            raise

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 30).until(lambda driver: driver.find_elements(*loc))
            return self.driver.find_elements(*loc)

        except NoSuchElementException:
            logging.warning('Can not find element: %s' % loc[1])
            self.log.myloggger('Can not find element: %s' % loc[1], flag=2)
            self.get_screenshot()
            raise

    def click(self, loc):
        logging.debug('Click element by %s: %s...' % (loc[0], loc[1]))
        self.log.myloggger('Click element by %s: %s...' % (loc[0], loc[1]), flag=0)
        try:
            self.find_element(*loc).click()
            time.sleep(2)
        except AttributeError:
            raise

    def double_click(self, loc):
        logging.debug('Click element by %s: %s...' % (loc[0], loc[1]))
        self.log.myloggger('Click element by %s: %s...' % (loc[0], loc[1]), flag=0)
        try:
            self.find_element(*loc).click()
            self.find_element(*loc).click()
        except AttributeError:
            raise

    def clicks(self, loc, index):
        logging.debug('Click element by %s: %s...' % (loc[0], loc[1]))
        self.log.myloggger('Click element by %s: %s...' % (loc[0], loc[1]), flag=0)
        try:
            self.find_elements(*loc)[index].click()
            time.sleep(2)
        except AttributeError:
            raise

    def click_back_key(self):
        self.log.myloggger('Click device back key...')
        self.driver.keyevent(4)
        time.sleep(1)

    def send_key(self, loc, text):
        try:
            logging.debug('Clear input-box: %s...' % loc[1])
            self.log.myloggger('Clear input-box: %s...' % loc[1], flag=0)
            self.find_element(*loc).clear()
            time.sleep(1)
            logging.debug('Input: %s' % text)
            self.log.myloggger('Input: %s' % text, flag=0)
            self.find_element(*loc).send_keys(text)
            self.hide_keyboard()
            time.sleep(2)
        except TimeoutException:
            raise
        except Exception:
            pass

    def send_keys(self, loc, index, text):
        try:
            logging.debug('Clear input-box: %s...' % loc[1])
            self.log.myloggger('Clear input-box: %s...' % loc[1], flag=0)
            self.find_elements(*loc)[index].clear()
            time.sleep(1)

            logging.debug('Input: %s' % text)
            self.log.myloggger('Input: %s' % text, flag=0)
            self.find_elements(*loc)[index].send_keys(text)
            time.sleep(2)
        except AttributeError:
            raise

    def hide_keyboard(self):
        self.driver.hide_keyboard()

    def is_display(self, loc):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return True
        except:
            return False

    # 获取屏幕的高度和宽度
    def get_windowsize(self):
        height = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        return height, width

    # 向上滑动屏幕
    def swipe_up(self):
        height, width = self.get_windowsize()
        self.driver.swipe(width/2, height * 3/4, width/2, height * 1/4)

    # 向下滑动屏幕
    def swipe_down(self):
        height, width = self.get_windowsize()
        self.driver.swipe(width/2, height * 1/4, width/2, height * 3/4)

    # 向左滑动屏幕
    def swipe_left(self):
        height, width = self.get_windowsize()
        self.driver.swipe(width * 3/4, height/2, width * 1/4, height/2)

    # 向右滑动屏幕
    def swipe_right(self):
        height, width = self.get_windowsize()
        self.driver.swipe(width * 1/4, height/2, width * 3/4, height/2)

    # 获取toast信息，报错
    # def find_toast(self, message):
    #     # mes = '//*[@text="请输入账号"]'
    #     elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, message))
    #     print elem

    #截图，并保存于指定目录
    def get_screenshot(self):
        dir_path = os.path.dirname(os.getcwd()) + "\\Report\\ScreenShot"
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        pic_name = 'screenshot_' + time.strftime('%Y%m%d%H%M%S') + '.png'
        pic_url = dir_path + pic_name

        try:
            self.driver.save_screenshot(pic_url)
            print ('screenshot_name:%s' % pic_name)
        except:
            raise

    # 获取当前activity的名称
    def get_current_activity_name(self):
        activity_name = self.driver.current_activity
        print ('Current activity name is: %s' % activity_name)
        return activity_name

class Log:

    def __init__(self, element):
        self.el = element

    def myloggger(self, msg, flag=1):

        log_path = os.path.dirname(os.getcwd()) + "\\Report\\log"
        if not os.path.isdir(log_path):
            os.makedirs(log_path)
        log_name = 'nw_' + time.strftime('%Y%m%d%H%M%S') + '.log'
        file_log = log_path + log_name

        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=file_log,
                            filemode='w'
                            )

        if flag == 0:
            logging.debug(msg)

        elif flag == 1:
            logging.info(msg)

        elif flag == 2:
            logging.warning(msg)
            self.el.get_screenshot()

        elif flag == -1:
            logging.error(msg)
            self.el.get_screenshot()
