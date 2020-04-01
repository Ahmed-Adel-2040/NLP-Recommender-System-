#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:04:03 2020

@author: ahmed-adel
"""


import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time


#binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList",2)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,text/x-csv,text/csv,application/vnd.ms-excel,application/csv,application/x-csv,text/csv,text/comma-separated-values,text/x-comma-separated-values,text/tab-separated-values,application/pdf")
profile.set_preference("browser.download.manager.showWhenStarting",False)
profile.set_preference("browser.helperApps.neverAsk.openFile","text/plain,text/x-csv,text/csv,application/vnd.ms-excel,application/csv,application/x-csv,text/csv,text/comma-separated-values,text/x-comma-separated-values,text/tab-separated-values,application/pdf")
profile.set_preference("browser.helperApps.alwaysAsk.force", False)
profile.set_preference("browser.download.manager.useWindow", False)
profile.set_preference("browser.download.manager.focusWhenStarting", False)
profile.set_preference("browser.helperApps.neverAsk.openFile", "")
profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
profile.set_preference("browser.download.manager.showAlertOnComplete", False)
profile.set_preference("browser.download.manager.closeWhenDone", True)
profile.set_preference("pdfjs.disabled", True)

caps = DesiredCapabilities.FIREFOX


df=pd.read_csv('All Industries.csv') 
codes=df['Code'].tolist()
newpath=''
length=len(codes)

for page in range(286,length):
    newpath = '/home/ahmed-adel/Data science/projects/Image Classifier/'+codes[page]
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    profile.set_preference("browser.download.dir",newpath)
    driver = webdriver.Firefox(firefox_profile=profile, capabilities=caps)
    
    print(newpath)

    url="https://www.onetonline.org/link/details/"+codes[page]
   

    driver.get(url)
    
    s= driver.find_elements_by_xpath("//a[contains(@title, 'Comma-Separated Values')]")
    if s:
        for cc in s:
            cc.click()
            time.sleep(1)
    driver.close()
    
   
    #done
#    job_Name=driver.find_element_by_xpath("//span[contains(@class, 'titleb')]").text
#    #done
#    #Last_Update=driver.find_element_by_xpath("//div[contains(@class, 'updates')]").text
#    #done
#    job_Description=driver.find_element_by_xpath('/html/body/div/div[4]/div/p[1]').text
#    #done
#    sample_Of_Report=driver.find_element_by_xpath('/html/body/div/div[4]/div/p[2]').text
#    #done
#    detailsKey=driver.find_element_by_xpath("//p[contains(@class, 'sm')]").text
#    
#    x=detailsKey.split('|')
#    detais=[]
#    for m in x:
#        m=m.replace(" ", "") 
#        detais.append(m)
#    
        
    #values=[]
    #record_Dictionary={}
    #recodList=[]
   
            
        
        
    
    
#//*[@id="wrapper_ToolsUsed"]/h2/span/a[2]
#//*[@id="wrapper_TechnologySkills"]/h2/span/a[2]        
#        for sub in subs:
#            subKeys.append(sub.text)
#    
#    record_Dictionary[key]=subKeys
#    
    
#        value=element.find_elements_by_xpath("//td[contains(@class, 'report2')]")
#        for v in value:
#            values.append(v.text)





    

#sohwMoreButtons=driver.find_elements_by_xpath("//div[contains(@class, 'collapse short')]")
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#for element in sohwMoreButtons:
#    if type(element.find_element_by_tag_name('a')) != 'FirefoxWebElement':
#        element.find_element_by_css_selector('a').click()
#        
#        time.sleep(3)










