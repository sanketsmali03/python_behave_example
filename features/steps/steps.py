import time
from features.environment import wait__for


@when('visit url "{url}"')
def step(context, url):
    context.browser.implicitly_wait(90)
    context.browser.set_page_load_timeout(90)
    context.browser.maximize_window()
    context.browser.get(url)
    time.sleep(10)

@when('field with name "{selector}" is given "{value}"')
def step(context, selector, value):
    context.browser.find_element_by_xpath("//a[@id='signin']").click()
    context.browser.find_element_by_xpath("//div[contains(text(),'Select Username')]").click()
    context.browser.find_element_by_id("react-select-2-option-0-3").click()
    context.browser.find_element_by_xpath("//div[contains(text(),'Select Password')]").click()
    context.browser.find_element_by_id("react-select-3-option-0-0").click()
    context.browser.find_element_by_xpath("//button").click()
    context.browser.find_element_by_xpath("//span[contains(text(),'OnePlus')]").click()
    context.browser.find_element_by_xpath("(//div[contains(text(),'Add to cart')])[1]").click()
    context.browser.find_element_by_xpath("//div[contains(text(),'Checkout')]").click()
    context.browser.find_element_by_id("firstNameInput").send_keys("test")
    context.browser.find_element_by_id("lastNameInput").send_keys("test")
    context.browser.find_element_by_id("addressLine1Input").send_keys("test")
    context.browser.find_element_by_id("provinceInput").send_keys("test")
    context.browser.find_element_by_id("postCodeInput").send_keys("40000")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()
    context.browser.find_element_by_xpath("//button[normalize-space()='Continue Shopping »']").click()
    context.browser.find_element_by_xpath("//Strong[contains(text(),'Orders')]").click()
    context.browser.find_element_by_xpath("//Strong[contains(text(),'Offers')]").click()
    context.browser.find_element_by_xpath("//a[@class='Navbar_logo__26S5Y']").click()
    context.browser.find_element_by_xpath("//span[contains(text(),'Samsung')]").click()
    context.browser.find_element_by_xpath("(//div[contains(text(),'Add to cart')])[1]").click()
    context.browser.find_element_by_xpath("//div[contains(text(),'Checkout')]").click()
    context.browser.find_element_by_id("firstNameInput").send_keys("test")
    context.browser.find_element_by_id("lastNameInput").send_keys("test")
    context.browser.find_element_by_id("addressLine1Input").send_keys("test")
    context.browser.find_element_by_id("provinceInput").send_keys("test")
    context.browser.find_element_by_id("postCodeInput").send_keys("40000")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()
    context.browser.find_element_by_xpath("//button[normalize-space()='Continue Shopping »']").click()
    context.browser.find_element_by_xpath("//Strong[contains(text(),'Orders')]").click()
    context.browser.find_element_by_xpath("//Strong[contains(text(),'Offers')]").click()
    context.browser.find_element_by_xpath("//a[@class='Navbar_logo__26S5Y']").click()

     
    

    


    





   
   

    


