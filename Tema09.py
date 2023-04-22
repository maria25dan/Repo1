'''
Implementează o clasă Login care să moștenească unittest.TestCase
Gasește elementele în partea de sus folosind ce selectors dorești:
- setUp()
- Driver
https://the-internet.herokuapp.com/
Click pe Form Authentication
tearDown()
Quit browser
'''
from datetime import datetime
from unittest import TestCase
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# service_chrome = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service_chrome)  # si daca nu este Chrome instalat, acum se va instala automat
# def get_time():
#     return datetime.now().strftime('%H:%M%S')

class Login(TestCase):
    driver = None
    LINK = "https://the-internet.herokuapp.com/"
    BUTTON_LOGIN = (By.XPATH, "//*[text()=' Login']")
    ERROR_MESSAGE = (By.ID, "flash")
    ERROR_CLOSE = (By.CLASS_NAME, "close")

    # definim metoda setUp
    def setUp(self):
        print(f"Se executa metoda setUp pentru {self._testMethodName}")
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        a_login = self.driver.find_element(By.XPATH, "//a[text()='Form Authentication']")
        a_login.click()
        self.driver.implicitly_wait(2)

    # definim metoda tearDown
    def tearDown(self):
        print(f"Se executa metoda tearDown pentru {self._testMethodName}")
        self.driver.quit()

     # metoda care primeste ca paramentru un locator
    # returneaza true daca elementul este prezent in pagina
    # sau false daca nu este prezent
    def is_element_present(self, element_locator):
        return len(self.driver.find_elements(*element_locator)) > 0

    def wait_for_element_to_be_absent(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(EC.none_of(EC.presence_of_element_located(element_locator)))

    # ● Test 1 - Verifică dacă noul url e corect
    def test_url(self):
        print(f"A inceput testul {self._testMethodName}")
        link_asteptat = "https://the-internet.herokuapp.com/login"
        link_actual = self.driver.current_url

        assert link_actual == link_asteptat, f'Invalid URL \n Expected {link_actual}, but found {link_asteptat}'

    # ● Test 2 - Verifică dacă page title e corect
    def test_title(self):
        print(f"A inceput testul {self._testMethodName}")
        titlu_initial = self.driver.title
        titlu_actual = "The Internet"

        assert titlu_initial == titlu_actual, f'Invalid, actual {titlu_actual}, but found {titlu_initial}'

    # ● Test 3 - Verifică textul de pe elementul xpath=//h2 e corect
    def test_text(self):
        print(f'A inceput testul {self._testMethodName}')
        elementul_actual = self.driver.find_element(By.XPATH, "//h2").text
        elementul_asteptat = 'Login Page'

        assert elementul_asteptat == elementul_actual, f'Invalid message \n Expected {elementul_asteptat} but found {elementul_actual}'

    # ● Test 4 - Verifică dacă butonul de login este displayed
    def test_login_displayed(self):
        print(f'A inceput testul {self._testMethodName}')
        buton_login = self.driver.find_element(*self.BUTTON_LOGIN)

        assert buton_login.is_displayed(), "Butonul nu este afisat!"

    # ● Test 5 - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    def test_atribut_hrief(self):
        print(f'A inceput testul {self._testMethodName}')
        atribut_href_1 = "http://elementalselenium.com/"
        atribut_href_2 = self.driver.find_element(By.XPATH, '//*[@id="page-footer"]/div/div/a').get_attribute('href')
        assert atribut_href_1 == atribut_href_2, f"Invalid title, expected {atribut_href_1}, but found {atribut_href_2}"

    '''
    ● Test 6 
    - Lasă goale user și pass 
    - Click login 
    - Verifică dacă eroarea e displayed
    '''

    def test_empty_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        login = self.driver.find_element(By.XPATH, "//*[@class='radius']")
        login.click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='flash']")
        assert error_message.is_displayed()

    ''' 
    ● Test 7
    - Completează cu user și pass invalide
    - Click login
    - Verifică dacă mesajul de pe eroare e corect
    - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
    expected = 'Your username is invalid!'
    self.assertTrue(expected in actual, 'Error message text is
    incorrect')
    '''

    def test_invalid_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(By.XPATH, "//*[@id='username']")
        user_field.send_keys("blablabla")
        pass_field = self.driver.find_element(By.XPATH, "//*[@id='password']")
        pass_field.send_keys(12345678)
        login = self.driver.find_element(By.XPATH, "//*[@class='radius']")
        login.click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='flash']").text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in error_message, 'Error message is incorrect')

    ''' 
    ● Test 8
    - Lasă goale user și pass
    - Click login
    - Apasă x la eroare
    - Verifică dacă eroarea a dispărut
    '''

    def test_empty_user_pass_error(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(By.XPATH, "//*[@id='username']")
        pass_field = self.driver.find_element(By.XPATH, "//*[@id='password']")
        login = self.driver.find_element(By.XPATH, "//*[@class='radius']").click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='flash']")
        assert error_message.is_displayed()

    '''
    ● Test 9
    - Ia ca o listă toate //label
    - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
    Password)
    - Aici e ok să avem 2 asserturi
    '''

    def test_empty_login_x(self):
        self.driver.find_element(*self.BUTTON_LOGIN).click()
        error = self.driver.find_element(*self.ERROR_MESSAGE)
        self.assertTrue(error.is_displayed(), "Error message is not displayed")

        self.driver.find_element(*self.ERROR_CLOSE).click()
        self.wait_for_element_to_be_absent(self.ERROR_MESSAGE, 2)

        assert not self.is_element_present(self.ERROR_MESSAGE)

    '''
    ● Test 10
    - Completează cu user și pass valide
    - Click login
    - Verifică ca noul url CONTINE /secure
    - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
    - Verifică dacă elementul cu clasa=’flash succes’ este displayed
    - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
    '''

    def test_valid_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tomsmith")
        pass_field = self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys("SuperSecretPassword!")
        click_login = self.driver.find_element(By.XPATH, "//*[@class='radius']").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='flash success']")))
        succes_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='flash success']")))
        assert succes_message.is_displayed()
        succes_message_2 = self.driver.find_element(By.XPATH, "//*[@id='flash']").text
        expected = " secure area!"
        self.assertIsNot(succes_message_2, expected, print(f"Mesajul contine textul:  {expected} "))

    '''
    ● Test 11
    - Completează cu user și pass valide
    - Click login
    - Click logout
    - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
    '''

    def test_login_logout(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tomsmith")
        pass_field = self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys("SuperSecretPassword!")
        click_login = self.driver.find_element(By.XPATH, "//*[@class='radius']").click()
        click_logout = self.driver.find_element(By.XPATH, "//*[@class='button secondary radius']").click()
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}"