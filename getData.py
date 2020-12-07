import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH_DRIVER = "C://Users//Dymytry//Desktop//GDL//chromedriver.exe"

class getCards:
    def getLigaP():
        driver = webdriver.Chrome(executable_path=PATH_DRIVER)
        driver.get("https://www.ligapokemon.com.br")

        id_textbox = "query"
        in_textbox = driver.find_element_by_id(id_textbox)
        in_textbox.send_keys(Keys.ENTER)
        time.sleep(5)

        xpath_table = "/html/body/div[1]/div[2]/div/div[3]/div[4]/div/table"

        try:
            element = WebDriverWait(driver,1000).until(EC.presence_of_element_located((By.XPATH,xpath_table)))
        finally:
            xpath_tbody = "/html/body/div[1]/div[2]/div/div[3]/div[4]/div/table/tbody/tr"
            in_tbody = driver.find_elements_by_xpath(xpath_tbody)
            # print(in_tbody)
            count = 1
            for x in in_tbody:
                # /html/body/div[1]/div[2]/div/div[3]/div[4]/div/table/tbody/tr[1]
                in_tr = x
                for y in range(1,4):
                    xpath_td = "/html/body/div[1]/div[2]/div/div[3]/div[4]/div/table/tbody/tr["+str(count)+"]/td["+str(y)+"]"
                    in_td = driver.find_element_by_xpath(xpath_td)
                    if y == 2:
                        xpath_tda = "/html/body/div[1]/div[2]/div/div[3]/div[4]/div/table/tbody/tr["+str(count)+"]/td["+str(y)+"]/p/a"
                        in_tda = driver.find_element_by_xpath(xpath_tda).text
                        print(str(in_tda))
                    else:
                        xpath_tda = "/html/body/div[1]/div[2]/div/div[3]/div[4]/div/table/tbody/tr["+str(count)+"]/td["+str(y)+"]/a/img"
                        in_tda = driver.find_element_by_xpath(xpath_tda)
                        print(str(in_tda.get_property("title")))
                count += 1



teste = getCards
teste.getLigaP()