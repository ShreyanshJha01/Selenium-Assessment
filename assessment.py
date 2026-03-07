
# # ques 1
# import time
# from selenium import webdriver

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)

# driver = webdriver.Chrome(opts)

# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()

# driver.find_element('xpath', '(//a[contains(text(),"Books")])[1]').click()
# time.sleep(1)

# driver.find_element('xpath', '(//input[@value="Add to cart"])[1]').click()
# time.sleep(1)

# driver.find_element('xpath', '//span[text()="Shopping cart"]').click()
# time.sleep(1)

# product = driver.find_element('xpath', '//a[@class="product-name"]')

# if product.is_displayed():
#     print("Product is present in the cart")
# else:
#     print("Product is not present in the cart")

# time.sleep(1)
# driver.close()




# #ques 2
# import time
# from selenium import webdriver

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)

# driver = webdriver.Chrome(opts)

# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# time.sleep(1)


# driver.find_element("xpath" , '//a[contains(text(),"Electronics")]').click()
# driver.find_element("xpath" , '(//a[@title="Show products in category Cell phones"])[2]').click()
# time.sleep(1)
# driver.close()

# #ques3
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)

# driver = webdriver.Chrome(opts)
# waitObj = WebDriverWait(driver, 20)

# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# time.sleep(1)

# driver.find_element('xpath', '//button[text()="Start"]').click()

# waitObj.until(EC.visibility_of_element_located(('xpath', '//h4[text()="Hello World!"]')))

# text = driver.find_element('xpath', '//h4[text()="Hello World!"]').text
# print(text)
# time.sleep(1)
# driver.close()



# ques 4
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)

# driver = webdriver.Chrome(opts)
# waitObj = WebDriverWait(driver,20)

# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# time.sleep(2)

# driver.find_element("xpath","//button[text()='Remove']").click()

# waitObj.until(EC.element_to_be_clickable(("xpath","//button[text()='Add']")))

# driver.find_element("xpath","//button[text()='Add']").click()
# time.sleep(1)
# driver.close()




# # ques 5
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)

# driver = webdriver.Chrome(opts)

# driver.get("https://demoqa.com/select-menu")
# driver.maximize_window()
# wait = WebDriverWait(driver,10)

# dropdown = wait.until(EC.element_to_be_clickable(("id","withOptGroup")))
# dropdown.click()

# option = wait.until(EC.element_to_be_clickable(("xpath","//div[text()='Group 2, option 1']")))
# option.click()

# selected_value = driver.find_element("xpath","//div[contains(@class,'singleValue')]").text

# print("Selected Value:", selected_value)

# if selected_value == "Group 2, option 1":
#     print("Verification Passed")
# else:
#     print("Verification Failed")

# time.sleep(1)
# driver.close()



# # #ques 6
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)

# driver = webdriver.Chrome(opts)
# ac = ActionChains(driver)

# driver.get("https://demoqa.com/select-menu")
# time.sleep(2)

# element = driver.find_element("xpath","//select[@id='cars']")
# ac.scroll_to_element(element).perform()
# time.sleep(2)

# select = Select(element)

# select.select_by_visible_text("Volvo")
# select.select_by_visible_text("Saab")
# select.select_by_visible_text("Opel")

# options = select.all_selected_options

# for i in options:
#     print(i.text)
# time.sleep(1)
# driver.close()


# #ques 7
# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)

# driver = webdriver.Chrome(opts)
# ac = ActionChains(driver)

# driver.get("https://demoqa.com/menu/")
# driver.maximize_window()
# time.sleep(2)

# main_item = driver.find_element("xpath","//a[text()='Main Item 2']")
# ac.move_to_element(main_item).perform()
# time.sleep(2)

# sub_list = driver.find_element("xpath","//a[text()='SUB SUB LIST »']")
# ac.move_to_element(sub_list).perform()
# time.sleep(2)

# sub_item = driver.find_element("xpath","//a[text()='Sub Sub Item 1']")
# ac.move_to_element(sub_item).click().perform()

# time.sleep(1)
# driver.close()


# # #ques 8 
# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains


# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)

# driver = webdriver.Chrome(opts)
# ac = ActionChains(driver)

# driver.get("https://demoqa.com/droppable")
# driver.maximize_window()
# time.sleep(2)

# src = driver.find_element("xpath",'//div[@id="draggable"]')
# tar = driver.find_element("xpath","//div[@id='droppable']")

# ac.drag_and_drop(src , tar).perform()
# time.sleep(3)

# text = driver.find_element("xpath","//div[@id='droppable']/p").text
# print(text)

# time.sleep(1)
# driver.close()


# # ques 9
# import time
# from selenium import webdriver

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)

# driver = webdriver.Chrome(opts)

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# time.sleep(1)

# driver.find_element("xpath","//button[text()='Click for JS Confirm']").click()
# time.sleep(1)

# alert = driver.switch_to.alert
# alert.accept()

# result = driver.find_element("id","result").text
# print(result)

# if result == "You clicked: Ok":
#     print("Verification Passed")
# else:
#     print("Verification Failed")

# time.sleep(1)
# driver.close()




# #ques 10
# import time
# from selenium import webdriver

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)

# driver = webdriver.Chrome(opts)

# driver.get("https://the-internet.herokuapp.com/upload")
# driver.maximize_window()
# time.sleep(1)

# filePath = "/home/speedhack/Documents/deep_learning/selenium_training/assessment/abc.txt"

# driver.find_element("id","file-upload").send_keys(filePath)
# time.sleep(1)

# driver.find_element("id","file-submit").click()
# time.sleep(1)

# uploadedFile = driver.find_element("id","uploaded-files").text
# print(uploadedFile)


# time.sleep(1)
# driver.close()


#ques 11
# Steps to Read Data from Excel

# import xlrd
# path = "file_path.xlsx"
# workbook = xlrd.open_workbook(path)
# worksheet = workbook.sheet_by_name("Sheet1")
# rows = worksheet.get_rows()
# for ele in rows:
#     print(ele[0].value, ele[1].value, ele[2].value)




# ques 12
# XPath Syntax

#  Using Attribute
#  //tagname[@attribute="value"]
# Example : //input[@id="user-name"]

#  Using Text
#  //tagname[text()="text"]
# Example : //a[text()="Books"]


#  Group Indexing
#  (//tagname[@attribute="value"])[index]
# Example :   (//input[@type="text"])[2]


# Using Contains
#  //tagname[contains(text(),"partial_text")]
# Example :  //span[contains(text(),"Products")]
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)

# driver = webdriver.Chrome(opts)
# ac = ActionChains(driver)

# driver.get("https://demoqa.com/select-menu")
# time.sleep(2)

# element = driver.find_element("xpath","//select[@id='cars']")
# ac.scroll_to_element(element).perform()
# time.sleep(2)

# select = Select(element)

# select.select_by_visible_text("Volvo")
# select.select_by_visible_text("Saab")
# select.select_by_visible_text("Opel")

# options = select.all_selected_options

# for i in options:
#     print(i.text)
# time.sleep(1)
# driver.close()


# #ques 7