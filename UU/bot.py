import telebot

from logic import FusionBrainAPI


fusion_brain_api = FusionBrainAPI('https://api-key.fusionbrain.ai/', '001988684F3789181C1564F4F32A5805', 'FA6858C8C9C94D327F72BD7BA504F04F')
bot = telebot.TeleBot('7689614483:AAG5n7-NSiWPNh3XMYKIwF1aCXqKz_ljPho')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который может генерировать картинки. Используй команду /help для просмотра остальных команд.")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Доступные команды:/generacion - по запросу генерирует фото.")

@bot.message_handler(commands=['generacion'])
def handle_show_city(message):
    bot.send_message(message.chat.id, "Какое фото мне сгенерировать? Напишите ваш запрос.")
    
bot.polling()
