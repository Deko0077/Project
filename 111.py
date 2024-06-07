import asyncio
import json
from telebot import types, TeleBot

token = '6324727670:AAGgUk1O13kbLa0wuMWSBeZw6Fy7uLVI45A'

bot = TeleBot(token)

active_question = None
active_otvet = None
active_themes = {}
active_user_question = {}
active_user_otvet = {}


def addition_questions(message):
    global active_question, active_themes

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    file.close()
    file = open('themes.json', 'w', encoding='utf-8')
    themes[active_themes[message.chat.id]]["questions"][message.text] = {
        "otvets": {}
    }
    json.dump(themes, file, ensure_ascii=False)
    active_question = message.text
    file.close()
    keyborddd = types.InlineKeyboardMarkup()
    buttonn1 = types.InlineKeyboardButton(text='Добавление ответа', callback_data='Добавление ответа')
    keyborddd.add(buttonn1)
    bot.send_message(message.from_user.id, text='Добавить ответ к написанному вопросу', reply_markup=keyborddd)


def addition_otvets(message):
    global active_question, active_themes, active_otvet

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    file.close()
    file = open('themes.json', 'w', encoding='utf-8')
    themes[active_themes[message.chat.id]]["questions"][active_question]["otvets"][message.text] = {}
    json.dump(themes, file, ensure_ascii=False)
    active_otvet = message.text
    file.close()
    bot.send_message(message.from_user.id, text='Ответ успешно добавлен')
    bot.register_next_step_handler(message, get_otvet)
    keyborddd = types.InlineKeyboardMarkup()
    buttonn1 = types.InlineKeyboardButton(text='Продолжение диалога', callback_data='Продолжение диалога')
    keyborddd.add(buttonn1)
    bot.send_message(message.from_user.id, text='Логическое продолжение диалога (нажмите на кнопку)', reply_markup=keyborddd)


def addition_answer(message):
    global active_themes, active_question, active_otvet

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    file.close()
    file = open('themes.json', 'w', encoding='utf-8')
    themes[active_themes[message.chat.id]]["questions"][active_question]["otvets"][active_otvet] = {
            "question": message.text
          }
    json.dump(themes, file, ensure_ascii=False)
    file.close()
    bot.send_message(message.from_user.id, text='Вопрос успешно добавлен')
    bot.register_next_step_handler(message, answer_otvet)
    keyborddd = types.InlineKeyboardMarkup()
    buttonn1 = types.InlineKeyboardButton(text='Добавить новую тему', callback_data='Добавить новую тему')
    buttonn2 = types.InlineKeyboardButton(text='Список существующих тем', callback_data='Список существующих тем')
    keyborddd.add(buttonn1)
    keyborddd.add(buttonn2)
    bot.send_message(message.from_user.id, text='Нажмите на кнопку', reply_markup=keyborddd)


def del_theme(chat_id):
    global active_themes

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    file.close()
    del themes[active_themes[chat_id]]
    file = open('themes.json', 'w', encoding='utf-8')
    json.dump(themes, file, ensure_ascii=False)
    file.close()
    bot.send_message(chat_id, text='Вы успешно удалили тему')
    keyborddd = types.InlineKeyboardMarkup()
    buttonn1 = types.InlineKeyboardButton(text='Добавить новую тему', callback_data='Добавить новую тему')
    buttonn2 = types.InlineKeyboardButton(text='Список существующих тем', callback_data='Список существующих тем')
    keyborddd.add(buttonn1)
    keyborddd.add(buttonn2)
    bot.send_message(chat_id, text='Нажмите на кнопку', reply_markup=keyborddd)


def del_questions(chat_id):
    global active_themes

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    active_theme = active_themes[chat_id]
    questions = themes[active_theme]['questions']
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    text = 'Выберите вопрос который хотите удалить\n'
    for i in range(len(list(questions.keys()))):
        text += str(i + 1) + '. ' + list(questions.keys())[i] + '\n'
        button = types.InlineKeyboardButton(text=str(i + 1), callback_data='3|' + str(i + 1))
        keyboard.add(button)
    bot.send_message(chat_id, text=text, reply_markup=keyboard)


def del_question(chat_id, chosenOption):
    global active_themes

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    active_theme = active_themes[chat_id]
    questions = themes[active_theme]['questions']
    file.close()
    questionsList = list(questions.keys())
    editableQuestion = questionsList[chosenOption - 1]
    del themes[active_theme]['questions'][editableQuestion]
    file = open('themes.json', 'w', encoding='utf-8')
    json.dump(themes, file, ensure_ascii=False)
    file.close()
    bot.send_message(chat_id=chat_id, text='Вы успешно удалили вопрос')
    keyborddd = types.InlineKeyboardMarkup()
    buttonn1 = types.InlineKeyboardButton(text='Добавить новую тему', callback_data='Добавить новую тему')
    buttonn2 = types.InlineKeyboardButton(text='Список существующих тем', callback_data='Список существующих тем')
    keyborddd.add(buttonn1)
    keyborddd.add(buttonn2)
    bot.send_message(chat_id, text='Нажмите на кнопку', reply_markup=keyborddd)


def del_otvets(chat_id):
    global active_themes

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    active_theme = active_themes[chat_id]
    otvets = themes[active_theme]['questions']
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    text = 'Выберите вопрос в котором вы хотите удалить ответ\n'
    for i in range(len(list(otvets.keys()))):
        text += str(i + 1) + '. ' + list(otvets.keys())[i] + '\n'
        button = types.InlineKeyboardButton(text=str(i + 1), callback_data='7|' + str(i + 1))
        keyboard.add(button)
    bot.send_message(chat_id, text=text, reply_markup=keyboard)


def del_otvet(chat_id, chosenOption):
    global active_user_otvet, active_themes, active_question

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    active_theme = active_themes[chat_id]
    otvets = themes[active_theme]['questions'][active_question]['otvets']
    file.close()
    test = list(themes[active_theme]['questions'][active_question]['otvets'].keys())[active_user_otvet[chat_id] - 1]
    active_user_otvet[chat_id] = test
    del otvets[test]
    file = open('themes.json', 'w', encoding='utf-8')
    json.dump(themes, file, ensure_ascii=False)
    file.close()
    bot.send_message(chat_id=chat_id, text='Вы успешно удалили ответ')
    keyborddd = types.InlineKeyboardMarkup()
    buttonn1 = types.InlineKeyboardButton(text='Добавить новую тему', callback_data='Добавить новую тему')
    buttonn2 = types.InlineKeyboardButton(text='Список существующих тем', callback_data='Список существующих тем')
    keyborddd.add(buttonn1)
    keyborddd.add(buttonn2)
    bot.send_message(chat_id, text='Нажмите на кнопку', reply_markup=keyborddd)


def find_otvet_for_del(chat_id, chosenOption):
    global active_question, active_themes, active_question

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    active_theme = active_themes[chat_id]
    active_question = list(themes[active_theme]['questions'].keys())[chosenOption - 1]
    otvets = themes[active_theme]['questions'][active_question]['otvets']
    file.close()
    otvetsList = list(otvets.keys())
    keyboard = types.InlineKeyboardMarkup()
    text = 'Выберите ответ который хотите изменить\n'
    for i in range(len(list(otvets.keys()))):
        text += str(i + 1) + '. ' + list(otvets.keys())[i] + '\n'
        button = types.InlineKeyboardButton(text=str(i + 1), callback_data='8|' + str(i + 1))
        keyboard.add(button)
    bot.send_message(chat_id, text=text, reply_markup=keyboard)


def edit_otvets(chat_id):
    global active_themes

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    active_theme = active_themes[chat_id]
    otvets = themes[active_theme]['questions']
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    text = 'Выберите вопрос в котором вы хотите изменить ответ\n'
    for i in range(len(list(otvets.keys()))):
        text += str(i + 1) + '. ' + list(otvets.keys())[i] + '\n'
        button = types.InlineKeyboardButton(text=str(i + 1), callback_data='5|' + str(i + 1))
        keyboard.add(button)
    bot.send_message(chat_id, text=text, reply_markup=keyboard)


def edit_otvet(message):
    global active_user_otvet, active_themes, active_question

    chat_id = message.chat.id
    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    active_theme = active_themes[chat_id]
    otvets = themes[active_theme]['questions'][active_question]['otvets']
    file.close()
    test = list(themes[active_theme]['questions'][active_question]['otvets'].keys())[active_user_otvet[chat_id] - 1]
    active_user_otvet[chat_id] = test
    print(test)
    otvets[message.text] = otvets[active_user_otvet[chat_id]]
    del otvets[test]
    file = open('themes.json', 'w', encoding='utf-8')
    json.dump(themes, file, ensure_ascii=False)
    file.close()
    bot.send_message(chat_id=message.chat.id, text='Вы успешно изменили ответ')
    keyborddd = types.InlineKeyboardMarkup()
    buttonn1 = types.InlineKeyboardButton(text='Добавить новую тему', callback_data='Добавить новую тему')
    buttonn2 = types.InlineKeyboardButton(text='Список существующих тем', callback_data='Список существующих тем')
    keyborddd.add(buttonn1)
    keyborddd.add(buttonn2)
    bot.send_message(message.from_user.id, text='Нажмите на кнопку', reply_markup=keyborddd)


def find_otvet_for_edit(message, chat_id, chosenOption):
    global active_question, active_themes, active_question

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    active_theme = active_themes[chat_id]
    active_question = list(themes[active_theme]['questions'].keys())[chosenOption - 1]
    otvets = themes[active_theme]['questions'][active_question]['otvets']
    file.close()
    otvetsList = list(otvets.keys())
    keyboard = types.InlineKeyboardMarkup()
    text = 'Выберите ответ который хотите изменить\n'
    for i in range(len(list(otvets.keys()))):
        text += str(i + 1) + '. ' + list(otvets.keys())[i] + '\n'
        button = types.InlineKeyboardButton(text=str(i + 1), callback_data='6|' + str(i + 1))
        keyboard.add(button)
    bot.send_message(chat_id, text=text, reply_markup=keyboard)


def edit_questions(chat_id):
    global active_themes

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    active_theme = active_themes[chat_id]
    questions = themes[active_theme]['questions']
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    text = 'Выберите вопрос который хотите изменить\n'
    for i in range(len(list(questions.keys()))):
        text += str(i + 1) + '. ' + list(questions.keys())[i] + '\n'
        button = types.InlineKeyboardButton(text=str(i + 1), callback_data='2|' + str(i + 1))
        keyboard.add(button)
    bot.send_message(chat_id, text=text, reply_markup=keyboard)


def edit_question(message):
    global active_user_question, active_themes

    chat_id = message.chat.id
    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    active_theme = active_themes[chat_id]
    questions = themes[active_theme]['questions']
    file.close()
    questions[message.text] = questions[active_user_question[chat_id]]
    del questions[active_user_question[chat_id]]
    del active_user_question[chat_id]
    file = open('themes.json', 'w', encoding='utf-8')
    json.dump(themes, file, ensure_ascii=False)
    file.close()
    bot.send_message(chat_id=message.chat.id, text='Вы успешно изменили вопрос')
    keyborddd = types.InlineKeyboardMarkup()
    buttonn1 = types.InlineKeyboardButton(text='Добавить новую тему', callback_data='Добавить новую тему')
    buttonn2 = types.InlineKeyboardButton(text='Список существующих тем', callback_data='Список существующих тем')
    keyborddd.add(buttonn1)
    keyborddd.add(buttonn2)
    bot.send_message(message.from_user.id, text='Нажмите на кнопку', reply_markup=keyborddd)


def find_question_for_edit(message, chat_id, chosenOption):
    global active_themes, active_user_question

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    active_theme = active_themes[chat_id]
    questions = themes[active_theme]['questions']
    file.close()
    questionsList = list(questions.keys())
    editableQuestion = questionsList[chosenOption - 1]
    active_user_question[chat_id] = editableQuestion
    bot.send_message(chat_id, text='Напишите вопрос')
    bot.register_next_step_handler(message, edit_question)


def edit_theme_name(message):
    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    file.close()
    value = themes[active_themes[message.chat.id]]
    themes[message.text] = value
    del themes[active_themes[message.chat.id]]
    file = open('themes.json', 'w', encoding='utf-8')
    json.dump(themes, file, ensure_ascii=False)
    file.close()
    active_themes[message.chat.id] = message.text
    bot.send_message(message.from_user.id, text='Название темы успешно изменено')
    keyborddd = types.InlineKeyboardMarkup()
    buttonn1 = types.InlineKeyboardButton(text='Добавить новую тему', callback_data='Добавить новую тему')
    buttonn2 = types.InlineKeyboardButton(text='Список существующих тем', callback_data='Список существующих тем')
    keyborddd.add(buttonn1)
    keyborddd.add(buttonn2)
    bot.send_message(message.from_user.id, text='Нажмите на кнопку', reply_markup=keyborddd)


def get_editing(user_id):
    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    file.close()
    keyborddd = types.InlineKeyboardMarkup()
    buttonn1 = types.InlineKeyboardButton(text='1. Изменение темы', callback_data='1. Изменение темы')
    buttonn2 = types.InlineKeyboardButton(text='2. Изменение вопросов', callback_data='2. Изменение вопросов')
    buttonn3 = types.InlineKeyboardButton(text='3. Изменение ответов', callback_data='3. Изменение ответов')
    buttonn4 = types.InlineKeyboardButton(text='4. Удаление темы', callback_data='4. Удаление темы')
    buttonn5 = types.InlineKeyboardButton(text='5. Удаление вопросов', callback_data='5. Удаление вопросов')
    buttonn6 = types.InlineKeyboardButton(text='6. Удаление ответов', callback_data='6. Удаление ответов')
    buttonn7 = types.InlineKeyboardButton(text='7. Добавление вопросов и ответов',
                                          callback_data='7. Добавление вопросов и ответов')
    keyborddd.add(buttonn1)
    keyborddd.add(buttonn2)
    keyborddd.add(buttonn3)
    keyborddd.add(buttonn4)
    keyborddd.add(buttonn5)
    keyborddd.add(buttonn6)
    keyborddd.add(buttonn7)
    bot.send_message(user_id, text='Выберите одну из кнопок', reply_markup=keyborddd)


def get_otvet(message):
    global active_otvet, active_themes

    file = open('themes.json', 'r', encoding='utf-8')
    otvets = json.load(file)
    file.close()
    file = open('themes.json', 'w', encoding='utf-8')
    otvets[active_themes[message.chat.id]]["questions"][active_question]["otvets"][message.text] = {}
    json.dump(otvets, file, ensure_ascii=False)
    active_otvet = message.text
    file.close()
    bot.send_message(message.from_user.id, text='Ответ успешно добавлен')
    bot.register_next_step_handler(message, get_otvet)
    keyborddd = types.InlineKeyboardMarkup()
    buttonn1 = types.InlineKeyboardButton(text='Продолжение', callback_data='Продолжение')
    keyborddd.add(buttonn1)
    bot.send_message(message.from_user.id, text='Логическое продолжение диалога (нажмите на кнопку)', reply_markup=keyborddd)


def answer_otvet(message):
    global active_themes, active_question, active_otvet

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    file.close()
    file = open('themes.json', 'w', encoding='utf-8')
    themes[active_themes[message.chat.id]]["questions"][active_question]["otvets"][active_otvet] = {
            "question": message.text
          }
    json.dump(themes, file, ensure_ascii=False)
    file.close()
    bot.send_message(message.from_user.id, text='Вопрос успешно добавлен')
    bot.register_next_step_handler(message, answer_otvet)
    keyborddd = types.InlineKeyboardMarkup()
    buttonn1 = types.InlineKeyboardButton(text='Добавить новую тему', callback_data='Добавить новую тему')
    buttonn2 = types.InlineKeyboardButton(text='Список существующих тем', callback_data='Список существующих тем')
    keyborddd.add(buttonn1)
    keyborddd.add(buttonn2)
    bot.send_message(message.from_user.id, text='Нажмите на кнопку', reply_markup=keyborddd)


def get_question(message):
    global active_question, active_themes

    file = open('themes.json', 'r', encoding='utf-8')
    questions = json.load(file)
    file.close()
    file = open('themes.json', 'w', encoding='utf-8')
    questions[active_themes[message.chat.id]]["questions"][message.text] = {
        "otvets": {}
    }
    json.dump(questions, file, ensure_ascii=False)
    active_question = message.text
    file.close()
    bot.send_message(message.from_user.id, text='Вопрос успешно добавлен')
    keyborddd = types.InlineKeyboardMarkup()
    buttonn1 = types.InlineKeyboardButton(text='Добавить ответ к вопросу', callback_data='Добавить ответ к вопросу')
    buttonn2 = types.InlineKeyboardButton(text='Добавить ещё один вопрос', callback_data='Добавить ещё один вопрос')
    keyborddd.add(buttonn1)
    keyborddd.add(buttonn2)
    bot.send_message(message.from_user.id, text='Выберите одну из кнопок', reply_markup=keyborddd)


def get_theme(message):
    global active_themes

    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    file.close()
    file = open('themes.json', 'w', encoding='utf-8')
    themes[message.text] = {
        "questions": {}
    }
    json.dump(themes, file, ensure_ascii=False)
    active_themes[message.chat.id] = message.text
    file.close()
    bot.send_message(message.from_user.id, text='Тема успешно добавлена')
    keyborddd = types.InlineKeyboardMarkup()
    buttonn1 = types.InlineKeyboardButton(text='Добавить вопрос к теме', callback_data='Добавить вопрос к теме')
    buttonn2 = types.InlineKeyboardButton(text='Добавить ещё одну тему', callback_data='Добавить ещё одну тему')
    keyborddd.add(buttonn1)
    keyborddd.add(buttonn2)
    bot.send_message(message.from_user.id, text='Выберите одну из кнопок', reply_markup=keyborddd)


@bot.message_handler(content_types=['text'])
def get_message(message):
    global active_user_question, active_user_otvet

    if message.text == '/start':
        bot.set_my_commands(
            commands=[
                types.BotCommand('/start', 'Запуск Бота')
            ],
            scope=types.BotCommandScopeChat(message.chat.id)
        )
        klava = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Список существующих тем', callback_data='Список существующих тем')
        button2 = types.InlineKeyboardButton(text='Добавление темы', callback_data='Добавление темы')
        klava.add(button1)
        klava.add(button2)
        bot.send_message(message.from_user.id, text='Добро пожаловать в телеграм бот (АДМИНИСТРАТОР)')
        bot.send_message(message.from_user.id, text='Выберите одну из перечисленных кнопок', reply_markup=klava)
    else:
        if active_user_question[message.from_user.id]:
            edit_question(message)
        elif active_user_otvet[message.from_user.id]:
            edit_otvet(message)


def get_exsisting(chat_id):
    file = open('themes.json', 'r', encoding='utf-8')
    themes = json.load(file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    for theme in list(themes.keys()):
        button = types.InlineKeyboardButton(text=theme, callback_data=theme)
        keyboard.add(button)
    bot.send_message(chat_id, text='Выберите одну из существующих тем', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)

    # информация для обработки выбранного шага (пункты 1-8)
    isPointChoose = False
    chosenPoint = None
    chosenOption = None
    if '|' in call.data:
        isPointChoose = True
        temp = call.data.split('|')
        chosenPoint = int(temp[0])
        chosenOption = int(temp[1])

    if call.data == 'Список существующих тем':
        get_exsisting(call.message.chat.id)
    elif call.data == 'Добавить новую тему':
        bot.send_message(call.from_user.id, text='Напишите название для новой темы')
        bot.register_next_step_handler(call.message, get_theme)
    elif call.data == 'Добавление темы':
        bot.send_message(call.from_user.id, text='Напишите название для новой темы')
        bot.register_next_step_handler(call.message, get_theme)
    elif call.data == 'Добавить вопрос к теме':
        bot.send_message(call.from_user.id, text='Напишите вопрос к теме')
        bot.register_next_step_handler(call.message, get_question)
    elif call.data == 'Добавить ещё одну тему':
        bot.send_message(call.from_user.id, text='Пожалуйста введите название новой темы')
        bot.register_next_step_handler(call.message, get_theme)
    elif call.data == 'Добавить ответ к вопросу':
        bot.send_message(call.from_user.id, text='Напишите ответ')
        bot.register_next_step_handler(call.message, get_otvet)
    elif call.data == 'Добавить ещё один ответ':
        bot.send_message(call.from_user.id, text='Пожалуйста введите ответ к вопросу')
        bot.register_next_step_handler(call.message, get_otvet)
    elif call.data == 'Продолжение':
        bot.send_message(call.from_user.id, text='Напишите вопрос к которому перейдёт следующее обращение')
        bot.register_next_step_handler(call.message, answer_otvet)
    elif call.data == 'Продолжение диалога':
        bot.send_message(call.from_user.id, text='Напишите вопрос к которому перейдёт следующее обращение')
        bot.register_next_step_handler(call.message, addition_answer)
    elif call.data == 'Добавить ещё один вопрос':
        bot.send_message(call.from_user.id, text='Пожалуйста введите вопрос к теме')
        bot.register_next_step_handler(call.message, get_question)
    elif call.data == '1. Изменение темы':
        bot.send_message(call.from_user.id, text='Напишите новое название для темы')
        bot.register_next_step_handler(call.message, edit_theme_name)
    elif call.data == '2. Изменение вопросов':
        edit_questions(call.message.chat.id)
    elif call.data == '3. Изменение ответов':
        edit_otvets(call.message.chat.id)
    elif call.data == '4. Удаление темы':
       del_theme(call.message.chat.id)
    elif call.data == '5. Удаление вопросов':
        del_questions(call.message.chat.id)
    elif call.data == '6. Удаление ответов':
        del_otvets(call.message.chat.id)
    elif call.data == '7. Добавление вопросов и ответов':
        bot.send_message(call.from_user.id, text='Напишите вопрос')
        bot.register_next_step_handler(call.message, addition_questions)
    elif call.data == 'Добавление ответа':
        bot.send_message(call.from_user.id, text='Напишите ответ')
        bot.register_next_step_handler(call.message, addition_otvets)
    elif isPointChoose:
        if chosenPoint == 2:
            find_question_for_edit(call.message, call.message.chat.id, chosenOption)
        elif chosenPoint == 3:
            del_question(call.message.chat.id, chosenOption)
        elif chosenPoint == 4:
            del_otvet(call.message.chat.id, chosenOption)
        elif chosenPoint == 5:
            find_otvet_for_edit(call.message, call.message.chat.id, chosenOption)
        elif chosenPoint == 6:
            active_user_otvet[call.message.chat.id] = chosenOption
            bot.send_message(call.message.chat.id, text='Напишите новый текст вопроса')
            bot.register_next_step_handler(call.message, edit_otvet)
        elif chosenPoint == 7:
            find_otvet_for_del(call.message.chat.id, chosenOption)
        elif chosenPoint == 8:
            active_user_otvet[call.message.chat.id] = chosenOption
            del_otvet(call.message.chat.id, chosenOption)
    else:
        file = open('themes.json', 'r', encoding='utf-8')
        themes = json.load(file)
        file.close()
        for theme in list(themes):
            if call.data == theme:
                active_themes[call.message.chat.id] = theme
                get_editing(call.from_user.id)
                break

bot.polling(none_stop=True, interval=0)