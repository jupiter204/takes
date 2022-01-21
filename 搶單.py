from select import select
import time
from time import sleep
from selenium import webdriver
browser = webdriver.Edge("D:\code\python\搶單\msedgedriver.exe")
def login():
    browser.get("https://ecssl.pchome.com.tw/sys/cflow/fsindex/BigCar/BIGCAR/ItemList")
    sleep(3)
    account = browser.find_element_by_xpath("//*[@id=\"loginAcc\"]")
    account.clear()
    account.send_keys("ss0922071773@gmail.com")
    passwd = browser.find_element_by_xpath("//*[@id=\"loginPwd\"]")
    passwd.clear()
    passwd.send_keys("s0937876554s")
    browser.find_element_by_xpath("//*[@id=\"btnLogin\"]").click()

def buy_home():
    browser.find_element_by_xpath("//*[@id=\"a_cod\"]").click()
    mobile=browser.find_element_by_xpath("//*[@id=\"BuyerMobile\"]")
    mobile.clear()
    mobile.send_keys("0937876554")
    browser.find_element_by_xpath("//*[@id=\"syncData\"]").click()
    rmobile=browser.find_element_by_xpath("//*[@id=\"ReceiverMobile\"]")
    rmobile.clear()
    rmobile.send_keys("0937876554")
    browser.find_element_by_xpath("//*[@id=\"frmUserInfo\"]/dl[4]/dd[2]/div[1]/div[2]/label/input").click()
    browser.find_element_by_xpath("//*[@id=\"chk_agree\"]").click()
    browser.find_element_by_xpath("//*[@id=\"btnSubmit\"]").click()

def buy_711():
    browser.find_element_by_xpath("//*[@id=\"radio_24hMarket\"]").click()
    browser.find_element_by_xpath("//*[@id=\"btn_use711\"]").click()
    sleep(1)
    browser.find_element_by_xpath("//*[@id=\"warning_btn_confirm\"]").click()
    sleep(0.2)
    browser.find_element_by_xpath("//*[@id=\"syncData\"]").click()
    browser.find_element_by_xpath("//*[@id=\"syncData\"]").click()
    browser.find_element_by_xpath("//*[@id=\"chk_agree\"]").click()
    browser.find_element_by_xpath("//*[@id=\"btnSubmit\"]").click()
login()
sleep(6)
while True:
    localtime = time.localtime()
    if localtime.tm_hour == 12 and localtime.tm_min == 59 :
        buy_711()
        break
    sleep(1)
print ("done")
exit()