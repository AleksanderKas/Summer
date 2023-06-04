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
driver.implicitly_wait(3)
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("reg_email").send_keys("Kass86@yandex.ru")
driver.find_element_by_id("reg_password").send_keys("PolaroidPolarizedSunglasses")
driver.find_element_by_css_selector(".woocomerce-FormRow>:nth-child(3)").click()
#############################################
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("Kass86@yandex.ru")
driver.find_element_by_id("password").send_keys("PolaroidPolarizedSunglasses")
driver.find_element_by_name("login").click()
driver.find_element_by_class_name("woocommerce-MyAccount-navigation-link--customer-logout")






