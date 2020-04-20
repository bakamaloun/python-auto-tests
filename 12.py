import time
import math
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button_r = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
    button_r.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    #alert = browser.switch_to.alert
    #alert.accept()
    value = browser.find_element_by_id("input_value")
    x_element = value.text
    print(x_element)
    x = int(x_element)
    y = str(math.log(abs(12*math.sin(int(x)))))
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()