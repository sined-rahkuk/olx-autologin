import random

from selenium import webdriver
from time import sleep

from creds import read_creds
from proxies import fetch_list_of_proxies

from conf import CHROME_DRIVER_PATH


def main():
    # proxies_list = fetch_list_of_proxies()

    creds_list = read_creds()
    # TODO: replace with an actual logic to let the user to choose
    account_to_use = creds_list[0]

    # driver = get_proxy_driver(None)
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.get('https://www.olx.ua/')
    driver.find_element_by_id('topLoginLink').click()
    driver.find_element_by_id('userEmail').send_keys(account_to_use['login'])
    driver.find_element_by_id('userPass').send_keys(account_to_use['password'])

    # Explicit wait, just in case
    sleep(1)
    driver.find_element_by_id('se_userLogin').click()
    driver.get('https://www.olx.ua/myaccount/answers/')

    while True:
        pass


def get_proxy_driver(proxies_list):
    # proxy_to_use = random.choice(proxies_list)
    proxy_to_use = '213.109.133.5:8080'

    print(proxy_to_use)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--proxy-server={proxy_to_use}')

    return webdriver.Chrome(CHROME_DRIVER_PATH, options=chrome_options)


if __name__ == "__main__":
    main()
