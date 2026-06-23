from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    driver.get("https://gitflic.ru/")    
    cookie_user1 = {"name": "user_id","value": "1","domain": "gitflic.ru"}
    driver.add_cookie(cookie_user1)

    driver.refresh()

    driver.get("https://gitflic.ru/user/1")

    user1_url = driver.current_url

    driver.delete_all_cookies()

    cookie_user2 = {"name": "user_id","value": "2", "domain": "gitflic.ru"}

    driver.add_cookie(cookie_user2)

    driver.refresh()

    driver.get("https://gitflic.ru/user/2")

    user2_url = driver.current_url

    assert user1_url != user2_url

    driver.quit()
