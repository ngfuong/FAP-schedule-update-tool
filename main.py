import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.select import Select

#firefox executable file path
firefoxBin = FirefoxBinary(r'/opt/firefox_dev/firefox')
#add gecko executable file path
driver = webdriver.Firefox(firefox_binary=firefoxBin, executable_path=r'/usr/local/bin/geckodriver')

#FETCH PAGE
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
time.sleep(2)

#CLICK SIGN IN BUTTON
main_page = driver.window_handles[0]
button = driver.find_element_by_class_name("g-signin2")
button.click()  #pop up
time.sleep(2)
print("List of windows:")
print([window for window in driver.window_handles])
login_page = driver.window_handles[1]

#CHANGING HANDLE TO SWITCH TO POP UP
driver.switch_to.window(login_page)
#for handle in driver.window_handles:
#    if handle != main_page:
#        login_page = handle

#LOGIN
print('Enter email id...')
#email = input().strip()
email = "phuonglnse150214@fpt.edu.vn"
print('Enter password: ', end ='')
password = input().strip()
driver.find_element_by_id("identifierId").send_keys(email)
# click the next button
next = driver.find_element_by_id("identifierNext")
next.click()
time.sleep(2)
# enter the password
driver.find_elements_by_name("password")[0].send_keys(password)

# click the login button
login = driver.find_element_by_id("passwordNext")
login.click()
time.sleep(2)

#SWITCH TO MAIN PAGE
driver.switch_to.window(main_page)
print(driver.page_source)

