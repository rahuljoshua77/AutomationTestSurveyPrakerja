import undetected_chromedriver as uc
uc.install()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import random
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
 
cwd = os.getcwd()

opts = webdriver.ChromeOptions()
opts.headless = True
opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
opts.add_argument('--ignore-ssl-errors=yes')
opts.add_argument("--start-maximized")

opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_experimental_option('excludeSwitches', ['enable-logging'])

def xpath_type(el,mount):
    return wait(browser,1).until(EC.presence_of_element_located((By.XPATH, el))).send_keys(mount)

def xpath_el(el):
    element_all = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, el)))
    browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all)


def page_six():
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div/div[2]/fieldset/div[1]/label/input")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[3]/div/div[2]/fieldset/div[1]/label/input")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[4]/div/div[2]/fieldset/div[1]/label/input")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[5]/div/div[2]/fieldset/div[3]/label/input")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[6]/div/div[2]/fieldset/div[2]/label/input")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[7]/div/div[2]/fieldset/div[2]/label/input")
    element = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '(//input[@value="Selanjutnya" or @value="Selesai"])')))
    browser.execute_script("arguments[0].click();", element)

def page_five():
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div/div[2]/div/label[2]/span")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[3]/div/div[2]/fieldset/div[1]/label/input")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[4]/div/div[2]/fieldset/div[1]/label/input")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[5]/div/div[2]/fieldset/div[3]/label/input")
    for i in range(1,7):
        xpath_el(f"/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[6]/div/div[2]/div/fieldset/table/tbody/tr[{i}]/td[{random.randint(2,3)}]/label/input")
    try:
        for i in range(1,16):
            xpath_el(f"/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[7]/div/div[2]/div/fieldset/table/tbody/tr[{i}]/td[{random.randint(2,3)}]/label/input")
    except:
        pass
    element = wait(browser,5).until(EC.presence_of_all_elements_located((By.XPATH, "(//input[@type='number'])")))
    get_idx = len(element)+1
    try:
        for i in range(0,get_idx):
            element[i].send_keys('50000')
            try:
                wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[10]/div/div[2]/input'))).send_keys('5000')
            except:
                pass
            browser.execute_script("arguments[0].scrollIntoView();", element[i])
    except:
        pass
    element = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '(//input[@value="Selanjutnya" or @value="Selesai"])')))
    browser.execute_script("arguments[0].click();", element)
    sleep(0.5)
    

def page_four():
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div/div[2]/fieldset/div[2]/label/input")
    for i in range(1,8):
        xpath_el(f"/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[3]/div/div[2]/div/fieldset/table/tbody/tr[{i}]/td[{random.randint(2,3)}]/label/input")
    for i in range(1,5):
        xpath_el(f"/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[4]/div/div[2]/div/fieldset/table/tbody/tr[{i}]/td[4]/label/input")
  
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[5]/div/div[2]/fieldset/div[2]/label/input")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[6]/div/div[2]/div/label[9]/span")
    for i in range(1,6):     
        xpath_el(f"/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[7]/div/div[2]/div/fieldset/table/tbody/tr[{i}]/td[2]/label/input")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[8]/div/div[2]/fieldset/div[2]/label/input")
    element = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '(//input[@value="Selanjutnya" or @value="Selesai"])')))
    browser.execute_script("arguments[0].click();", element)

def page_three():
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div/div[2]/fieldset/div[2]/label/input")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[3]/div/div[2]/fieldset/div[2]/label/input")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[4]/div/div[2]/div/fieldset/table/tbody/tr[1]/td[2]/label/input")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[4]/div/div[2]/div/fieldset/table/tbody/tr[2]/td[3]/label/input")
    for i in range(1,5):
        xpath_el(f"/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[5]/div/div[2]/div/fieldset/table/tbody/tr[{i}]/td[{random.randint(2,3)}]/label/input")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[6]/div/div[2]/fieldset/div[1]/label/input")
    element = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '(//input[@value="Selanjutnya" or @value="Selesai"])')))
    browser.execute_script("arguments[0].click();", element)

def page_two():
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div/div[2]/fieldset/div[2]/label/input")
    element = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '(//input[@value="Selanjutnya" or @value="Selesai"])')))
    browser.execute_script("arguments[0].click();", element)

def page_one():
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div/div[2]/fieldset/div[2]/label/input")
    xpath_el("/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[3]/div/div[2]/fieldset/div[1]/label/input")
    element = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/section/div/div/div[2]/form/div[2]/div/div[1]/div[4]/div/div[2]/fieldset/div[1]/label/input")))
    browser.execute_script("arguments[0].click();", element)
    element = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '(//input[@value="Selanjutnya" or @value="Selesai"])')))
    browser.execute_script("arguments[0].click();", element)
     
def radio_button():
    try:
        page_one()
        print(f"[{time.strftime('%d-%m-%y %X')}] [ {email} ] Page One Done")
    except Exception as e:
        pass
    try:
        page_two()
        print(f"[{time.strftime('%d-%m-%y %X')}] [ {email} ] Page Two Done")
    except Exception as e:
        pass
    try:
        page_three()
        print(f"[{time.strftime('%d-%m-%y %X')}] [ {email} ] Page Three Done")
    except Exception as e:
        pass
    try:
        page_four()
        print(f"[{time.strftime('%d-%m-%y %X')}] [ {email} ] Page Four Done")
    except Exception as e:
        pass
    try:
        page_five()
        print(f"[{time.strftime('%d-%m-%y %X')}] [ {email} ] Page Five Done")
    except Exception as e:
        pass
    try:
        page_six()
        print(f"[{time.strftime('%d-%m-%y %X')}] [ {email} ] Page Six Done")
    except Exception as e:
        pass

    notif = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/section/div/div/div[2]'))).text
    if "Lihat Pelatihan" in notif or "Seksi WB: Kesejahteraan" in notif:
        print(f"[{time.strftime('%d-%m-%y %X')}] [ {email} ] Survey Failed")
        with open('failed.txt','a') as f:
            f.write('{0}|{1}\n'.format(email,password))
    else:
        if "\n" in notif:
            notif = notif.split("\n")
            notif = notif[1]
        print(f"[{time.strftime('%d-%m-%y %X')}] [ {email} ] Success Survey, {notif.strip()}")
        with open('success_survei.txt','a') as f:
            f.write('{0}|{1}\n'.format(email,password))
    browser.quit()

def private_accept():
    
    xpath_el('/html/body/div[2]/div[4]/div/div/div/div/form/div[2]/div[1]/label')
    xpath_el("//button[contains(text(),'Lanjutkan')]")
    print(f"[{time.strftime('%d-%m-%y %X')}] [ {email} ] Checked Ya")
    radio_button()

def login():
    print(f"[{time.strftime('%d-%m-%y %X')}] [ {email} ] Login Account")
    browser.refresh()
    element = wait(browser,20).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="email"]')))
    element.send_keys(email)
        
    sleep(0.2)
     
    element = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
    
    element.send_keys(password)
    sleep(0.5)
      
    wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))).click()
    try:
        private_accept()
    except:
        try:
            radio_button()
        except:
            pass

def open_browser(k):
    
    global browser
    global element
    global email
    global password
    k = k.split("|")
    email = k[0]
    password = k[1]
    random_angka = random.randint(100,999)
    random_angka_dua = random.randint(10,99)
    opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.{random_angka}.{random_angka_dua} Safari/537.36")
    browser = webdriver.Chrome(options=opts, desired_capabilities=dc)
    browser.get('https://dashboard.prakerja.go.id/masuk')
    try:
        login()
    except Exception as e:
        print(f"[{time.strftime('%d-%m-%y %X')}] [ {email} ] Failed Login, Error: {e}")
        with open('failed.txt','a') as f:
            f.write('{0}|{1}\n'.format(email,password))
        browser.quit()
if __name__ == '__main__':
    global list_accountsplit
    print(f"[{time.strftime('%d-%m-%y %X')}] Automation Survey")
    jumlah = int(input(f"[{time.strftime('%d-%m-%y %X')}] Multi Processing: "))
    file_list_akun = "prakerja.txt"
    myfile_akun = open(f"{cwd}/{file_list_akun}","r")
    akun = myfile_akun.read()
    list_accountsplit = akun.split("\n")
    k = list_accountsplit

    with Pool(jumlah) as p:  
        p.map(open_browser, k)
    
