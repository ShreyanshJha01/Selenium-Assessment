# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import time

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)

# ques 1
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.facebook.com")
# driver.maximize_window()
# time.sleep(1)
#
# driver.find_element("xpath", "//input[@id='email']").send_keys("hello")
# driver.find_element("xpath", "//input[@id='pass']").send_keys("123")
#
# time.sleep(1)
# driver.find_element("xpath", "//button[@name='login']").click()
# time.sleep(1)

# ques 2
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.myntra.com")
# driver.maximize_window()
# time.sleep(1)
#
# driver.find_element("xpath", "//input[@class='desktop-searchBar']").send_keys("puma")
# time.sleep(1)
#
# driver.find_element("xpath", "//li[contains(@class,'desktop-suggestion')]").click()
# time.sleep(1)
#
# driver.find_element("xpath", "(//li[contains(@class,'product-base')])[1]").click()
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(1)
#
# driver.find_element("xpath", "//div[contains(text(),'ADD TO BAG')]").click()
# time.sleep(1)

# ques 3
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.icici.bank.in/")
# driver.maximize_window()
# time.sleep(1)
#
# driver.find_element("xpath", "//span[contains(text(),' Accounts')]").click()
# time.sleep(1)
#
# driver.find_element("xpath", '(//a[@data-itm="nli_savingsAccount_accounts_savingsAccount_productPageHeroBanner_1CTA_CMS_apply_CAMPAIGNS"])[2]').click()
# time.sleep(1)
#
# driver.switch_to.window(driver.window_handles[1])
#
# driver.find_element("xpath", '//input[@id="name"]').send_keys("hel")
# driver.find_element("xpath", '//input[@id="mobile_number"]').send_keys("65859597757")
#
# driver.find_element("xpath", "//button[contains(text(),'Apply')]").click()
# time.sleep(1)
#
# print("Validation message displayed")


## ques 4

#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.netmeds.com/")
# driver.maximize_window()
# time.sleep(1)
#
# ac = ActionChains(driver)
# menu = driver.find_element("xpath", "//a[text()=' Medicine ']")
# ac.move_to_element(menu).perform()
# time.sleep(1)
#
# driver.find_element("xpath", "//a[text()='Order Online']").click()
# time.sleep(1)
#
# driver.find_element("xpath", "//button[text()=' Upload Prescription ']").click()
# time.sleep(1)
#
# driver.find_element("xpath", "//input[@type='file']").send_keys("assessment.txt")
# time.sleep(1)

# ques 5
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.netmeds.com/")
# driver.maximize_window()
# time.sleep(1)
#
# driver.find_element("xpath", '//div[@class="position-relative profile-name"]').click()
# time.sleep(1)
#
# driver.find_element("xpath", '//input[@type="number"]').send_keys("915478619")
# driver.find_element("xpath", "//button[text()=' Get OTP ']").click()
# time.sleep(1)
#
# driver.find_element("xpath", "//input[@type='tel']").send_keys("1111111")
# time.sleep(1)

# ques 6
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.maximize_window()
# time.sleep(1)
#
# driver.find_element("xpath", "(//input[@role='searchbox'])[1]").click()
# driver.find_element("xpath", "(//input[@role='searchbox'])[1]").send_keys("KOLKATA")
# time.sleep(1)
# driver.find_element("xpath", "//span[contains(text(),'KOLKATA')]").click()
#
# driver.find_element("xpath", "(//input[@role='searchbox'])[2]").click()
# driver.find_element("xpath", "(//input[@role='searchbox'])[2]").send_keys("DELHI")
# time.sleep(1)
# driver.find_element("xpath", "//span[contains(text(),'DELHI')]").click()
#
# driver.find_element("xpath", "(//input[@type='text'])[3]").click()
# time.sleep(1)
# driver.find_element("xpath", "//a[text()='25']").click()
#
# driver.find_element("xpath", "//button[contains(text(),'Search')]").click()
# time.sleep(1)

# ques 7
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.purplle.com/")
# driver.maximize_window()
# time.sleep(1)
#
# ac = ActionChains(driver)
# menu = driver.find_element("xpath", "//a[contains(text(),'BRANDS')]")
# ac.move_to_element(menu).perform()
#
# driver.find_element("xpath", '//input[@placeholder="Search for brands..."]').send_keys("lakme")
# time.sleep(1)
#
# driver.execute_script("window.scrollTo(0,500)")
# driver.find_element("xpath", "//img[contains(@alt,'Lakme Sunscreen')]").click()
# time.sleep(1)
#
# driver.find_element("xpath", "//input[@placeholder='Enter Pincode']").send_keys("706761")
# time.sleep(1)

# ques 8
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://lifeinsurance.adityabirlacapital.com/")
# driver.maximize_window()
# time.sleep(1)
#
# driver.find_element("xpath", "(//a[text()='Her Insurance'])[2]").click()
# time.sleep(1)
#
# driver.find_element("xpath", "//input").send_keys("helo")
# time.sleep(1)
#
# driver.find_element("xpath", '//input[@id="lastName"]').send_keys("123")
# time.sleep(1)
#
# driver.find_element("xpath", '//input[@id="email"]').send_keys("hello@gmail.com")
# time.sleep(1)
#
# driver.find_element("xpath", '//input[@id="phonenumber"]').send_keys("9167890410")
# time.sleep(1)

#ques 9
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.apollopharmacy.in/")
# driver.maximize_window()
# time.sleep(1)
#
# driver.find_element("xpath", "//a[contains(text(),'Find Doctors')]").click()
# time.sleep(1)
#
# driver.find_element("xpath", "//a[contains(text(),'General Physician')]").click()
# time.sleep(1)
#
# driver.find_element("xpath", "(//div[contains(@class,'doctor')])[1]").click()
# time.sleep(1)

# ques 10
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://porter.in/")
# driver.maximize_window()
# time.sleep(1)
#
# driver.find_element("xpath", '//p[@class="CitySelector_city-selector-text__hWWNe"]').click()
# time.sleep(1)
#
# driver.find_element('xpath','(//img[@alt="City Image"])[1]').click()
# time.sleep(1)
#
# driver.find_element("xpath", "//div[contains(text(),'Packers')]").click()
# time.sleep(1)
#
# driver.find_element("xpath", "//input[@placeholder='Pickup']").send_keys("hello")
# driver.find_element("xpath", "//input[@placeholder='Drop']").send_keys("ranchi")
#
# driver.find_element("xpath", "//input[@type='tel']").send_keys("9998787899")
# time.sleep(1)
#
# driver.find_element("xpath", "//input[@type='date']").send_keys("01-04-2026")
# time.sleep(1)