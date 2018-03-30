# script to just open one whatsapp chat group after another and store their titles.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,time,random
from selenium.webdriver.remote.remote_connection import LOGGER
import logging,os
LOGGER.setLevel(logging.WARNING)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# encoding=utf8 
reload(sys)  
sys.setdefaultencoding('utf8')
 

# Replace below path with the absolute path
# to chromedriver in your computer

driver = webdriver.Chrome();
#driver = webdriver.Firefox(executable_path='/Users/kgarimella/Downloads/geckodriver');
driver.set_page_load_timeout(3) 

filename = "whatsapp_group_links.txt";
f = open(filename); # file containing the links to the whatsapp groups
lines = f.readlines();
count = 1;

#driver.get("https://web.whatsapp.com");
#wait = WebDriverWait(driver, 600)

#time.sleep(15); # sleep for some time while I use my phone to scan the QR code

for line in lines:
    try:
        line = line.strip().strip("/");
        group_id = line.split("/")[-1];
        print >> sys.stderr, "processing", line;
        driver.get(line);
        group_info = driver.find_element_by_css_selector(".block__title");
        title = group_info.get_attribute('innerHTML');
        print group_id + "\t" + title;
        sleep_time = random.randint(1,5);
        time.sleep(sleep_time);
    except:
        print >> sys.stderr, "fx";
        pass;
