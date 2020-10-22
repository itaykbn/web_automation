from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import io


class Gmail:
    def __init__(self, driver, wait):
        with open("credentials.json", "r", encoding="utf8") as f:
            data = json.load(f)
            self.gmailId = data["credentials"]["account"]
            self.password = data["credentials"]["password"]
        self.driver = driver
        self.wait = wait

    @staticmethod
    def get_inbox_shortcut(messages):
        i = 0
        print(f"------------------------------------inbox-email-start-----------------------------------------------")
        for message in messages:
            print(f"------------------------------------message{i}-----------------------------------------------")
            print(message.text)
            i += 1
            print("")
        print(f"------------------------------------inbox-email-end-----------------------------------------------")

    def get_gmail_msg_thread(self, index, messages):
        messages[index].click()
        threadXPath = "//div[contains(@role,'listitem')]"
        chat = self.wait.until(EC.presence_of_all_elements_located((
            By.XPATH, threadXPath)))
        i = 0
        print(f"------------------------------------email-thread-start-----------------------------------------------")
        for message in chat:
            print(f"------------------------------------message{i}-----------------------------------------------")
            print(message.text)
            print("")
            print("")
            i += 1
        print(f"------------------------------------inbox-thread-end-----------------------------------------------")

    def send_email(self, to, subject, message):
        self.driver.get(
            "https://accounts.google.com/AccountChooser/signinchooser?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser")

        self.driver.implicitly_wait(4)

        compose = self.driver.find_element_by_xpath("//div[contains(@class,'T-I T-I-KE L3')]")
        compose.click()

        to_field = self.driver.find_element_by_xpath("//textarea[contains(@name,'to')]")
        to_field.send_keys(to)

        subject_filed = self.driver.find_element_by_xpath("//input[contains(@name,'subjectbox')]")
        subject_filed.send_keys(subject)

        message_field = self.driver.find_element_by_xpath("//div[contains(@aria-label,'Message Body')]")
        message_field.send_keys(message)

        send_button = self.driver.find_element_by_xpath("//div[contains(@class,'T-I J-J5-Ji aoO v7 T-I-atl L3')]")
        send_button.click()
        self.wait.until(EC.presence_of_element_located((
            By.XPATH, "//span[contains(@class,'bAq')]")))
        time.sleep(3)

    def get_inbox(self):
        self.driver.get(
            "https://accounts.google.com/AccountChooser/signinchooser?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser")

        self.driver.implicitly_wait(4)
        msgXPath = "//tr[contains(@jscontroller,'ZdOxDb')]"
        messages = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, msgXPath)))
        return messages

    def auth_google(self):
        login_box = self.driver.find_element_by_xpath('//*[@id ="identifierId"]')
        login_box.send_keys(self.gmailId)

        next_button = self.driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
        next_button[0].click()

        self.driver.implicitly_wait(4)

        pass_word_box = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pass_word_box.send_keys(self.password)
        "VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc"
        self.driver.implicitly_wait(4)

        next_button = self.driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
        next_button[0].click()
