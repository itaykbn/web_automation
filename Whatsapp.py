import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class Whatsapp:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def send_whatsapp(self, to, message):
        self.driver.get("https://web.whatsapp.com/")

        # Replace 'Friend's Name' with the name of your friend
        # or the name of a group
        target = f'"{to}"'

        # Replace the below string with your own message
        string = f"{message}"

        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = self.wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()
        # inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
        inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        input_box = self.wait.until(EC.presence_of_element_located((
            By.XPATH, inp_xpath)))
        input_box.send_keys(string + Keys.ENTER)
        time.sleep(1)

    def get_whatsapp(self, sender):
        self.driver.get("https://web.whatsapp.com/")

        # Replace 'Friend's Name' with the name of your friend
        # or the name of a group
        target = f'"{sender}"'

        # Replace the below string with your own message

        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = self.wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()

        messages = self.driver.find_elements_by_xpath(
            "//span[contains(@class,'_3Whw5 selectable-text invisible-space copyable-text')]/span")

        print(
            f"------------------------------------whatsapp-thread-start-----------------------------------------------")
        i = 0
        for message in messages:
            print(f"------------------------------------message{i}-----------------------------------------------")
            print(message.text)
            i += 1
            print("")

        time.sleep(1)
        print(f"------------------------------------whatsapp-thread-end-----------------------------------------------")
