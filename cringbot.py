import telebot 
from telebot import types 
import random
token='6303097248:AAHtokl6JP75yXugkWMnj5m-P2lhr6jfFOg'

bot=telebot.TeleBot("6303097248:AAHtokl6JP75yXugkWMnj5m-P2lhr6jfFOg")

images = ['1.webp', '2.webp', '3.webp', '4.webp']
maus = ['1.webp', '2.webp', '3.webp', '4.webp', '5.webp', '6.webp', '7.webp', '8.webp', '9.webp']
pops = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg'] 


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Поздороваться')
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот, созданный в развлекательных целях".format(message.from_user), reply_markup=markup)	

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
   if message.text == 'Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Открытка с добрым утром')
        btn2 = types.KeyboardButton('Подкаты на все случаи жизни')
        btn3 = types.KeyboardButton('Отсчёт до дня смерти')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Выберите интересующий вас запрос', reply_markup=markup) #ответ бота


   elif message.text == 'Открытка с добрым утром':
    bot.send_message(message.from_user.id, 'С добрым утром!', parse_mode='Markdown')
    bot.send_photo(message.from_user.id,open('C:/Users/admin/Desktop/bot/' + random.choice(images),'rb'))


   elif message.text == 'Подкаты на все случаи жизни':
    bot.send_message(message.from_user.id, 'Подкаты на все случаи жизни', parse_mode='Markdown') 
    bot.send_photo(message.from_user.id,open('C:/Users/admin/Desktop/pops/' + random.choice(pops),'rb'))

   elif message.text == 'Отсчёт до дня смерти':
    bot.send_message(message.from_user.id, 'Отсчёт до дня смерти', parse_mode='Markdown')
    bot.send_photo(message.from_user.id, open('C:/Users/admin/Desktop/lox/' + random.choice(maus),'rb'))

if __name__ =="__main__":
   bot.polling(none_stop=True, interval=0)