import telebot
import telegram
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

bot_token = '6105542352:AAE0Bz8_g-ADYTTIDz9C_fc1MeLwz6Hyl0Q'
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Нажмите кнопку для запуска скрипта', reply_markup=get_keyboard())

passlinks = []
faillinks = []
@bot.message_handler(func=lambda message: True)
def handle_command(message):
    bot.send_message(message.chat.id, 'Запуск скрипта...')
    # bot.send_message(chat_id='-1001955843413', text= "Запуск скрипта")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options = options
    driver = webdriver.Chrome(options=options)
    sites = [
        "https://sales-inquiries.ae/axcapital/dubai-hills/                          ",
        "https://sales-inquiries.ae/axcapital/damac-lagoons/                        ",
        "https://sales-inquiries.ae/axcapital/one-zaabeel/                          ",
        "https://sales-inquiries.ae/axcapital/lagoon-view/                          ",
        "https://sales-inquiries.ae/axcapital/damac-hills/                          ",
        "https://sales-inquiries.ae/axcapital/madinat-jumeirah-living               ",
        "https://sales-inquiries.ae/axcapital/elysian-mansions/                     ",
        "https://sales-inquiries.ae/axcapital/arabian-ranches                       ",
        "https://sales-inquiries.ae/axcapital/st-regis-downtown/                    ",
        "https://sales-inquiries.ae/axcapital/tilal-al-ghaf/                        ",
        "https://sales-inquiries.ae/axcapital/davinci-tower/                        ",
        "https://sales-inquiries.ae/axcapital/cavalli-estates/                      ",
        "https://sales-inquiries.ae/axcapital/damac-cavalli/                        ",
        "https://sales-inquiries.ae/axcapital/one-and-only/                         ",
        "https://sales-inquiries.ae/axcapital/w-residences-cairo/                   ",
        "https://sales-inquiries.ae/axcapital/w-residences-palm-jumeirah/           ",
        "https://sales-inquiries.ae/axcapital/park-field/                           ",
        "https://sales-inquiries.ae/axcapital/w-residences-downtown/                ",
        "https://sales-inquiries.ae/axcapital/mbl-royal/                            ",
        "https://sales-inquiries.ae/axcapital/one-jbr/                              ",
        "https://sales-inquiries.ae/axcapital/safa-two/                             ",
        "https://sales-inquiries.ae/axcapital/rashid-seagate/                       ",
        "https://sales-inquiries.ae/axcapital/wasl-one/                             ",
        "https://sales-inquiries.ae/axcapital/sls-tower/                            ",
        "https://sales-inquiries.ae/axcapital/liv-residences/                       ",
        "https://sales-inquiries.ae/axcapital/sobha-hartland/                       ",
        "https://sales-inquiries.ae/axcapital/central-park/                         ",
        "https://sales-inquiries.ae/axcapital/expo-golf-villa/                      ",
        "https://sales-inquiries.ae/axcapital/ahad-residences/                      ",
        "https://sales-inquiries.ae/axcapital/lunaria-al-barari/                    ",
        "https://sales-inquiries.ae/axcapital/hawana-salalah/                       ",
        "https://sales-inquiries.ae/axcapital/blvd-heights/                         ",
        "https://sales-inquiries.ae/axcapital/maple/                                ",
        "https://sales-inquiries.ae/axcapital/talia/                                ",
        "https://sales-inquiries.ae/axcapital/opera-grand/                          ",
        "https://sales-inquiries.ae/axcapital/the-cove/                             ",
        "https://sales-inquiries.ae/axcapital/orania/                               ",
        "https://sales-inquiries.ae/axcapital/bliss-two-townhouses/                 ",
        "https://sales-inquiries.ae/axcapital/al-furjan/                            ",
        "https://sales-inquiries.ae/axcapital/marina-living/                        ",
        "https://sales-inquiries.ae/axcapital/ajman-creek-towers/                   ",
        "https://sales-inquiries.ae/axcapital/nad-al-sheba-gardens/                 ",
        "https://sales-inquiries.ae/axcapital/district-one-villas/                  ",
        "https://sales-inquiries.ae/axcapital/the-crest/                            ",
        "https://sales-inquiries.ae/axcapital/marina-shores/                        ",
        "https://sales-inquiries.ae/axcapital/waves-grande/                         ",
        "https://sales-inquiries.ae/axcapital/address-jbr/                          ",
        "https://sales-inquiries.ae/axcapital/louvre-residences/                    ",
        "https://sales-inquiries.ae/axcapital/mag-eye/                              ",
        "https://sales-inquiries.ae/axcapital/elie-saab-vie/                        ",
        "https://sales-inquiries.ae/axcapital/samana-hills/                         ",
        "https://sales-inquiries.ae/axcapital/la-violeta/                           ",
        "https://sales-inquiries.ae/axcapital/the-valley/                           ",
        "https://sales-inquiries.ae/axcapital/the-residences/                       ",
        "https://sales-inquiries.ae/axcapital/jumeirah-living-business-bay/         ",
        "https://sales-inquiries.ae/axcapital/la-vie-jbr/                           ",
        "https://sales-inquiries.ae/axcapital/aykon-heights/                        ",
        "https://sales-inquiries.ae/axcapital/deyaar-regalia/                       ",
        "https://sales-inquiries.ae/axcapital/murooj-al-furjan/                     ",
        "https://sales-inquiries.ae/axcapital/palm-tower/                           ",
        "https://sales-inquiries.ae/axcapital/urban-oasis/                          ",
        "https://sales-inquiries.ae/axcapital/shams-townhouses/                     ",
        "https://sales-inquiries.ae/axcapital/reem-townhouses/                      ",
        "https://sales-inquiries.ae/axcapital/belair/                               ",
        "https://sales-inquiries.ae/axcapital/address-villas-hillcrest/             ",
        "https://sales-inquiries.ae/axcapital/mag-318/                              ",
        "https://sales-inquiries.ae/axcapital/paragon-by-igo/                       ",
        "https://sales-inquiries.ae/axcapital/il-primo/                             ",
        "https://sales-inquiries.ae/axcapital/jebel-ali-village/                    ",
        "https://sales-inquiries.ae/axcapital/lime-gardens/                         ",
        "https://sales-inquiries.ae/axcapital/safa-one/                             ",
        "https://sales-inquiries.ae/axcapital/rukan-lofts/                          ",
        "https://sales-inquiries.ae/axcapital/the-portman/                          ",
        "https://sales-inquiries.ae/axcapital/elite-downtown-residences/            ",
        "https://sales-inquiries.ae/axcapital/gems-estates/                         ",
        "https://sales-inquiries.ae/axcapital/orla-dorchester-collection/           ",
        "https://sales-inquiries.ae/axcapital/six-senses                            ",
        "https://sales-inquiries.ae/axcapital/mjl-lamaa/                            ",
        "https://sales-inquiries.ae/axcapital/peninsula-four/                       ",
        "https://sales-inquiries.ae/axcapital/burj-royale/                          ",
        "https://sales-inquiries.ae/axcapital/mudon-al-ranim/                       ",
        "https://sales-inquiries.ae/axcapital/joy-townhouses/                       ",
        "https://sales-inquiries.ae/axcapital/anwa-omniyat/                         ",
        "https://sales-inquiries.ae/axcapital/marina-vista-tower/                   ",
        "https://sales-inquiries.ae/axcapital/ahs/                                  ",
        "https://sales-inquiries.ae/axcapital/beach-mansion/                        ",
        "https://sales-inquiries.ae/axcapital/chic-tower/                           ",
        "https://sales-inquiries.ae/axcapital/al-furjan/                            ",
        "https://sales-inquiries.ae/axcapital/fern/                                 ",
        "https://sales-inquiries.ae/axcapital/palm-beach-towers/                    ",
        "https://sales-inquiries.ae/axcapital/terraces-tower/                       ",
        "https://sales-inquiries.ae/axcapital/dorchester-residences/                ",
        "https://sales-inquiries.ae/axcapital/15-northside/                         ",
        "https://sales-inquiries.ae/axcapital/mag-city/                             ",
        "https://sales-inquiries.ae/axcapital/ellington-beach-house/                ",
        "https://sales-inquiries.ae/axcapital/rukan-maison/                         ",
        "https://sales-inquiries.ae/axcapital/luma-21/                              ",
        "https://sales-inquiries.ae/axcapital/burj-crown/                           ",
        "https://sales-inquiries.ae/axcapital/lotus/                                ",
        "https://sales-inquiries.ae/axcapital/acacia/                               ",
        "https://sales-inquiries.ae/axcapital/sunrise-bay/                          ",
        "https://sales-inquiries.ae/axcapital/keturah-reserve/                      ",
        "https://sales-inquiries.ae/axcapital/liv-lux/                              ",
        "https://sales-inquiries.ae/axcapital/bluewaters-bay/                       ",
        "https://sales-inquiries.ae/axcapital/design-quarters/                      ",
        "https://sales-inquiries.ae/axcapital/elegance-tower/                       ",
        "https://sales-inquiries.ae/axcapital/canal-heights-business-bay/           ",
        "https://sales-inquiries.ae/axcapital/elitz-residences-by-danube/           ",
        "https://sales-inquiries.ae/axcapital/keturah-resort-by-ritz-carlton/       ",
        "https://sales-inquiries.ae/axcapital/south-bay/                            ",
        "https://sales-inquiries.ae/axcapital/canal-heights-de-grisogono/      ",
        "https://sales-inquiries.ae/axcapital/senses/                               ",
        "https://sales-inquiries.ae/axcapital/canal-heights/                        ",
        "https://sales-inquiries.ae/axcapital/jomana/                               ",
        "https://sales-inquiries.ae/axcapital/caya/                                 ",
        "https://sales-inquiries.ae/axcapital/the-sanctuary/                        ",
        "https://sales-inquiries.ae/axcapital/palace-residences-north/              ",
        "https://sales-inquiries.ae/axcapital/al-jazi                               ",
        "https://sales-inquiries.ae/axcapital/sobha-one-dubai/                      ",
        "https://sales-inquiries.ae/axcapital/waves-opulence-mbr-city/              ",
        "https://sales-inquiries.ae/axcapital/cavalli-couture/                      ",
        "https://sales-inquiries.ae/axcapital/farm-gardens/                         ",
        "https://sales-inquiries.ae/axcapital/district-west/                        ",
        "https://sales-inquiries.ae/axcapital/mansio-at-the-palm/                   ",
        "https://sales-inquiries.ae/axcapital/palace-residences/                    ",
        "https://sales-inquiries.ae/axcapital/ascot-residences/                     ",
        "https://sales-inquiries.ae/axcapital/22-carats/                            ",
        "https://sales-inquiries.ae/axcapital/fairway-villas                        ",
        "https://sales-inquiries.ae/axcapital/the-grand/                            ",
        "https://sales-inquiries.ae/axcapital/mira-oasis/                           ",
        "https://sales-inquiries.ae/axcapital/blvd-cresent/                         ",
        "https://sales-inquiries.ae/axcapital/sobha-seahaven/                       ",
        "https://sales-inquiries.ae/axcapital/harbour-lights/                       ",
        "https://sales-inquiries.ae/axcapital/anya/                                 ",
        "https://sales-inquiries.ae/axcapital/residence-110/                        ",
        "https://sales-inquiries.ae/axcapital/maison-prive/                         ",
        "https://sales-inquiries.ae/axcapital/camelia/                              ",
        "https://sales-inquiries.ae/axcapital/the-ritz-carlton-residences/          ",
        "https://sales-inquiries.ae/axcapital/upper-house/                          ",
        "https://sales-inquiries.ae/axcapital/elora/                                ",
        "https://sales-inquiries.ae/axcapital/the-sustainable-city/                 ",
        "https://sales-inquiries.ae/axcapital/one-crescent/                         ",
        "https://sales-inquiries.ae/axcapital/erin/                                 ",
        "https://sales-inquiries.ae/axcapital/elvira/                               ",
        "https://sales-inquiries.ae/axcapital/damac-bay/                            ",
        "https://sales-inquiries.ae/axcapital/binghatti-creek/                      ",
        "https://sales-inquiries.ae/axcapital/park-ridge/                           ",
        "https://sales-inquiries.ae/axcapital/17-icon-bay/                          ",
        "https://sales-inquiries.ae/axcapital/keturah-reserve-at-meydan/            ",
        "https://sales-inquiries.ae/axcapital/manarat-living/                       ",
        "https://sales-inquiries.ae/axcapital/park-horizon/                         ",
        "https://sales-inquiries.ae/axcapital/keturah-resort/                       ",
        "https://sales-inquiries.ae/axcapital/manarat-living-shorts/                ",
        "https://sales-inquiries.ae/axcapital/damac-cavalli/ru/                     ",
        "https://sales-inquiries.ae/axcapital/one-and-only/ru                       ",
        "https://sales-inquiries.ae/axcapital/one-zaabeel/ru                        ",
        "https://sales-inquiries.ae/axcapital/tilal-al-ghaf/ru/                     ",
        "https://sales-inquiries.ae/axcapital/madinat-jumeirah-living/ru            ",
        "https://sales-inquiries.ae/axcapital/cavalli-estates/ru/                   ",
        "https://sales-inquiries.ae/axcapital/w-residences-cairo/ru                 ",
        "https://sales-inquiries.ae/axcapital/w-residences-palm-jumeirah/ru         ",
        "https://sales-inquiries.ae/axcapital/w-residences-downtown/ru/             ",
        "https://sales-inquiries.ae/axcapital/rashid-seagate/ru                     ",
        "https://sales-inquiries.ae/axcapital/park-field/ru                         ",
        "https://sales-inquiries.ae/axcapital/safa-two/ru                           ",
        "https://sales-inquiries.ae/axcapital/davinci-tower/ru/                     ",
        "https://sales-inquiries.ae/axcapital/liv-residences/ru                     ",
        "https://sales-inquiries.ae/axcapital/sobha-hartland/ru                     ",
        "https://sales-inquiries.ae/axcapital/the-crest/ru/                         ",
        "https://sales-inquiries.ae/axcapital/damac-lagoons/ru/                     ",
        "https://sales-inquiries.ae/axcapital/st-regis-downtown/ru                  ",
        "https://sales-inquiries.ae/axcapital/arabian-ranches/ru/                   ",
        "https://sales-inquiries.ae/axcapital/district-one-villas/ru                ",
        "https://sales-inquiries.ae/axcapital/lagoon-view/ru/                       ",
        "https://sales-inquiries.ae/axcapital/ahad-residences/ru                    ",
        "https://sales-inquiries.ae/axcapital/address-jbr/ru                        ",
        "https://sales-inquiries.ae/axcapital/louvre-residences/ru                  ",
        "https://sales-inquiries.ae/axcapital/mag-eye/ru                            ",
        "https://sales-inquiries.ae/axcapital/expo-golf-villa/ru                    ",
        "https://sales-inquiries.ae/axcapital/central-park/ru                       ",
        "https://sales-inquiries.ae/axcapital/marina-shores/ru                      ",
        "https://sales-inquiries.ae/axcapital/waves-grande/ru                       ",
        "https://sales-inquiries.ae/axcapital/la-violeta/ru                         ",
        "https://sales-inquiries.ae/axcapital/the-valley/ru                         ",
        "https://sales-inquiries.ae/axcapital/elie-saab-vie/ru                      ",
        "https://sales-inquiries.ae/axcapital/samana-hills/ru                       ",
        "https://sales-inquiries.ae/axcapital/jumeirah-living-business-bay/ru       ",
        "https://sales-inquiries.ae/axcapital/la-vie-jbr/ru                         ",
        "https://sales-inquiries.ae/axcapital/aykon-heights/ru                      ",
        "https://sales-inquiries.ae/axcapital/one-jbr/ru                            ",
        "https://sales-inquiries.ae/axcapital/deyaar-regalia/ru/                    ",
        "https://sales-inquiries.ae/axcapital/wasl-one/ru                           ",
        "https://sales-inquiries.ae/axcapital/murooj-al-furjan/ru                   ",
        "https://sales-inquiries.ae/axcapital/ava-at-palm-jumeirah/ru/              ",
        "https://sales-inquiries.ae/axcapital/lunaria-al-barari/ru                  ",
        "https://sales-inquiries.ae/axcapital/the-residences/ru/                    ",
        "https://sales-inquiries.ae/axcapital/shams-townhouses/ru                   ",
        "https://sales-inquiries.ae/axcapital/reem-townhouses/ru                    ",
        "https://sales-inquiries.ae/axcapital/belair/ru                             ",
        "https://sales-inquiries.ae/axcapital/address-villas-hillcrest/ru           ",
        "https://sales-inquiries.ae/axcapital/palm-tower/ru                         ",
        "https://sales-inquiries.ae/axcapital/paragon-by-igo/ru                     ",
        "https://sales-inquiries.ae/axcapital/jebel-ali-village/ru                  ",
        "https://sales-inquiries.ae/axcapital/lime-gardens/ru/                      ",
        "https://sales-inquiries.ae/axcapital/il-primo/ru                           ",
        "https://sales-inquiries.ae/axcapital/rukan-maison/ru/                      ",
        "https://sales-inquiries.ae/axcapital/rukan-lofts/ru                        ",
        # "https://sales-inquiries.ae/axcapital/the-portman/ru                        ",
        "https://sales-inquiries.ae/axcapital/seven-palm-residences/ru/             ",
        "https://sales-inquiries.ae/axcapital/mag-318/ru                            ",
        "https://sales-inquiries.ae/axcapital/burj-royale/ru                        ",
        "https://sales-inquiries.ae/axcapital/mudon-al-ranim/ru                     ",
        "https://sales-inquiries.ae/axcapital/joy-townhouses/ru                     ",
        "https://sales-inquiries.ae/axcapital/safa-one/ru                           ",
        "https://sales-inquiries.ae/axcapital/anwa-omniyat/ru/                      ",
        "https://sales-inquiries.ae/axcapital/marina-vista-tower/ru/                ",
        "https://sales-inquiries.ae/axcapital/the-cove/ru                           ",
        "https://sales-inquiries.ae/axcapital/orania/ru                             ",
        "https://sales-inquiries.ae/axcapital/blvd-heights/ru                       ",
        "https://sales-inquiries.ae/axcapital/ellington-beach-house/ru              ",
        "https://sales-inquiries.ae/axcapital/mjl-lamaa/ru                          ",
        "https://sales-inquiries.ae/axcapital/maple/ru                              ",
        "https://sales-inquiries.ae/axcapital/talia/ru                              ",
        "https://sales-inquiries.ae/axcapital/opera-grand/ru                        ",
        "https://sales-inquiries.ae/axcapital/bliss-two-townhouses/ru               ",
        "https://sales-inquiries.ae/axcapital/al-furjan/ru                          ",
        "https://sales-inquiries.ae/axcapital/beach-mansion/ru                      ",
        "https://sales-inquiries.ae/axcapital/burj-crown/ru                         ",
        "https://sales-inquiries.ae/axcapital/upper-house/ru                        ",
        "https://sales-inquiries.ae/axcapital/chic-tower/ru                         ",
        "https://sales-inquiries.ae/axcapital/lotus/ru                              ",
        "https://sales-inquiries.ae/axcapital/elora/ru                              ",
        "https://sales-inquiries.ae/axcapital/fern/ru                               ",
        "https://sales-inquiries.ae/axcapital/the-sustainable-city/ru               ",
        "https://sales-inquiries.ae/axcapital/ahs/ru                                ",
        "https://sales-inquiries.ae/axcapital/acacia/ru                             ",
        "https://sales-inquiries.ae/axcapital/one-crescent/ru                       ",
        "https://sales-inquiries.ae/axcapital/sunrise-bay/ru                        ",
        "https://sales-inquiries.ae/axcapital/erin/ru                               ",
        "https://sales-inquiries.ae/axcapital/hawana-salalah/ru                     ",
        "https://sales-inquiries.ae/axcapital/elvira/ru                             ",
        "https://sales-inquiries.ae/axcapital/terraces-tower/ru                     ",
        "https://sales-inquiries.ae/axcapital/marina-living/ru                      ",
        "https://sales-inquiries.ae/axcapital/binghatti-creek/ru                    ",
        "https://sales-inquiries.ae/axcapital/park-ridge/ru                         ",
        "https://sales-inquiries.ae/axcapital/liv-lux/ru                            ",
        "https://sales-inquiries.ae/axcapital/17-icon-bay/ru                        ",
        "https://sales-inquiries.ae/axcapital/bluewaters-bay/ru                     ",
        "https://sales-inquiries.ae/axcapital/keturah-reserve-at-meydan/ru          ",
        "https://sales-inquiries.ae/axcapital/elegance-tower/ru                     ",
        "https://sales-inquiries.ae/axcapital/elitz-residences-by-danube/ru         ",
        "https://sales-inquiries.ae/axcapital/manarat-living/ru                     ",
        "https://sales-inquiries.ae/axcapital/al-jazi/ru                            ",
        "https://sales-inquiries.ae/axcapital/sobha-one-dubai/ru                    ",
        "https://sales-inquiries.ae/axcapital/waves-opulence-mbr-city/ru            ",
        "https://sales-inquiries.ae/axcapital/cavalli-couture/ru                    ",
        "https://sales-inquiries.ae/axcapital/farm-gardens/ru                       ",
        "https://sales-inquiries.ae/axcapital/mansio-at-the-palm/ru                 ",
        "https://sales-inquiries.ae/axcapital/the-grand/ru                          ",
        "https://sales-inquiries.ae/axcapital/ascot-residences/ru                   ",
        "https://sales-inquiries.ae/axcapital/22-carats/ru                          ",
        "https://sales-inquiries.ae/axcapital/the-ritz-carlton-residences/ru        ",
        "https://sales-inquiries.ae/axcapital/fairway-villas/ru                     ",
        "https://sales-inquiries.ae/axcapital/blvd-cresent/ru                       ",
        "https://sales-inquiries.ae/axcapital/camelia/ru                            ",
        "https://sales-inquiries.ae/axcapital/harbour-lights/ru                     "
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
                                print(f'Ошибка при обработке сайта {site}: {str(e)}')

                                continue

    # bot.send_message(chat_id='-1001955843413', text="Скрипт выполнен")
    driver.quit()
    bot.send_message(message.chat.id, 'Скрипт выполнен')




def get_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(telebot.types.KeyboardButton('Запустить скрипт'))
    return keyboard


if __name__ == '__main__':
    bot.polling(none_stop=True)
