from typing import Dict, List
from lxml import etree
from io import StringIO
from selenium import webdriver


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bfo_crawler.models.finance_model import OrganizationModel


def get_bfo_org_ids(inns: List[int]) -> List[Dict[str, int]]:
    """
    Selenium balance sheet scrapper from bo.nalog.ru.
    :param inns: list of inns of organisations
    :return: list of dicts with org inns
    """
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    ac = ActionChains(driver)
    parser = etree.HTMLParser()
    # driver.implicitly_wait(10)
    results = []

    for inn in inns:
        url = f"https://bo.nalog.ru/search?query={inn}&page=1"
        driver.get(url)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#search"))
        )
        ac.click().perform()
        tree = etree.parse(StringIO(driver.page_source), parser)
        orgs = tree.xpath('//*[@id="root"]/main/div/div/div[2]/div[2]/a')
        if len(orgs) > 0:
            id_link = orgs[0].attrib["href"]
            bfo_id = int("".join(list(filter(str.isdigit, id_link))))
            results.append(OrganizationModel(inn=inn, bfo_id=bfo_id).dict())
        else:
            results.append(OrganizationModel(inn=inn, bfo_id=None, results=[]).dict())
    return results
