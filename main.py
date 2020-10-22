import json

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from Gmail import Gmail
from Whatsapp import Whatsapp

chrome_options = ChromeOptions()
chrome_options.set_capability('unhandledPromptBehavior', 'accept')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
wait = WebDriverWait(driver, 600)

GOOGLE = Gmail(driver, wait)
WHATSAPP = Whatsapp(driver, wait)


def main():
    global driver
    with open("credentials.json", "r",encoding="utf8") as f:
        data = json.load(f)
        whatsapp_contacts = data["contacts"]["whatsapp"]
        gmail_contacts = data["contacts"]["Gmail"]

    set_up()

    GOOGLE.send_email(gmail_contacts["Me"], "testing auto email from python in parallel with whatsapp - finally",
                      "hello from python, don't worry about the warning message i'm doing that to bypass the google block ")

    WHATSAPP.send_whatsapp(whatsapp_contacts["Me"], "hello from python- finally")

    WHATSAPP.get_whatsapp(whatsapp_contacts["Me"])
    WHATSAPP.get_whatsapp(whatsapp_contacts["Physics"])

    gmail_messages = GOOGLE.get_inbox()

    GOOGLE.get_inbox_shortcut(gmail_messages)
    index = input("enter mail num")
    GOOGLE.get_gmail_msg_thread(int(index), gmail_messages)


def set_up():
    # bypass google automation block

    driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
    stack_overflow_login = driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]')
    stack_overflow_login.click()

    # authenticate with google
    GOOGLE.auth_google()
    driver.get(
        "https://accounts.google.com/AccountChooser/signinchooser?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser")
    GOOGLE.auth_google()


if __name__ == '__main__':
    main()
