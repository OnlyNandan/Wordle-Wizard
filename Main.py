import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
import csv
import random
present = False
year = datetime.now().year
timeframe = 1
def get_date():
    date = datetime.now()
    current_date = date.strftime("%d")
    current_month = date.strftime("%B")
    return current_date, current_month

def first_date():
        try:
            with open("answers.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row == []:
                        pass
                    else:
                        last_date = row[0]
                date , month, year = last_date.split()
                date = str(int(date) + 1 )
                print(date, month, year)
                command = 'date -s "%s %s %s"' % (date, month, year)
    
                p = os.system('echo %s|sudo -S %s' % ("1982", command))

        except FileNotFoundError:
            print("No file found")
            pass
        except Exception as e:
            print(e)
            pass

def next_month(current_month):
    global year
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    current_month_index = months.index(current_month)
    if current_month_index == 11:
        year = int(datetime.now().year) + 1
        return months[0]

    else:
        return months[current_month_index + 1]


def set_date():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    current_date, current_month = get_date()
    sudoPassword = '1982'
    next_date = str(int(current_date) + 1)
    print(next_date, current_month)
    command = 'date -s "%s %s 2024"' % (next_date, current_month)
    
    p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
    if current_month == months[0] or current_month == months[2] or current_month == months[4] or current_month == months[6] or current_month == months[7] or current_month == months[9]:
        if current_date == '31':
            month = next_month(current_month)
            command = 'date -s "%s %s 2024"' % ("1", month)
            p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
    elif current_month == months[1]:
        if current_date == '28' or current_date == '29':
            month = next_month(current_month)
            command = 'date -s "%s %s 2024"' % ("1", month)
            p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
    elif current_month == months[3] or current_month == months[5] or current_month == months[8] or current_month == months[10]:
        if current_date == '30':
            month = next_month(current_month)
            command = 'date -s "%s %s 2024"' % ("1", month)
            p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
    elif current_month == months[11]:
        if current_date == '31':
            year = int(datetime.now().year) + 1
            command = 'date -s "%s %s %s"' % ("1", "January",year)
            p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))     

def est_play():
    global driver
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.nytimes.com/games/wordle/index.html")

    driver.maximize_window()

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/button"))
    )

    element.click()

    time.sleep(2)
    element2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="help-dialog"]/div/div/button'))
    )

    element2.click()

def get_words():
    global word
    with open("english_words_original_wordle.txt", "r") as file:
        words = file.readlines()
        word = random.choice(words)
        word = word.strip()
        if len(word) != 5:
            get_words()


def get_answers():
    global present
    for i in range(0,6):
        get_words()
        for letter in word:
            element3 = driver.find_element(By.XPATH, '/html/body')
            time.sleep(0.5)
            element3.send_keys(letter)
        element3.send_keys(Keys.ENTER)
        time.sleep(1.5)

    time.sleep(2)
    element3.send_keys(Keys.CONTROL + 'a')
    element3.send_keys(Keys.CONTROL + 'c')
    copied_text = pyperclip.paste()
    answer = copied_text.split("\n")
    answer = answer[1]
    try:
        with open("answers.csv", "r") as file:
            date = datetime.now()
            current_date = date.strftime("%d")
            current_month = date.strftime("%B")
            current_year = date.strftime("%Y")
            date = f"{current_date} {current_month} {current_year}"
            reader = csv.reader(file)
            for row in reader:
                if date in row:
                    present = True
                else:
                    pass
                
    except:
        pass
    if present != True:    
        with open("answers.csv", "a") as file:
            writer = csv.writer(file)
            now = datetime.now()
            current_date = now.strftime("%d")
            current_month = now.strftime("%B")
            current_year = now.strftime("%Y")
            date = f"{current_date} {current_month} {current_year}"
            n = [date, answer]
            writer.writerow(n)
        driver.quit()
    else:
        driver.quit()

first_date()       

for i in range(0, timeframe):
    est_play()
    get_answers()
    time.sleep(2)
    set_date()

        