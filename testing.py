from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


import requests
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

s=Service("C:\\Users\\acer\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.thesparksfoundationsingapore.org/")

print("\n \n************** Let's Check For The TestCases *********************\n")

#--------------------------------TestCase 1:Title --------------------------------
print("TestCase #1:")
if (driver.title):
    print("Title Verification Successful: ", driver.title)
else:
    print("Title Verification Failed!\n")
time.sleep(3)
print("")

#-------------------------------- TestCase 2:Home button --------------------------------
print("TestCase #2:")
try:
    driver.find_element(By.PARTIAL_LINK_TEXT,"The Sparks Foundation").click()

    print("Home link works!\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")
time.sleep(3)

#-------------------------------- TestCase 3:Check if navbar appears --------------------------------
print("TestCase #3:")
try:
    driver.find_element(By.CLASS_NAME,"navbar")
    print("Navbar Verification Successful!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")
time.sleep(3)

#-------------------------------- TestCase 4:Scrolling down --------------------------------
print("TestCase #4:")
for i in range(0, 1500, 200):
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {i})")
    time.sleep(1)
print("scrolled down")

###################### TestCase 5:scrolling up ######################################
print("TestCase #5:")
driver.find_element(By.ID,"toTopHover").click()
time.sleep(1)
print("scrolled up")
print("")

#-------------------------------- TestCase 6:About Us Page --------------------------------
print("TestCase #6:")
try:
    driver.find_element(By.LINK_TEXT,'About Us').click()
    time.sleep(3)

    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)

#-------------------------------- TestCase 7:Policies and Code --------------------------------
print('TestCase #7:')
try:
    driver.find_element(By.LINK_TEXT,'Policies and Code').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Policies").click()
    time.sleep(3)
    print('Policy page exists. Success!\n')
except NoSuchElementException:
    print('Policy Page Does not exist. Failed!\n')
    time.sleep(3)

#-------------------------------- TestCase 8:Workshop page --------------------------------
print('TestCase #8:')
try:
    driver.find_element(By.LINK_TEXT,'Programs').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Workshops").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,'LEARN MORE').click()
    time.sleep(3)
    print('Workshop Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

#-------------------------------- TestCase 9: Check If Logo Exists --------------------------------
print('TestCase #9:')
try:
    driver.find_element(By.XPATH,'//*[@id="home"]/div/div[1]/h1/a/*').click()
    print('Found Logo! Success!\n')
    time.sleep(3)
except NoSuchElementException:
    print('No logo found!\n')

time.sleep(4)
driver.switch_to.window(driver.window_handles[0])
print("switched to 1st Tab\n")
time.sleep(1.5)

#-------------------------------- TestCase 10:Check the Form --------------------------------
print("TestCase #10:")
try:
    driver.find_element(By.LINK_TEXT,'Join Us').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,'Why Join Us').click()
    time.sleep(3)
    print("Typing your name...")
    driver.find_element(By.NAME,'Name').send_keys('Shivam Neware')
    time.sleep(3)
    print("Typing your Email address...")
    driver.find_element(By.NAME,'Email').send_keys('shivamneware9@gmail.com')
    time.sleep(3)
    select = Select(driver.find_element(By.CLASS_NAME,'form-control'))
    time.sleep(3)
    select.select_by_visible_text('Student')
    time.sleep(3)
    driver.find_element_by(By.CLASS_NAME,'button-w3layouts').click()
    time.sleep(3)
    print("Form Verification Successful!\n")
    time.sleep(3)
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(3)

# --------------------------------TestCase 11:Check the Contact us Page --------------------------------
print("TestCase #11:")
try:
    driver.find_element(By.LINK_TEXT,"Contact Us").click()
    time.sleep(1)
    info = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(1)

    if (info.text == "+65-8402-8590, info@thesparksfoundation.sg"):
        print('contact Information Correct!')
    else:
        print('Contact Information Incorrect!')

    print("Contact Page Verification Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification unsuccessful!")

########################### TestCase 12:again back to main page #########################


print("TestCase #12:")
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/h1/a").click()
print(" again back to main page")
time.sleep(3)
print("")

