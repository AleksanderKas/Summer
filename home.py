from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
path_to_extension = r'C:\Users\Alexander\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.6.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0,900);")
driver.find_element_by_css_selector(".post-160.product>:nth-child(2)").click()
driver.find_element_by_class_name("reviews_tab").click()
driver.find_element_by_class_name("star-5").click()
driver.find_element_by_id("comment").send_keys("Nice book!")
driver.find_element_by_id("author").send_keys("Alexander")
driver.find_element_by_id("email").send_keys("Kass86@yandex.ru")
driver.find_element_by_css_selector("#submit.submit").click()



