from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException


def logs(error: str) -> None:
    """
    Запись ошибок в файл логи.
    :param error:
    :return:
    """
    with open("logs.txt", "a", encoding="UTF-8") as file_logs:
        file_logs.write(f"Возникла ошибка: {error}.\nВремя: "
                        + str(datetime.now().strftime("%d.%m.%Y %H.%M")) + "\n")


if __name__ == '__main__':

    def get_webdriver() -> int:
        while True:
            browser_number = int(
                input("Добро пожаловать в тестовый полигон!\nДоступные браузеры:\n"
                      "1 = Chrome\n2 = Firefox\nВведите цифру:\n"))
            if 1 <= browser_number <= 2:
                return browser_number
            else:
                print("Выберите Chrome или Firefox...")


    if get_webdriver() == 1:
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    try:
        driver.implicitly_wait(10)
        driver.get("https://demoqa.com")
    except WebDriverException as e:
        logs(str(e))
    try:
        driver.find_element(By.CLASS_NAME, "card-body").click()
        driver.find_element(By.ID, "item-1").click()
        driver.find_element(By.CLASS_NAME, "rct-collapse-btn").click()
        driver.find_elements(By.CLASS_NAME, "rct-collapse-btn")[3].click()
        driver.find_elements(By.CLASS_NAME, "rct-checkbox")[4].click()
    except (NoSuchElementException, TimeoutException):
        logs("Элемент не может быть найден или ")
    time.sleep(10)
    driver.quit()
    print("Работа завершена без ошибок!")
