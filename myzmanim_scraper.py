import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDWait
from selenium.common.exceptions import TimeoutException


class myZmanimScraper:
        def __init__(self):
            self.driver = None
            try:
                self.options = Options()
                self.options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
                self.options.add_experimental_option("useAutomationExtension", False)
                self.options.add_argument("--headless")


            except Exception as e:
                print("Error setting up options")

            try:
                self.driver = webdriver.Chrome(options=self.options)
                
            except Exception as e:
                print("Error creating webdriver instance")

            self.url = 'https://www.myzmanim.com/search.aspx'
            self.driver.get("https://www.myzmanim.com/search.aspx")
        
        def get_times(self) -> dict:
            time.sleep(3)
            try:
                  search_box_xpath = '//*[@id="txtSearch"]'
                  search_box = WDWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, search_box_xpath))
                )
                  search_box.click()
                  zip_code = '48104'
                  for num in zip_code:
                       search_box.send_keys(num)
                       time.sleep(0.1)
                  search_box.send_keys(Keys.ENTER)
                  time.sleep(3)
            except TimeoutException:
                  print("Error: could not type in zip coee")
                  return
            try:
                 ann_arbor_button_xpath = '//*[@id="Form1"]/table[1]/tbody/tr/td[2]'
                 ann_arbor_button = WDWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, ann_arbor_button_xpath)))
                 ann_arbor_button.click()
            except TimeoutException:
                  print("Error: could not type in zip coee")
                  return    
            try:
                 shkiyah_time_xpath = '//*[@id="Form1"]/center/table[6]/tbody/tr/td[2]/div[1]/table/tbody/tr[26]/td[2]/span[1]'
                 shkiyah_time_element = self.driver.find_element(By.XPATH,shkiyah_time_xpath)
                 shkiyah_time = shkiyah_time_element.text
                 plag_hamincha_xpath = '//*[@id="Form1"]/center/table[6]/tbody/tr/td[2]/div[1]/table/tbody/tr[23]/td[2]/span[1]'
                 plag_time_element = self.driver.find_element(By.XPATH,plag_hamincha_xpath)
                 plag_time = plag_time_element.text
                 
                 times = {}
                 times["shkiyah"] = shkiyah_time
                 times["plag"] = plag_time
                 return times
            except Exception:
                 print("Error: could not find times")
                 return
                
                 
def main():
     my_zmanim = myZmanimScraper()
     zmanim = my_zmanim.get_times()
     print(zmanim)


    
if __name__ == '__main__':
     main()