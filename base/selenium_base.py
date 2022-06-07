from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20, 0.2)

    def get_type_of_locator(self, find_by: str) -> dict:
        """Return type of locator for some element on page"""
        find_by = find_by.lower()
        locator_types = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'class_name': By.CLASS_NAME,
            'id': By.ID,
            'link_text': By.LINK_TEXT,
            'name': By.NAME,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME
        }
        return locator_types[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Waiting visibility of element and return WebElement"""
        return self.wait.until(ec.visibility_of_element_located((self.get_type_of_locator(find_by), locator)),
                               locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Waiting on element and return WebElement if it is present on DOM"""
        return self.wait.until(ec.presence_of_element_located((self.get_type_of_locator(find_by), locator)),
                               locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Wait on element until it disappears """
        return self.wait.until(ec.invisibility_of_element_located((self.get_type_of_locator(find_by), locator)),
                               locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        """Waiting on elements and return WebElements if they are visible"""
        return self.wait.until(ec.visibility_of_all_elements_located((self.get_type_of_locator(find_by), locator)),
                               locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        """Waiting on elements and return WebElements if they are present on DOM"""
        return self.wait.until(ec.presence_of_all_elements_located((self.get_type_of_locator(find_by), locator)),
                               locator_name)

    def get_text_from_web_elements(self, elements: List[WebElement]) -> List[str]:
        """The input should be a list of WebElements, where we read text from each element and Return a List[String]"""
        return [element.text for element in elements]

    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        """The input should we a list of WebElements, from which we return a single WebElement found by it's name"""
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

