from src.Config.Config import Config
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from src.DTO.JobDTO import JobDTO

class Parser:
    def __init__(self, config: Config):
        self.__config = config

        options = Options()

        user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR ' \
                     '2.0.50727; InfoPath.2)'

        print(user_agent)

        options.add_argument('--log-level=3')
        options.add_argument('--disable-logging')
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--window-size=1920,1080')
        options.add_argument(f"--user-agent={user_agent}")

        self.__driver = webdriver.Chrome(os.path.join(os.getcwd(), 'driver', 'chromedriver'), chrome_options=options, )

    def get_jobs(self) -> list:
        self.__driver.get(self.__config.get_upwork_filters_url())
        elements = self.__driver.find_elements(By.CSS_SELECTOR, 'section[data-test="JobTile"]')

        jobs = []

        for element in elements:
            job_dto = JobDTO()

            title_element = element.find_element(By.CSS_SELECTOR, 'h3.job-tile-title')
            info_element = element.find_element(By.CSS_SELECTOR, 'div[data-test="JobTileFeatures"]')
            description_element = element.find_element(By.CSS_SELECTOR, 'span[data-test="job-description-text"]')

            job_dto.title = title_element.text
            job_dto.link = title_element.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            job_dto.amount = info_element.find_element(By.CSS_SELECTOR, 'span[data-test="budget"]').text
            job_dto.work_type = info_element.find_element(By.CSS_SELECTOR, 'strong[data-test="job-type"]').text
            job_dto.description = description_element.text

            jobs.append(job_dto)

        return jobs
