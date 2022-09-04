import telebot
import random

token = '_'
bot = telebot.TeleBot(token)

HELP = """
/help - вывести список команд.
/add - добавить на определённю дату (дд.мм.гггг/сегодня) задачу в список.
/show - напечатать задачи на определенную дату.
/exit - выход
/random - добавляет рандомную задачу на сегодня"""

tasks = {}
random_task = ['Посмотреть обучающий курс', 'Сходить на прогулку', 'Потренить', 'Почитать книгу', 'Покушать']

def adding(date, task):
    date = date.lower()
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]

@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    if len(task) < 3:
        bot.send_message(message.chat.id, f'Задача из 2 и менее символов - это не задача!')
    else:
        adding(date, task)
        bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEEVX1iRd95Z_GMKn4unwjxoBVoHi07qQACxwoAAvxlAUrfEkMNGcJAQSME')

@bot.message_handler(commands=['random'])
def random_add(message):
    date = 'сегодня'
    task = random.choice(random_task)
    adding(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')

@bot.message_handler(commands=['show'])
def show(message):
    date = message.text.split()[1].lower()
    if date in tasks:
        text = ''
        for task in tasks[date]:
            text += f'[ ] {task}\n'
    else:
        text = 'Задач на эту дату нет'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(content_types=['text'])
def echo(message):
    word = "Мария"
    if word in message.text:
        bot.send_message(message.chat.id, "Ба! Знакомые все лица!")
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
