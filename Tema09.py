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
from webdriver_manager.chrome import ChromeDriverManager

# service_chrome = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service_chrome)  # si daca nu este Chrome instalat, acum se va instala automat
# def get_time():
#     return datetime.now().strftime('%H:%M%S')

class Login(TestCase):
    driver = None
    LINK = "https://the-internet.herokuapp.com/"
    BUTTON_LOGIN = (By.XPATH, "//*[text()=' Login']")

    #definim metoda setUp
    def setUp(self):
        print(f"Se executa metoda setUp pentru {self._testMethodName}")
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        a_login = self.driver.find_element(By.XPATH, "//a[text()='Form Authentication']")
        a_login.click()
        self.driver.implicitly_wait(2)

    #definim metoda tearDown
    def tearDown(self):
        print(f"Se executa metoda tearDown pentru {self._testMethodName}")
        self.driver.quit()

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




'''
● Test 6 
- Lasă goale user și pass 
- Click login 
- Verifică dacă eroarea e displayed
'''





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


''' 
● Test 8
- Lasă goale user și pass
- Click login
- Apasă x la eroare
- Verifică dacă eroarea a dispărut
'''




'''
● Test 9
- Ia ca o listă toate //label
- Verifică textul ca textul de pe ele să fie cel așteptat (Username și
Password)
- Aici e ok să avem 2 asserturi
'''


'''
● Test 10
- Completează cu user și pass valide
- Click login
- Verifică ca noul url CONTINE /secure
- Folosește un explicit wait pentru elementul cu clasa ’flash succes’
- Verifică dacă elementul cu clasa=’flash succes’ este displayed
- Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
'''


'''
● Test 11
- Completează cu user și pass valide
- Click login
- Click logout
- Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
'''