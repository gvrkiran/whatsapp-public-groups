# script to go through a list of whatsapp groups and join them.

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
 

directory = "group_data_html/";
if not os.path.exists(directory):
    os.makedirs(directory)

# Replace below path with the absolute path
# to chromedriver in your computer

driver = webdriver.Chrome();
#driver = webdriver.Firefox(executable_path='/Users/kgarimella/Downloads/geckodriver');
driver.set_page_load_timeout(15) 
 
filename = sys.argv[1];
f = open(filename); # file containing the links to the whatsapp groups
lines = f.readlines();
count = 1;

driver.get("https://web.whatsapp.com");
wait = WebDriverWait(driver, 600)

time.sleep(15); # sleep for some time while I use my phone to scan the QR code

for line in lines:
    line = line.strip().strip("/");
    group_id = line.split("/")[-1];
    print >> sys.stderr, "processing", line;
    driver.get(line);
#    try:
    for i in range(1,2):
        join_button = driver.find_element_by_css_selector("#action-button");
        print >> sys.stderr, "clicked join button", group_id;
        join_button.click();
#        if(count==1):
#            time.sleep(50); # sleep first time for some time to allow for scanning the qr code
#            count += 1;
#        else:
#            sleep_time = random.randint(9,10);
#            print >> sys.stderr, "sleeping for", sleep_time;
#            time.sleep(sleep_time); # allow time for page to load
        sleep_time = random.randint(20,30);
        time.sleep(sleep_time); # allow time for page to load
        print >> sys.stderr, "sleeping for", sleep_time;
#        group_info = WebDriverWait(driver, sleep_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-body")));
        group_info = driver.find_element_by_css_selector(".popup-body");
        out = open(directory + "/" + group_id,"w");
        print >> sys.stderr, "saving info";
        out.write(group_info.get_attribute('innerHTML') + "\n");
        out.close();
#        join_group_button = WebDriverWait(driver, sleep_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-plain.btn-default.popup-controls-item")));
        join_group_button = driver.find_element_by_css_selector(".btn-plain.btn-default.popup-controls-item");
        print >> sys.stderr, "joined group", group_id;
#        if(not 
#        try:join_group_button.find_element_by_xpath("//*[contains(text(), 'Retry Now')]")):
        join_group_button.click();

#    except:
#        print >> sys.stderr, "unable to join group", line;
#        pass;

driver.close();
