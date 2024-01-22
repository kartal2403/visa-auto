from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

email = "email"
password = "password"

driver = webdriver.Chrome('/Users/sipanmerhasakcan/dev/chromedriver')

driver.get('https://ais.usvisa-info.com/tr-tr/niv/users/sign_in')
search_box = driver.find_element_by_name('user[email]')
search_box.send_keys(email)
search_box = driver.find_element_by_name('user[password]')
search_box.send_keys(password)
button = driver.find_element_by_xpath('//*[@id="sign_in_form"]/div[3]/label/div')
button.click()
button = driver.find_element_by_xpath('//*[@id="sign_in_form"]/p[1]/input') # Butonun ID'si 'button_id'
button.click()
time.sleep(2)
button = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/ul/li/a') # Butonun ID'si 'button_id'
button.click()
time.sleep(2)
button = driver.find_element_by_xpath('/html/body/div[4]/main/div[2]/div[2]/div/section/ul/li[1]/a') # Butonun ID'si 'button_id'
button.click() 
time.sleep(2)
button = driver.find_element_by_xpath('/html/body/div[4]/main/div[2]/div[2]/div/section/ul/li[1]/div/div/div[2]/p[2]/a') # Butonun ID'si 'button_id'
button.click()

def ComboboxSec():
    combobox_element = driver.find_element_by_xpath("/html/body/div[4]/main/div[4]/div/div/form/fieldset/ol/fieldset/div/div[2]/div[1]/div/li/select")  
    # Combobox'ı seç
    select = Select(combobox_element)
    select.select_by_visible_text("Istanbul")
    # Butonu bulma ve tıklama
    time.sleep(3)
    button = driver.find_element_by_xpath('/html/body/div[4]/main/div[4]/div/div/form/fieldset/ol/fieldset/div/div[2]/div[3]/li[1]/input') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

def GunAraOcak():
    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[1]/td[2]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[1]/td[3]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[1]/td[4]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[1]/td[5]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[1]/td[6]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[1]/td[7]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[2]/td[1]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[2]/td[2]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[2]/td[3]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[2]/td[4]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[2]/td[5]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[2]/td[6]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[2]/td[7]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[3]/td[1]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[3]/td[2]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[3]/td[3]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[3]/td[4]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[3]/td[5]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[3]/td[6]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[3]/td[7]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[4]/td[1]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[4]/td[2]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[4]/td[3]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[4]/td[4]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[4]/td[5]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[4]/td[6]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[4]/td[7]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[5]/td[1]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[5]/td[2]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[5]/td[3]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[1]/table/tbody/tr[5]/td[4]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

def GunAraSubat():
    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[1]/td[5]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[1]/td[6]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[1]/td[7]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[2]/td[1]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[2]/td[2]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[2]/td[3]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[2]/td[4]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[2]/td[5]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[2]/td[6]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[2]/td[7]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[3]/td[1]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[3]/td[2]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[3]/td[3]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[3]/td[4]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[3]/td[5]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[3]/td[6]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[3]/td[7]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[4]/td[1]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[4]/td[2]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[4]/td[3]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[4]/td[4]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[4]/td[5]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[4]/td[6]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[4]/td[7]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[5]/td[1]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[5]/td[2]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[5]/td[3]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

    # Butonu bulma ve tıklama
    button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[5]/td[4]/span') # Butonun ID'si 'button_id'
    button.click() # Butona tıklama

while True:
    ComboboxSec()
    GunAraOcak()
    GunAraSubat
    driver.refresh()