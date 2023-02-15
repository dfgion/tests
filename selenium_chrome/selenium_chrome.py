from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from unittest import TestCase

def get_link(login, password):
    url = 'https://passport.yandex.ru/auth/add'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url=url)
        driver.maximize_window()
        input_login = driver.find_element(value='passp-field-login')
        input_login.clear()
        input_login.send_keys(login)
        input_login.send_keys(Keys.ENTER)
        time.sleep(3)
        input_password = driver.find_element(by='name', value='passwd')
        input_password.send_keys(password)
        input_password.send_keys(Keys.ENTER)
        time.sleep(5)
        result = driver.current_url
    except Exception as ex:
        result = 'Except'
    finally:
        driver.close()
        driver.quit()
        return result
    
def check_login(login):
    url = 'https://passport.yandex.ru/auth/add'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url=url)
        driver.maximize_window()
        input_login = driver.find_element(value='passp-field-login')
        input_login.clear()
        input_login.send_keys(login)
        input_login.send_keys(Keys.ENTER)
        time.sleep(5)
        error = driver.find_element(value='field:input-login:hint')
        if error:
            result = False
    except Exception as ex:
        result = True
    finally:
        driver.close()
        driver.quit()
        return result
    
class Test_selenium(TestCase):
    def test_link(self): # Тест показывает прошла ли авторизация или нет путем сравнения url страниц
        current_link = get_link(login='WRITE LOGIN HERE', password='WRITE PASSWORD HERE')
        correct_link = 'https://id.yandex.ru/'
        self.assertEqual(current_link, correct_link)
    def test_login(self): # Тест показывает зарегистрирован ли кто-то под логином, передаваемым в тест или нет.
        current_answer = check_login(login='WRITE LOGIN HERE')
        correct_answer = True
        self.assertEqual(correct_answer, current_answer)

