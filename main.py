import os
import time
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

gmailId = 'itay.kbn@gmail.com'
passWord = '1t@9214927915'

chrome_options = ChromeOptions()
chrome_options.set_capability('unhandledPromptBehavior', 'accept')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
wait = WebDriverWait(driver, 600)


def get_inbox_shortcut(messages):
    i = 0
    print(f"------------------------------------inbox-email-start-----------------------------------------------")
    for message in messages:
        print(f"------------------------------------message{i}-----------------------------------------------")
        print(message.text)
        i += 1
        print("")
    print(f"------------------------------------inbox-email-end-----------------------------------------------")


def get_gmail_msg_thread(index, messages):
    global driver, wait

    messages[index].click()
    threadXPath = "//div[contains(@role,'listitem')]"
    chat = wait.until(EC.presence_of_all_elements_located((
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


def do_actions():
    global driver

    # set_up()

    # send_email("itay.kbn@gmail.com", "testing auto email from python in parallel with whatsapp - finally","hello from python, don't worry about the warning message i'm doing that to bypass the google block ")

    # send_whatsapp("לבד,בדד,גלמוד😭", "hello from python- finally")

    # get_whatsapp("לבד,בדד,גלמוד😭")
    get_whatsapp("יא פיזיקה עם דודי")

    # gmail_messages = get_inbox()

    # get_inbox_shortcut(gmail_messages)
    # index = input("enter mail num")
    # get_gmail_msg_thread(int(index), gmail_messages)


def set_up():
    # bypass google automation block

    driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
    stack_overflow_login = driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]')
    stack_overflow_login.click()

    # authenticate with google
    auth_google()
    driver.get(
        "https://accounts.google.com/AccountChooser/signinchooser?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser")
    auth_google()


def auth_google():
    global driver
    login_box = driver.find_element_by_xpath('//*[@id ="identifierId"]')
    login_box.send_keys(gmailId)

    next_button = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
    next_button[0].click()

    driver.implicitly_wait(4)

    pass_word_box = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    pass_word_box.send_keys(passWord)
    "VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc"
    driver.implicitly_wait(4)

    next_button = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
    next_button[0].click()


def send_email(to, subject, message):
    global driver, wait

    driver.get(
        "https://accounts.google.com/AccountChooser/signinchooser?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser")

    driver.implicitly_wait(4)

    compose = driver.find_element_by_xpath("//div[contains(@class,'T-I T-I-KE L3')]")
    compose.click()

    to_field = driver.find_element_by_xpath("//textarea[contains(@name,'to')]")
    to_field.send_keys(to)

    subject_filed = driver.find_element_by_xpath("//input[contains(@name,'subjectbox')]")
    subject_filed.send_keys(subject)

    message_field = driver.find_element_by_xpath("//div[contains(@aria-label,'Message Body')]")
    message_field.send_keys(message)

    send_button = driver.find_element_by_xpath("//div[contains(@class,'T-I J-J5-Ji aoO v7 T-I-atl L3')]")
    send_button.click()
    wait.until(EC.presence_of_element_located((
        By.XPATH, "//span[contains(@class,'bAq')]")))
    time.sleep(3)


def get_inbox():
    global driver, wait
    driver.get(
        "https://accounts.google.com/AccountChooser/signinchooser?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser")

    driver.implicitly_wait(4)
    msgXPath = "//tr[contains(@jscontroller,'ZdOxDb')]"
    messages = wait.until(EC.presence_of_all_elements_located((By.XPATH, msgXPath)))
    return messages


def send_whatsapp(to, message):
    global driver
    global wait
    driver.get("https://web.whatsapp.com/")

    # Replace 'Friend's Name' with the name of your friend
    # or the name of a group
    target = f'"{to}"'

    # Replace the below string with your own message
    string = f"{message}"

    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()
    # inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
    inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)


def get_whatsapp(sender):
    global driver
    global wait
    driver.get("https://web.whatsapp.com/")

    # Replace 'Friend's Name' with the name of your friend
    # or the name of a group
    target = f'"{sender}"'

    # Replace the below string with your own message

    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()

    messages = driver.find_elements_by_xpath(
        "//span[contains(@class,'_3Whw5 selectable-text invisible-space copyable-text')]/span")

    print(f"------------------------------------whatsapp-thread-start-----------------------------------------------")
    i = 0
    for message in messages:
        print(f"------------------------------------message{i}-----------------------------------------------")
        print(message.text)
        i += 1
        print("")

    time.sleep(1)
    print(f"------------------------------------whatsapp-thread-end-----------------------------------------------")


def main():
    do_actions()


if __name__ == '__main__':
    main()
