
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

#cu NAME n-am facut, nu mi-e clar de unde il iau. Noi la clasa am facut exemple cu TAG_NAME


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
va urma...
Pentru xpath identifică elemente după criteriile de mai jos:
● 3 după atribut valoare
● 3 după textul de pe element
● 1 după parțial text
● 1 cu SAU, folosind pipe |
● 1 cu *
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]
● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
ce element vreau să interacționez.
'''

