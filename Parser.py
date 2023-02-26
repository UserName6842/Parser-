from selenium import webdriver
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import csv
import sqlite3


with open('cadnums.csv') as f:
    numbers = {line[0]:line[1:] for line in csv.reader(f)}

    for number, el in numbers.items():
        print(number)

        ### Селениум. ###
        useragent = UserAgent()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'user-agent={useragent.random}')

        browser = webdriver.Chrome(options=chrome_options)
        browser.get('https://kadbase.ru')

        text_area_xpath = '/html/body/div/div[4]/div[1]/div[1]/div/div[2]/form/div[2]/input[1]'
        browser.find_element_by_xpath(text_area_xpath).send_keys(number)  ### КАДАРСТОВЫЙ НОМЕР number. ###

        button_xpath = '/html/body/div/div[4]/div[1]/div[1]/div/div[2]/form/div[2]/input[2]'
        browser.find_element_by_xpath(button_xpath).click()

        give_url = browser.current_url
        #print(give_url)  ### УБРАТЬ. ###

        if give_url == 'https://kadbase.ru/lk/':
            while give_url == 'https://kadbase.ru/lk/':
                print('ПЛОХОЙ URL, ДАВАЙ ПО НОВОЙ!')
                print(number)
                browser.close()
                ### Селениум. ###
                useragent = UserAgent()
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument(f'user-agent={useragent.random}')

                browser = webdriver.Chrome(options=chrome_options)
                browser.get('https://kadbase.ru')

                text_area_xpath = '/html/body/div/div[4]/div[1]/div[1]/div/div[2]/form/div[2]/input[1]'
                browser.find_element_by_xpath(text_area_xpath).send_keys(number)  ### КАДАРСТОВЫЙ НОМЕР number. ###

                button_xpath = '/html/body/div/div[4]/div[1]/div[1]/div/div[2]/form/div[2]/input[2]'
                browser.find_element_by_xpath(button_xpath).click()

                give_url = browser.current_url

            if give_url != 'https://kadbase.ru/lk/':
                ### ПАРСЕР. ###
                HOST = 'https://kadbase.ru'
                URL = give_url
                HEADERS = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'user-agent': f'user-agent={useragent.random}'
                }

                ### Создание базы. ###
                db = sqlite3.connect('info.db')
                cur = db.cursor()

                cur.execute("""CREATE TABLE IF NOT EXISTS numbers (
                                        kadastr TEXT,
                                        link TEXT
                                    )""")

                db.commit()

                ### ВЕНЕСЕНИЕ В ТАБЛИЦУ ###
                cur.execute("SELECT * FROM numbers")
                cur.execute(f"INSERT INTO numbers VALUES (?, ?)", (number, give_url))
                db.commit()

                browser.close()  ### Закрывает окно после отработки скрипта. ###
        else:
            ### ПАРСЕР. ###
            HOST = 'https://kadbase.ru'
            URL = give_url
            HEADERS = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'user-agent': f'user-agent={useragent.random}'
            }


            def get_html(url, params=''):
                r = requests.get(url, headers=HEADERS, params=params)
                return r


            result1 = ''
            result2 = ''


            def get_content1(html):
                global result1
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find('div', class_='ser_bl', ).find_all('div', class_='tx_sser')
                for item in items:
                    result1 = item.get_text(strip=True)
                return result1


            def get_content2(html):
                global result2
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find('div', class_='col2_sser_2', ).find_all('div', class_='tx_sser')
                for item in items:
                    result2 = item.get_text(strip=True)
                return result2


            ### Создание базы. ###
            db = sqlite3.connect('info2.db')
            cur = db.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS numbers2 (
                        kadastr TEXT,
                        link TEXT,
                        data1 TEXT,
                        data2 TEXT
                    )""")

            db.commit()

            ### ВЕНЕСЕНИЕ В ТАБЛИЦУ ###
            cur.execute("SELECT * FROM numbers2")
            cur.execute(f"INSERT INTO numbers2 VALUES (?, ?, ?, ?)", (number, give_url, get_content1(give_url), get_content2(give_url)))
            db.commit()

            browser.close()  ### Закрывает окно после отработки скрипта. ###


from selenium import webdriver
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import csv
import sqlite3


with open('cadnums.csv') as f:
    numbers = {line[0]:line[1:] for line in csv.reader(f)}

    for number, el in numbers.items():
        print(number)

        ### Селениум. ###
        useragent = UserAgent()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'user-agent={useragent.random}')

        browser = webdriver.Chrome(options=chrome_options)
        browser.get('https://kadbase.ru')

        text_area_xpath = '/html/body/div/div[4]/div[1]/div[1]/div/div[2]/form/div[2]/input[1]'
        browser.find_element_by_xpath(text_area_xpath).send_keys(number)  ### КАДАРСТОВЫЙ НОМЕР number. ###

        button_xpath = '/html/body/div/div[4]/div[1]/div[1]/div/div[2]/form/div[2]/input[2]'
        browser.find_element_by_xpath(button_xpath).click()

        give_url = browser.current_url
        #print(give_url)  ### УБРАТЬ. ###

        if give_url == 'https://kadbase.ru/lk/':
            while give_url == 'https://kadbase.ru/lk/':
                print('ПЛОХОЙ URL, ДАВАЙ ПО НОВОЙ!')
                print(number)
                browser.close()
                ### Селениум. ###
                useragent = UserAgent()
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument(f'user-agent={useragent.random}')

                browser = webdriver.Chrome(options=chrome_options)
                browser.get('https://kadbase.ru')

                text_area_xpath = '/html/body/div/div[4]/div[1]/div[1]/div/div[2]/form/div[2]/input[1]'
                browser.find_element_by_xpath(text_area_xpath).send_keys(number)  ### КАДАРСТОВЫЙ НОМЕР number. ###

                button_xpath = '/html/body/div/div[4]/div[1]/div[1]/div/div[2]/form/div[2]/input[2]'
                browser.find_element_by_xpath(button_xpath).click()

                give_url = browser.current_url

            if give_url != 'https://kadbase.ru/lk/':
                ### ПАРСЕР. ###
                HOST = 'https://kadbase.ru'
                URL = give_url
                HEADERS = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'user-agent': f'user-agent={useragent.random}'
                }

                ### Создание базы. ###
                db = sqlite3.connect('info.db')
                cur = db.cursor()

                cur.execute("""CREATE TABLE IF NOT EXISTS numbers (
                                        kadastr TEXT,
                                        link TEXT
                                    )""")

                db.commit()

                ### ВЕНЕСЕНИЕ В ТАБЛИЦУ ###
                cur.execute("SELECT * FROM numbers")
                cur.execute(f"INSERT INTO numbers VALUES (?, ?)", (number, give_url))
                db.commit()

                browser.close()  ### Закрывает окно после отработки скрипта. ###
        else:
            ### ПАРСЕР. ###
            HOST = 'https://kadbase.ru'
            URL = give_url
            HEADERS = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'user-agent': f'user-agent={useragent.random}'
            }


            r = requests.get(url = URL, headers = HEADERS).content

            soup1 = BeautifulSoup(r, 'lxml')
            n1 = soup1.find('div', class_='ser_bl', ).find_all('div', class_='tx_sser')
            for item1 in n1:
                result1 = item1.get_text(strip=True)

            soup2 = BeautifulSoup(r, 'lxml')
            n11 = soup2.find('div', class_='col2_sser_2', ).find_all('div', class_='tx_sser')
            for item2 in n11:
                result2 = item2.get_text(strip=True)


            ### Создание базы. ###
            db = sqlite3.connect('info2.db')
            cur = db.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS numbers2 (
                        kadastr TEXT,
                        link TEXT,
                        data1 TEXT,
                        data2 TEXT
                    )""")

            db.commit()

            ### ВЕНЕСЕНИЕ В ТАБЛИЦУ ###
            cur.execute("SELECT * FROM numbers2")
            cur.execute(f"INSERT INTO numbers2 VALUES (?, ?, ?, ?)", (number, give_url, result1, result2))
            db.commit()

            browser.close()  ### Закрывает окно после отработки скрипта. ###


