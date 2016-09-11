#coding=utf-8
from selenium import webdriver
import time,os
driver = webdriver.Chrome()
driver.get("http://189.20.210.78:8081/TellerAssistant/index.jsp")
##m=driver.find_element_by_id('modifyTellerStatusForm')
##m=driver.find_element_by_xpath('//option[@value="uat"]').click()
m=driver.find_element_by_xpath('/html/body/fieldset/form[@id="modifyTellerStatusForm"]/select/option[@value="uat"]').click()
##m.find_element_by_xpath('//option[@value="uat"]').click()
sid=driver.find_element_by_xpath('/html/body/fieldset/form[@id="modifyTellerStatusForm"]/select/option[@value="13"]').click()
driver.find_element_by_id("tellerID").send_keys("620062")
driver.find_element_by_id("submit2").click()
time.sleep(2)
alert=driver.switch_to_alert()
print alert.text
alert.accept()
time.sleep(3)


