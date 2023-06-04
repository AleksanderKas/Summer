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
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("Kass86@yandex.ru")
# driver.find_element_by_id("password").send_keys("PolaroidPolarizedSunglasses")
# driver.find_element_by_name("login").click()
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector(".masonry-done>:nth-child(3)").click()
# Title = driver.find_element_by_class_name("product_title.entry-title")
# Title_check = Title.text
# assert Title_check == "HTML5 Forms"
#######################################################

# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("Kass86@yandex.ru")
# driver.find_element_by_id("password").send_keys("PolaroidPolarizedSunglasses")
# driver.find_element_by_name("login").click()
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector(".cat-item.cat-item-19>:nth-child(1)").click()
# Cart = driver.find_element_by_css_selector(".current-cat>:nth-child(2)")
# Cart_check = Cart.text
# assert Cart_check == "(3)"
#######################################################
# from selenium.webdriver.support.select import Select
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("Kass86@yandex.ru")
# driver.find_element_by_id("password").send_keys("PolaroidPolarizedSunglasses")
# driver.find_element_by_name("login").click()
# driver.find_element_by_id("menu-item-40").click()
# Default = driver.find_element_by_css_selector(".orderby>:nth-child(1)")
# Default_status_check = Default.get_attribute("value")
# assert Default_status_check == "menu_order"
# element = driver.find_element_by_class_name("orderby")
# select = Select(element)
# select.select_by_value("price-desc")
# element = driver.find_element_by_class_name("orderby")
# element_check = element.get_attribute("value")
# assert element_check == "price-desc"
#######################################################
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("Kass86@yandex.ru")
# driver.find_element_by_id("password").send_keys("PolaroidPolarizedSunglasses")
# driver.find_element_by_name("login").click()
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector(".products.masonry-done>:nth-child(1)").click()
# old_price = driver.find_element_by_css_selector(".price>del>span")
# old_price_value = old_price.text
# assert old_price_value == "₹600.00"
# new_price = driver.find_element_by_css_selector(".price>ins>span")
# new_price_value = new_price.text
# assert new_price_value == "₹450.00"
# driver.find_element_by_css_selector(".images>:nth-child(1)").click()
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images>:nth-child(1)")))
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()
################################################################################






























