from selenium import webdriver

from conf import CHROME_DRIVER_PATH

PROXYLIST_PAGE = 'http://spys.one/free-proxy-list/UA/'

# Returns a list of proxies addresses from free-proxy.cz in format ip_addr:port


def fetch_list_of_proxies():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.headless = True
    driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=chrome_options)
    driver.get(PROXYLIST_PAGE)

    driver.execute_script(
        "document.getElementById('xpp').value=4;\
         document.getElementById('xf1').value=1;\
         document.getElementById('xf5').value=1;\
         document.getElementById('xf5').form.submit()")

    return []
    # driver.find_element_by_id('clickexport').click()
    # text = driver.find_element_by_id('zkzk').text
    # entries = [entry for entry in text.split('\n')]

    # return entries


if __name__ == "__main__":
    proxies = fetch_list_of_proxies()
    print('length: ' + str(len(proxies)))
    print(proxies)

    while True:
        pass
