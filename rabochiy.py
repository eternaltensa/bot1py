
import telebot
import telegram
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

bot_token = 'telegram bot token'
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Type', reply_markup=get_keyboard())

passlinks = []
faillinks = []
@bot.message_handler(func=lambda message: True)
def handle_command(message):
    bot.send_message(message.chat.id, 'Script started')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options = options
    driver = webdriver.Chrome(options=options)
    sites = [

             ]

    for site in sites:
        driver.get(site)
        time.sleep(7)

        try:
            call_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Call') or contains(text(), 'Позвонить')     or contains(text(), 'Главная')]")
        except:
             try:
                call_button2 = driver.find_element(By.XPATH, "//*[contains(text(), 'Показать') or contains(text(), 'Show')]")
             except:
                 try:
                    call_button3 = driver.find_element(By.XPATH,
                                               "//*[contains(text(), 'ПОКАЗАТЬ НОМЕР') or contains(text(), 'show number')]")
                 except:
                    try:
                        call_button4 = driver.find_element(By.XPATH,
                                               "//*[contains(text(), 'About') or contains(text(), 'SHOW')]")
                    except:
                     try:
                        call_button5 = driver.find_element(By.XPATH,
                                               "//*[contains(text(), 'WHATSAPP') or contains(text(), 'Whatsapp')]")
                     except:
                        try:
                            call_button5 = driver.find_element(By.XPATH,
                                               "//*[contains(text(), 'Главная') ]")
                        except:
                         try:
                                call_button5 = driver.find_element(By.XPATH,
                                                                   "//*[contains(text(), 'Отправить') ]")


                         except:
                            try:
                                print("Кнопка 'Call' или 'Позвонить' не найдена на странице." + " "+ site)
                                bot.send_message(message.chat.id, site + " "+ "FAIL")
                                bot.send_message(chat_id='-1001955843413', text= site + " "+ "FAIL")
                                faillinks.append(site)
                            except Exception as e:
                                print('Ошибка при обработке сайта' + site)

                                continue

    driver.quit()
    bot.send_message(message.chat.id, 'Скрипт выполнен')




def get_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(telebot.types.KeyboardButton('Запустить скрипт'))
    return keyboard


if __name__ == '__main__':
    bot.polling(none_stop=True)
