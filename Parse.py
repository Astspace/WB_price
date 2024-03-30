from selenium import webdriver
import time
from typing import TypedDict
from typing import TypeAlias


Rub: TypeAlias = int

class Dataitem(TypedDict):
    id_item: int
    name_item: str
    price_item: Rub
    rating_item: float | str
    core_item: int | str

class ParseWB():
    def __init__(self, url):
        self.url = url

    def _add_options_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
        options.add_argument("headless")
        options.add_argument("--disable-blink-features=AutomationControlled")
        return options

    def _create_driver(self):
        options = self._add_options_driver()
        driver = webdriver.Chrome(options=options)
        return driver

    def _get_html_data(self):
        driver = self._create_driver()
        try:
            driver.get(url=self.url)
            time.sleep(5)
        except Exception as ex:
            print("Не удалось получить html-данные web-страницы, ошибка:")
            print(ex)
            exit(1)
        finally:
            driver.quit()
        return driver.page_source

    def _create_index_html(self):
        page_source = self._get_html_data()
        with open("index.html", "w", encoding="utf-8") as file:
            file.write(page_source)

    def _create_dict_item_info(self):
        item_info = {}
        with open("index.html", encoding="utf-8") as file:
            src = file.read()