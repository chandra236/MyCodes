from selenium import webdriver
b = webdriver.Firefox()
b.get('http://web.whatsapp.com')
raw_input()
elem = b.find_element_by_xpath('//span[contains(text(),"Devendra")]')
elem.click()
elem1 = b.find_elements_by_class_name('input')
i = 0
while i < 10:
    elem1[1].send_keys('Your whatsapp is hacked')
    b.find_element_by_class_name('send-container').click()
    i = i + 1
