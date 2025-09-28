import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Step 1 : to launch the browser
driver = webdriver.Chrome()


#step2: to control the elements  and the nevigate  the  browser
driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=945381073955500771&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061952&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1")
driver.maximize_window()
time.sleep(2)

sign_btn = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='nav-link-accountList']/a"))
    )
sign_btn.click()
print("sign button clicked successfully")

   
#step 5: fill the empty field
driver.find_element(By.ID,"ap_email_login").send_keys("9840028345")

ctn_btn = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,"a-button-input"))
    )
ctn_btn.click()
print("Continue button clicked successfully")

driver.find_element(By.ID,"ap_password").send_keys("Test@123")

#step 6: to create the account
create_btn = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"signInSubmit"))
)

create_btn.click()
print("To sign in successfully")
time.sleep(5)


# #to select the product 

deal_link = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.LINK_TEXT,"Bestsellers"))
    )
deal_link.click()
print("Bestselling  link clicked successfully")


# to select the items 
product_select = driver.find_element(By.XPATH,"//a[@class ='a-link-normal aok-block']")
product_select.click()
print("select the product successfully")


select_choice = driver.find_element(By.XPATH,"//span[@id = 'color_name_0' ]")
select_choice.click()
print("Select the favorite the product")
time.sleep(2)



buy_btn = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//input[@id = 'buy-now-button']"))
)
buy_btn.click()
print("Successful 'Buy Now' click button")

time.sleep(4)

select_cash = driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div/div[2]/div/div[10]/div[2]/div[2]/div/div/div[1]/form/div/div/div/div/div[7]/div/div/div/div/div[1]/div/label/input")
select_cash.click()
print("Successful select the 'CASH' option")

time.sleep(4)


payment_methods = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div[5]/div[1]/div/div/div[2]/div/div[10]/div[2]/div[2]/div/span/span/span/input"))
)
payment_methods.click()
print("To click the payment method button")

time.sleep(4)