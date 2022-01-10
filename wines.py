import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

dr = webdriver.Chrome()
dr.get('https://www.wine-searcher.com/biz/all')

x = 1
time.sleep(2)

#pages
for p in range(1, 2, 1):

    #items
    for i in range(2, 26, 1):

        name = dr.find_element_by_xpath('//*[@id="merchantsearch"]/tbody/tr[' + str(i) + ']/td[1]/a')
        address = dr.find_element_by_xpath('//*[@id="merchantsearch"]/tbody/tr[' + str(i) + ']/td[4]/small').text
        
        wines = dr.find_element_by_xpath('//*[@id="merchantsearch"]/tbody/tr[' + str(i) + ']/td[3]/small').text
        wines = re.search('[0-9]+', wines).group()
        
        name.click()
        time.sleep(10)
        
        phone = dr.find_element_by_css_selector('#content-block > div > div > div > div.fwidth-block-r-300 > div > div:nth-child(1) > div.merc-cont.merc-cont-detail > div:nth-child(3) > ul > li > span.merc-contact > span').text
                
        while '+' not in phone: 
            x += 1
            phone = dr.find_element_by_css_selector('#content-block > div > div > div > div.fwidth-block-r-300 > div > div:nth-child(1) > div.merc-cont.merc-cont-detail > div:nth-child(3) > ul > li > span.merc-contact > span').text
            
            if '+' in phone:
                x = 1
                break
                
        dr.back()
        
        name = dr.find_element_by_xpath('//*[@id="merchantsearch"]/tbody/tr[' + str(i) + ']/td[1]/a').text
        print('name: ' + name)
        print('wines: ' + wines)
        print('address: ' + address)
        print('phone: ' + phone)
        
        time.sleep(4)
        
        if i == 26:
            dr.find_element_by_xpath('//*[@id="merchantsearch"]/tbody/tr[27]/td/div/a[9]').click()