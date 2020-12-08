from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )

if (button):
	bbutton = browser.find_element_by_css_selector("button#book")
	bbutton.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

ans_element = browser.find_element_by_id("answer")
ans_element.send_keys(y)

button = browser.find_element_by_css_selector("button#solve")
button.click()