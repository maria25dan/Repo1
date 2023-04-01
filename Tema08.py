
'''
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
- Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
Interactionează cu un element la alegere din listă.
'''
import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

# ● Id
# driver = webdriver.Chrome()
# driver.get("https://formy-project.herokuapp.com/enabled")
# time.sleep(2)
# driver.maximize_window() #maximizez fereastra
#
# first_ID = driver.find_element(By.ID, 'disabledInput')
# first_ID.click()
#
# second_ID = driver.find_element(By.ID, 'input')
# second_ID.click()

#● Link text
# driver = webdriver.Chrome()
# driver.get("https://formy-project.herokuapp.com/")
# time.sleep(3)
# driver.maximize_window() #maximizez fereastra

# link_web_1 = driver.find_element(By.LINK_TEXT, "Autocomplete")
# link_web_1.click()
# driver.back()
# print()
#
# link_web_2 = driver.find_element(By.LINK_TEXT, "Buttons")
# link_web_2.click()
# driver.back()
# print()
#
# link_web_3 = driver.find_element(By.LINK_TEXT, "Checkbox")
# link_web_3.click()
# driver.back()
# print()

#● Parțial link text
# link_web_partial = driver.find_element((By.PARTIAL_LINK_TEXT, 'and Drop')) #am eroare
# link_web_partial.click()
# time.sleep(2)
# driver.back()
# driver.find_element(By.PARTIAL_LINK_TEXT, 'and Drop').click()  # functioneaza
# time.sleep(2)

#TAG
# driver = webdriver.Chrome()
# driver.get("https://formy-project.herokuapp.com/form")
# time.sleep(3)
# driver.maximize_window() #maximizez fereastra
# lista_inputuri = driver.find_elements(By.TAG_NAME, "input")
# print(f"Avem {len(lista_inputuri)} elemente cu tag-ul HTML <input>") #ave, 10 elemente

# driver = webdriver.Chrome()
# driver.get("https://formy-project.herokuapp.com/radiobutton")
# time.sleep(3)
# driver.maximize_window() #maximizez fereastra
# lista_meta = driver.find_elements(By.TAG_NAME, "meta")
# print(f"Avem {len(lista_meta)} elemente cu tag-ul HTML <meta>") #avem 2 elemente

# driver = webdriver.Chrome()
# driver.get("https://formy-project.herokuapp.com/enabled")
# time.sleep(3)
# driver.maximize_window() #maximizez fereastra
# lista_input_2 = driver.find_elements(By.TAG_NAME, "input")
# print(f"Avem {len(lista_input_2)} elemente cu tag-ul HTML <input>") #avem 2 elemente

#NAME

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/login")
# time.sleep(3)
# driver.maximize_window() #maximizez fereastra
# lista_input_3 = driver.find_elements(By.NAME, "username")
# print(f"Avem {len(lista_input_3)} element cu tag-ul HTML <username>") #avem 1 element

# ● Class name*

# driver = webdriver.Chrome()
# driver.get("https://formy-project.herokuapp.com/enabled")
# time.sleep(3)
# driver.maximize_window() #maximizez fereastra
# lista_class_name_1 = driver.find_elements(By.CLASS_NAME, 'form-control')
# print(f'Avem {len(lista_class_name_1)} elemente cu clasa form-control ')

# driver = webdriver.Chrome()
# driver.get("https://formy-project.herokuapp.com/form")
# time.sleep(3)
# driver.maximize_window() #maximizez fereastra
# lista_class_name_2 = driver.find_elements(By.CLASS_NAME, 'navbar-toggler')
# print(f'Avem {len(lista_class_name_2)} elemente cu clasa navbar-toggler ') # avem 1 element

# driver = webdriver.Chrome()
# driver.get("https://formy-project.herokuapp.com/form")
# time.sleep(3)
# driver.maximize_window() #maximizez fereastra
# lista_class_name_1 = driver.find_elements(By.CLASS_NAME, 'form-group')
# print(f'Avem {len(lista_class_name_1)} elemente cu clasa form-group') # avem 1 element


#● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)

# driver = webdriver.Chrome()
# driver.get("https://formy-project.herokuapp.com/form")
# time.sleep(3)
# driver.maximize_window() #maximizez fereastra
# css_id = driver.find_element(By.CSS_SELECTOR, '#logo')
# css_clasa = driver.find_element(By.CSS_SELECTOR, 'a.navbar-brand')
# css_atribut = driver.find_element(By.CSS_SELECTOR, 'input[id="last-name"]') #tag si atributul id
# driver.quit()

#---------------------------partea a 2 -a ________________________________
'''
Pentru xpath identifică elemente după criteriile de mai jos:

'''
# ----------------------------● 3 după atribut valoare
driver = webdriver.Chrome()
driver.get("https://formy-project.herokuapp.com/form")
time.sleep(2)
driver.maximize_window()
# atribut_1_absolut = driver.find_elements(By.XPATH, '/html/body/div/form/div/div[1]/input')
# print(f'Avem {len(atribut_1_absolut)} element')
#
# atribut_2_relativ = driver.find_elements(By.XPATH, '//*[@id="job-title"]')
# print(f'Avem {len(atribut_2_relativ)} element')
#
# atribut_3_relativ = driver.find_elements(By.XPATH, '//*[@id="datepicker"]')
# print(f'Avem {len(atribut_3_relativ)} element')

# ----------------------------● 3 după textul de pe element
element_text_1 = driver.find_element(By.XPATH, '//label[contains(text(),"name")]')
print(f"Avem: {(element_text_1)} elemente")
element_text_2 = driver.find_element(By.XPATH, '//label[contains(text(),"name")]')
element_text_3 = driver.find_element(By.XPATH, '//label[(text()="First name")]')
element_text_4 = driver.find_element(By.XPATH, '//label[contains(text(), "Job")]')


# ----------------------------● 1 după parțial text
element_nume = driver.find_element(By.XPATH, '//*[contains(@ID,"name")]')
print(element_nume)
# ----------------------------● 1 cu SAU, folosind pipe |

operator_pipe = driver.find_element(By.XPATH, "//*[@id='last-name'] | //*[@id='job-title']")
print(operator_pipe)

# ----------------------------● 1 cu *
operator_steluta = driver.find_element(By.XPATH, "//*[@id='datepicker']")
print(f'Avem: {(operator_steluta)} . ')

# --------● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci cu (xpath)[1]


# ----------------------------● 1 în care să folosești parent::


# ----------------------------● 1 în care să folosești fratele anterior sau de după (la alegere)


# ----------------------------● 1 funcție ca și cea de la clasă prin care să pot alege
# eu prin parametru cu ce element vreau să interacționez.