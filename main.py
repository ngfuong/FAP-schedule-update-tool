import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.select import Select

firefoxBin = FirefoxBinary(r'/usr/local/firefox_dev/firefox')
driver = webdriver.Firefox(firefox_binary=firefoxBin, executable_path=r'/usr/local/bin/geckodriver')
url = "http://fap.fpt.edu.vn/"
driver.get(url)
driver.implicitly_wait(0.5)

#SELECT DROP DOWN MENU
"""
<select name="ctl00$mainContent$ddlCampus" onchange="javascript:setTimeout('__doPostBack(\'ctl00$mainContent$ddlCampus\',\'\')', 0)" id="ctl00_mainContent_ddlCampus" class="btn btn-default">
	<option selected="selected" value="">Select Campus</option>
	<option value="3">FU-Hòa Lạc</option>
	<option value="4">FU-Hồ Chí Minh</option>
	<option value="5">FU-Đà Nẵng</option>
	<option value="6">FU-Cần Thơ</option>
"""
dropdown = driver.find_element_by_xpath("//*[@name='ctl00$mainContent$ddlCampus']")
select = Select(dropdown)
select.select_by_visible_text("FU-Hồ Chí Minh")
time.sleep(5)

#CLICK BUTTON
main_page = driver.current_window_handle
button = driver.find_element_by_class_name("g-signin2")
button.click()  #pop up
time.sleep(5)

#CHANGING HANDLE TO SWITCH TO POP UP
for handle in driver.window_handles: 
    if handle != main_page: 
        login_page = handle
#LOGIN
print('Enter email id : ', end ='') 
email = input().strip() 
print('Enter password : ', end ='') 
password = input().strip()
# enter the email !!!!!!!!!!!!!!!!!!!!!
driver.find_element_by_xpath("//*[@name='identifier']").send_keys(email)
# click the next button
next = driver.find_element_by_xpath("//*[@id='identifierNext']")
next.click()
time.sleep(5)
# enter the password
driver.find_element_by_xpath('//*[@id ="password"]').send_keys(password)

# click the login button
next = driver.find_element_by_xpath('//*[@id="passwordNext"]')
next.click()
time.sleep(5)

driver.switch_to.window(main_page)
print(driver.page_source)

