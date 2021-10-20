import telebot

token = "2091923087:AAGuT_SvctjWe0KLFv3TEBrU1FUxaLNgP0Q"

bot = telebot.TeleBot(token)
helptext = """
/add - добавить задачу в список
/show - показать задачи из списка
/help - вывести помощь
/random - назначить рандомную задачу на сегодня
/showall - показать все задачи
"""

DB={}

def addtodo (date, task):
    if date in DB:
        DB[date].append(task)
    else:
        DB[date] = []
        DB[date].append(task)
#    print("Итого на дату " + date + " " + str(DB[date]))

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет, засранец! Мои команды: \n" + helptext)

@bot.message_handler(commands=['help'])
def help(message):
	bot.reply_to(message, helptext)

@bot.message_handler(commands=['add'])
def add(message):
    task = message.text.split(maxsplit=2)
    task[1] = task[1].lower()
    addtodo (task[1], task[2])
    bot.reply_to(message, "Задача \"" + task[2] + "\" на " + task[1] + " принята")

@bot.message_handler(commands=['showall'])
def showall(message):
    dates = list(DB)
    answer = ""
    for i in dates:
        for k in DB[i]:
            answer = answer + i + " : " + k + "\n"
    bot.reply_to(message, answer)
#    print(dates)
#    bot.reply_to(message, str(dates))

@bot.message_handler(commands=['show'])
def show(message):
    command=message.text.split(maxsplit=1)
    date=command[1].lower()
    date_u=command[1].upper()
    answer = ""
    if date in DB:
        for task in DB[date]:
            answer = answer + "[ ] " + task + "\n"
        bot.reply_to(message, date_u + "\n" + answer)
    else:
        bot.reply_to(message, "Нет задач на данную дату!")

bot.infinity_polling()
