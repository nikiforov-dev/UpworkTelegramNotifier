from src.Config.Config import Config
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from src.DTO.JobDTO import JobDTO


class Parser:
    def __init__(self, config: Config):
        self.__config = config

    def __init_driver(self):
        options = Options()

        user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR ' \
                     '2.0.50727; InfoPath.2)'

        options.add_argument('--log-level=3')
        options.add_argument('--disable-logging')
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--window-size=1920,1080')
        options.add_argument(f"--user-agent={user_agent}")

        self.__driver = webdriver.Chrome(os.path.join(os.getcwd(), 'driver', 'chromedriver'), chrome_options=options)

    def get_jobs(self) -> list:
        try:
            self.__init_driver()

            self.__driver.get(self.__config.get_upwork_filters_url())
            elements = self.__driver.find_elements(By.CSS_SELECTOR, 'section[data-test="JobTile"]')

            jobs = []

            for element in elements:
                job_dto = JobDTO()

                title_element = element.find_element(By.CSS_SELECTOR, 'h3.job-tile-title')
                info_element = element.find_element(By.CSS_SELECTOR, 'div[data-test="JobTileFeatures"]')
                description_element = element.find_element(By.CSS_SELECTOR, 'span[data-test="job-description-text"]')

                job_dto.title = self.__get_data(title_element)
                job_dto.link = self.__get_data(title_element, By.CSS_SELECTOR, 'a', 'href')
                job_dto.amount = self.__get_data(info_element, By.CSS_SELECTOR, 'span[data-test="budget"]')
                job_dto.work_type = self.__get_data(info_element, By.CSS_SELECTOR, 'strong[data-test="job-type"]')
                job_dto.description = self.__get_data(description_element)

                jobs.append(job_dto)
        finally:
            self.__driver.quit()

        return jobs

    def __get_data(self, element: WebElement, selector_type: str = None, selector: str = None, attr: str = None) -> str:
        if selector_type is None or selector is None:
            return element.text

        found_elements = element.find_elements(selector_type, selector)

        found_element = None

        if found_elements is not None and len(found_elements) > 0:
            found_element = found_elements[0]

        if found_element is None:
            return ''

        if attr is not None:
            return found_element.get_attribute(attr) if found_element.get_attribute(attr) is not None else ''

        return found_element.text
