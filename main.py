import time
import parserr
import db_driver
import parser_onliner
import os.path

if not os.path.exists('db_main.db'):
    db_driver.db_create()
try:
    parserr.Parser().db_filling()
except:
    print('clone')
time.sleep(120)
while True:
    parser_onliner.search()
#####
#Для работы нужно запустить main.py and Bot_tg.py подождать 120 секунд and ->>>>tg bot--->>> @Aladin_mf_bot
# Для проверки нужно отсортировать на онлайнере квартиры  по параметру (новые)