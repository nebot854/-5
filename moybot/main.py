from logic import DB_Managr
from config import *
from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telebot import types

bot = TeleBot('7689614483:AAG5n7-NSiWPNh3XMYKIwF1aCXqKz_ljPho')
hideBoard = types.ReplyKeyboardRemove() 

cancel_button = "Отмена 🚫"
def cansel(message):
    bot.send_message(message.chat.id, "Чтобы посмотреть команды, используй - /info", reply_markup=hideBoard)
  
def no_projects(message):
    bot.send_message(message.chat.id, 'У вас пока что нету трат что бы их записать используйте команда /Finans')

def gen_inline_markup(rows):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for row in rows:
        markup.add(InlineKeyboardButton(row, callback_data=row))
    return markup

def gen_markup(rows):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 1
    for row in rows:
        markup.add(KeyboardButton(row))
    markup.add(KeyboardButton(cancel_button))
    return markup
attributes_of_projects = {'ваша покупка' : ["Что вы купили", "pokypka"],
                          "траты на покупку" : ["Ведите сумму", "tratu"],
                          "Статус" : ["Выберите новый статус задачи", "status_id"]}

def info_project(message, user_id, project_name):
    info = manager.get_project_info(user_id, project_name)[0]
    skills = manager.get_project_skills(project_name)
    if not skills:
        skills = 'Навыки пока не добавлены'
    bot.send_message(message.chat.id, f"""Project name: {info[0]}
Description: {info[1]}
Link: {info[2]}
Status: {info[3]}
""")



@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Здравствуйте! Я бот который может записать ваши траты,ваш заработок. Каманда
    /info поможет лучше разобратся как и что делать. 
""")
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id,
"""
Вот команды которые могут тебе помочь:

/Finans - спрашивает что за товар записывает товар после чего спрашивается цена и после всего он записывает это в базу данных
/Statictic - показывает статистику твоих трат 
""")
@bot.message_handler(commands=['Finans'])
def addtask_command(message):
    bot.send_message(message.chat.id, "что купили?")
    bot.register_next_step_handler(message, name_project)

def name_project(message):
    name = message.text
    user_id = message.from_user.id
    data = [user_id, name]
    bot.send_message(message.chat.id, "за сколько вы купили?")
    bot.register_next_step_handler(message, link_project, data=data)

def link_project(message, data):
    data.append(message.text)
    statuses = [x[0] for x in manager.get_statuses()] 
    bot.send_message(message.chat.id, "что за трата: еда, оджеда, ипотека кредит или курпная покупка", reply_markup=gen_markup(statuses))
    bot.register_next_step_handler(message, callback_project, data=data, statuses=statuses)

def callback_project(message, data, statuses):
    status = message.text
    if message.text == cancel_button:
        cansel(message)
        return
    if status not in statuses:
        bot.send_message(message.chat.id, "Вы выбрал статус не из списка, попробуй еще раз!)", reply_markup=gen_markup(statuses))
        bot.register_next_step_handler(message, callback_project, data=data, statuses=statuses)
        return
    status_id = manager.get_status_id(status)
    data.append(status_id)
    manager.insert_project([tuple(data)])
    bot.send_message(message.chat.id, "Ваша покупка сохранена")

@bot.message_handler(commands=['Statictic'])
def get_projects(message):
    user_id = message.from_user.id
    projects = manager.get_projects(user_id)
    if projects:
        text = "\n".join([f"Project name:{x[2]} \nLink:{x[4]}\n" for x in projects])
        bot.send_message(message.chat.id, text, reply_markup=gen_inline_markup([x[2] for x in projects]))
    else:
        no_projects(message)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    eat = call.data
    info_project(call.message, call.from_user.id, eat)   

if __name__ == '__main__':
    manager = DB_Managr(DATABASE)
    bot.infinity_polling()