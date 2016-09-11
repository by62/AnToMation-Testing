#coding=utf-8
def input_():
    driver.find_element_by_xpath('/html/body/fieldset/form[@id="modifyTellerStatusForm"]/select/option[@value="uat"]').click()
    driver.find_element_by_xpath('/html/body/fieldset/form[@id="modifyTellerStatusForm"]/select/option[@value="13"]').click()
    driver.find_element_by_id("tellerID").send_keys("620062")
