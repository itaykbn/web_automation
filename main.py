import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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

with open("credentials.json", "r", encoding="utf8") as f:
    data = json.load(f)
    whatsapp_contacts = data["contacts"]["whatsapp"]
    gmail_contacts = data["contacts"]["Gmail"]

GOOGLE = Gmail(driver, wait)
WHATSAPP = Whatsapp(driver, wait)


def handle_gmail_client():
    global gmail_contacts
    contact = input(f"pick one of the contacts: {gmail_contacts}\n:  ")
    subject = input(f"enter message subject for {gmail_contacts[contact]}")
    message = input(f"enter message to send to {gmail_contacts[contact]}")
    GOOGLE.send_email(gmail_contacts[contact], subject, message)


def handle_whatsapp_client():
    global whatsapp_contacts
    target = input("have you come to get message or send one?(y for send / n for get")
    contact = input(f"pick one of the contacts: {whatsapp_contacts}\n:  ")
    if target.lower() == "y":
        message = input(f"enter message to send to {f'{whatsapp_contacts[contact]}'}")
        WHATSAPP.send_whatsapp(f'{whatsapp_contacts[contact]}', message)
    elif target.lower() == "n":
        WHATSAPP.get_whatsapp(f'{whatsapp_contacts[contact]}')


def main():
    set_up()
    handle_gmail_client()

    handle_whatsapp_client()
    handle_whatsapp_client()

    gmail_messages = GOOGLE.get_inbox()

    GOOGLE.get_inbox_shortcut(gmail_messages)
    index = input("enter message num:")
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
    driver.get("https://web.whatsapp.com/")
    print("scan please")
    x_arg = '//span[contains(@title,' + '"Dad"' + ')]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()
    driver.get("https://google.com/")


if __name__ == '__main__':
    main()
