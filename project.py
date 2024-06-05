import telebot
from telebot import types
import json
import requests
from bs4 import BeautifulSoup

token = '6974569769:AAHFHGT2YEhws3nnmq2dUYZ_13qGO74G91I'

bot = telebot.TeleBot(token)

page = 1
limit = 10

active_theme = None
active_question = None
active_otvets = None
active_info = None

buttons_sport = [
            types.InlineKeyboardButton(text='Биатлон', callback_data='info_Биатлон'),
            types.InlineKeyboardButton(text='Бобслей', callback_data='info_Бобслей'),
            types.InlineKeyboardButton(text='Горнолыжный спорт', callback_data='info_Горнолыжный спорт'),
            types.InlineKeyboardButton(text='Кёрлинг', callback_data='info_Кёрлинг'),
            types.InlineKeyboardButton(text='Лыжное двоеборье', callback_data='info_Лыжное двоеборье'),
            types.InlineKeyboardButton(text='Лыжные гонки', callback_data='info_Лыжные гонки'),
            types.InlineKeyboardButton(text='Прыжки на лыжах', callback_data='info_Прыжки на лыжах'),
            types.InlineKeyboardButton(text='Санный спорт', callback_data='info_Санный спорт'),
            types.InlineKeyboardButton(text='Скелетон', callback_data='info_Скелетон'),
            types.InlineKeyboardButton(text='Сноуборд', callback_data='info_Сноуборд'),
            types.InlineKeyboardButton(text='Фигурное катание', callback_data='info_Фигурное катание'),
            types.InlineKeyboardButton(text='Фристайл', callback_data='info_Фристайл'),
            types.InlineKeyboardButton(text='Хоккей', callback_data='info_Хоккей'),
            types.InlineKeyboardButton(text='Шорт - трек', callback_data='info_Шорт - трек'),
            types.InlineKeyboardButton(text='Баскетбол', callback_data='info_Баскетбол'),
            types.InlineKeyboardButton(text='Бейсбол', callback_data='info_Бейсбол'),
            types.InlineKeyboardButton(text='Бокс', callback_data='info_Бокс'),
            types.InlineKeyboardButton(text='Вело спорт', callback_data='info_Вело спорт'),
            types.InlineKeyboardButton(text='Водное поло', callback_data='info_Водное поло'),
            types.InlineKeyboardButton(text='Волейбол', callback_data='info_Волейбол'),
            types.InlineKeyboardButton(text='Гандбол', callback_data='info_Гандбол'),
            types.InlineKeyboardButton(text='Гольф', callback_data='info_Гольф'),
            types.InlineKeyboardButton(text='Гребля на байдарках', callback_data='info_Гребля на байдарках'),
            types.InlineKeyboardButton(text='Гребный слалом', callback_data='info_Гребный слалом'),
            types.InlineKeyboardButton(text='Гребной спорт', callback_data='info_Гребной спорт'),
            types.InlineKeyboardButton(text='Дзюдо', callback_data='info_Дзюдо'),
            types.InlineKeyboardButton(text='Бадминтон', callback_data='info_Бадминтон'),
            types.InlineKeyboardButton(text='Каратэ', callback_data='info_Каратэ'),
            types.InlineKeyboardButton(text='Конный спорт', callback_data='info_Конный спорт'),
            types.InlineKeyboardButton(text='Лёгкая атлетика', callback_data='info_Лёгкая атлетика'),
            types.InlineKeyboardButton(text='Настольный теннис', callback_data='info_Настольный теннис'),
            types.InlineKeyboardButton(text='Парусный спорт', callback_data='info_Парусный спорт'),
            types.InlineKeyboardButton(text='Плавание', callback_data='info_Плавание'),
            types.InlineKeyboardButton(text='Пляжный волейбол', callback_data='info_Пляжный волейбол'),
            types.InlineKeyboardButton(text='Прыжки в воду', callback_data='info_Прыжки в воду'),
            types.InlineKeyboardButton(text='Прыжки на батуте', callback_data='info_Прыжки на батуте'),
            types.InlineKeyboardButton(text='Регби', callback_data='info_Регби'),
            types.InlineKeyboardButton(text='Сёрфинг', callback_data='info_Сёрфинг'),
            types.InlineKeyboardButton(text='Скалолазание', callback_data='info_Скалолазание'),
            types.InlineKeyboardButton(text='Скейтбординг', callback_data='info_Скейтбординг'),
            types.InlineKeyboardButton(text='Современное пятиборье', callback_data='info_Современное пятиборье'),
            types.InlineKeyboardButton(text='Софтбол', callback_data='info_Софтбол'),
            types.InlineKeyboardButton(text='Стрельба', callback_data='info_Стрельба'),
            types.InlineKeyboardButton(text='Стрельба из лука', callback_data='info_Стрельба из лука'),
            types.InlineKeyboardButton(text='Теннис', callback_data='info_Теннис'),
            types.InlineKeyboardButton(text='Триатлон', callback_data='info_Триатлон'),
            types.InlineKeyboardButton(text='Тхэквондо', callback_data='info_Тхэквондо'),
            types.InlineKeyboardButton(text='Тяжёлая атлетика', callback_data='info_Тяжёлая атлетика'),
            types.InlineKeyboardButton(text='Фехтование', callback_data='info_Фехтование'),
            types.InlineKeyboardButton(text='Футбол', callback_data='info_Футбол')
        ]

buttons_game = [
            types.InlineKeyboardButton(text='CS2', callback_data='info_CS2'),
            types.InlineKeyboardButton(text='Valorant', callback_data='info_Valorant'),
            types.InlineKeyboardButton(text='Undertale', callback_data='info_Undertale'),
            types.InlineKeyboardButton(text='Deltarune', callback_data='info_Deltarune'),
            types.InlineKeyboardButton(text='Minecraft', callback_data='info_Minecraft'),
            types.InlineKeyboardButton(text='Terraria', callback_data='info_Terraria'),
            types.InlineKeyboardButton(text='Grand The Auto V', callback_data='info_Grand The Auto V'),
            types.InlineKeyboardButton(text='Geometry Dash', callback_data='info_Geometry Dash'),
            types.InlineKeyboardButton(text='Brawl Stars', callback_data='info_Brawl Stars'),
            types.InlineKeyboardButton(text='PUBG: Battlegrounds', callback_data='info_PUBG: Battlegrounds'),
            types.InlineKeyboardButton(text='Cyberpunk 2077', callback_data='info_Cyberpunk 2077'),
            types.InlineKeyboardButton(text='Standoff2', callback_data='info_Standoff2'),
            types.InlineKeyboardButton(text='Forza Horizon 5', callback_data='info_Forza Horizon 5'),
            types.InlineKeyboardButton(text='Forza Horizon 4', callback_data='info_Forza Horizon 4'),
            types.InlineKeyboardButton(text='Horizon Zero Dawn', callback_data='info_Horizon Zero Dawn'),
            types.InlineKeyboardButton(text='Davil May Cry 5', callback_data='info_Davil May Cry 5'),
            types.InlineKeyboardButton(text='Cuphead', callback_data='info_Cuphead'),
            types.InlineKeyboardButton(text='Goat Simulator', callback_data='info_Goat Simulator'),
            types.InlineKeyboardButton(text='FIFA', callback_data='info_FIFA'),
            types.InlineKeyboardButton(text='Five Nights at Freddys', callback_data='info_Five Nights at Freddys'),
            types.InlineKeyboardButton(text='Apex Legends', callback_data='info_Apex Legends'),
            types.InlineKeyboardButton(text='Fall Guys', callback_data='info_Fall Guys'),
            types.InlineKeyboardButton(text='Rocket League', callback_data='info_Rocket League'),
            types.InlineKeyboardButton(text='Among Us', callback_data='info_Among Us'),
            types.InlineKeyboardButton(text='Poppy Playtime', callback_data='info_Poppy Playtime'),
            types.InlineKeyboardButton(text='S.T.A.L.K.E.R', callback_data='info_S.T.A.L.K.E.R'),
            types.InlineKeyboardButton(text='eFootbal™', callback_data='info_eFootbal™'),
            types.InlineKeyboardButton(text='The Witcher', callback_data='info_The Witcher'),
            types.InlineKeyboardButton(text='Diablo', callback_data='info_Diablo'),
            types.InlineKeyboardButton(text='DOOM', callback_data='info_DOOM'),
            types.InlineKeyboardButton(text='Mortal Kombat', callback_data='info_Mortal Kombat'),
            types.InlineKeyboardButton(text='Tekken', callback_data='info_Tekken'),
            types.InlineKeyboardButton(text='The Last of Us', callback_data='info_The Last of Us'),
            types.InlineKeyboardButton(text='The Walking Dead', callback_data='info_The Walking Dead'),
            types.InlineKeyboardButton(text='Resident Evil', callback_data='info_Resident Evil'),
            types.InlineKeyboardButton(text='Dying Light', callback_data='info_Dying Light'),
            types.InlineKeyboardButton(text='Unrecord', callback_data='info_Unrecord'),
            types.InlineKeyboardButton(text='Gran Turismo', callback_data='info_Gran Turismo'),
            types.InlineKeyboardButton(text='Смута', callback_data='info_Смута'),
            types.InlineKeyboardButton(text='Little Nightmares', callback_data='info_Little Nightmares'),
            types.InlineKeyboardButton(text='Elden Ring', callback_data='info_Elden Ring'),
            types.InlineKeyboardButton(text='The elder scrolls V Skyrim', callback_data='info_The elder scrolls V Skyrim'),
            types.InlineKeyboardButton(text='Final Fantasy', callback_data='info_Final Fantasy'),
            types.InlineKeyboardButton(text='The Legend of Zelda', callback_data='info_The Legend of Zelda'),
            types.InlineKeyboardButton(text='Genshin Impact', callback_data='info_Genshin Impact'),
            types.InlineKeyboardButton(text='Helldivers 2', callback_data='info_Helldivers 2'),
            types.InlineKeyboardButton(text='Dota 2', callback_data='info_Dota 2'),
            types.InlineKeyboardButton(text='Hollow Knight', callback_data='info_Hollow Knight'),
            types.InlineKeyboardButton(text='Call of Duty: Warzon', callback_data='info_Call of Duty: Warzon'),
            types.InlineKeyboardButton(text='Hello Neighbor', callback_data='info_Hello Neighbor')

]


buttons_auto = [
            types.InlineKeyboardButton(text='Audi A4', callback_data='info_Audi A4'),
            types.InlineKeyboardButton(text='Audi S5', callback_data='info_Audi S5'),
            types.InlineKeyboardButton(text='Audi RS6', callback_data='info_Audi RS6'),
            types.InlineKeyboardButton(text='Audi A7 Sportback', callback_data='info_Audi A7 Sportback'),
            types.InlineKeyboardButton(text='Audi E-Tron', callback_data='info_Audi E-Tron'),
            types.InlineKeyboardButton(text='BMW M8', callback_data='info_BMW M8'),
            types.InlineKeyboardButton(text='BMW 4', callback_data='info_BMW 4'),
            types.InlineKeyboardButton(text='BMW X5', callback_data='info_BMW X5'),
            types.InlineKeyboardButton(text='BMW X7', callback_data='info_BMW X7'),
            types.InlineKeyboardButton(text='BMW i7', callback_data='info_BMW i7'),
            types.InlineKeyboardButton(text='Mercedec-Benz AMG GT', callback_data='info_Mercedec-Benz AMG GT'),
            types.InlineKeyboardButton(text='Mercedec-Benz CLS', callback_data='info_Mercedec-Benz CLS'),
            types.InlineKeyboardButton(text='Mercedec-Benz A', callback_data='info_Mercedec-Benz A'),
            types.InlineKeyboardButton(text='Mercedec-Benz G AMG', callback_data='info_Mercedec-Benz G AMG'),
            types.InlineKeyboardButton(text='Mercedec-Benz GLA', callback_data='info_Mercedec-Benz GLA'),
            types.InlineKeyboardButton(text='Ford Mustag', callback_data='info_Ford Mustag'),
            types.InlineKeyboardButton(text='Ford Fiesta', callback_data='info_Ford Fiesta'),
            types.InlineKeyboardButton(text='Ford Puma', callback_data='info_Ford Puma'),
            types.InlineKeyboardButton(text='Ford Ranger Raptor', callback_data='info_Ford Ranger Raptor'),
            types.InlineKeyboardButton(text='Ford Mustang Mach-E', callback_data='info_Ford Mustang Mach-E'),
            types.InlineKeyboardButton(text='Nissan Z', callback_data='info_Nissan Z'),
            types.InlineKeyboardButton(text='Nissan GT-R', callback_data='info_Nissan GT-R'),
            types.InlineKeyboardButton(text='Nissan Juke', callback_data='info_Nissan Juke'),
            types.InlineKeyboardButton(text='Nissan Navara', callback_data='info_Nissan Navara'),
            types.InlineKeyboardButton(text='Nissan Murano', callback_data='info_Nissan Murano'),
            types.InlineKeyboardButton(text='Tesla Model 3', callback_data='info_Tesla Model 3'),
            types.InlineKeyboardButton(text='Tesla Model S', callback_data='info_Tesla Model S'),
            types.InlineKeyboardButton(text='Tesla Model X', callback_data='info_Tesla Model X'),
            types.InlineKeyboardButton(text='Tesla Cybertruck', callback_data='info_Tesla Cybertruck'),
            types.InlineKeyboardButton(text='Lamborghini Urus', callback_data='info_Lamborghini Urus'),
            types.InlineKeyboardButton(text='Lamborghini Huracan', callback_data='info_Lamborghini Huracan'),
            types.InlineKeyboardButton(text='Lamborghini Aventador', callback_data='info_Lamborghini Aventador'),
            types.InlineKeyboardButton(text='Lamborghini Centenario', callback_data='info_Lamborghini Centenario'),
            types.InlineKeyboardButton(text='Lamborghini Sian', callback_data='info_Lamborghini Sian'),
            types.InlineKeyboardButton(text='Ferrari Purosangue', callback_data='info_Ferrari Purosangue'),
            types.InlineKeyboardButton(text='Ferrari 812 Superfast', callback_data='info_Ferrari 812 Superfast'),
            types.InlineKeyboardButton(text='Ferrari Roma', callback_data='info_Ferrari Roma'),
            types.InlineKeyboardButton(text='Ferrari SF90 Stradale', callback_data='info_Ferrari SF90 Stradale'),
            types.InlineKeyboardButton(text='Ferrari Enzo', callback_data='info_Ferrari Enzo'),
            types.InlineKeyboardButton(text='LADA Niva Travel', callback_data='info_LADA Niva Travel'),
            types.InlineKeyboardButton(text='LADA Vesta', callback_data='info_LADA Vesta'),
            types.InlineKeyboardButton(text='LADA Granta', callback_data='info_LADA Granta'),
            types.InlineKeyboardButton(text='LADA Largus', callback_data='info_LADA Largus'),
            types.InlineKeyboardButton(text='LADA Niva', callback_data='info_LADA Niva'),
            types.InlineKeyboardButton(text='Opel Crossland', callback_data='info_Opel Crossland'),
            types.InlineKeyboardButton(text='Opel Corsa', callback_data='info_Opel Corsa'),
            types.InlineKeyboardButton(text='Opel Astra', callback_data='info_Opel Astra'),
            types.InlineKeyboardButton(text='Opel Insignia', callback_data='info_Opel Insignia'),
            types.InlineKeyboardButton(text='Opel Mokka', callback_data='info_Opel Mokka'),
            types.InlineKeyboardButton(text='Bentley Continental GT', callback_data='info_Bentley Continental GT')
]


@bot.message_handler(content_types=['text'])
def get_message(message):

    if message.text == '/start':

        bot.set_my_commands(
            commands=[
                types.BotCommand('/start', 'Запуск бота'),
                types.BotCommand('/quest', 'Начать квест'),
                types.BotCommand('/info', 'Информация'),
                types.BotCommand('/help', 'Помощь')
            ],
            scope=types.BotCommandScopeChat(message.chat.id)
        )

        bot.send_message(message.from_user.id, text='''
*Привет!*
            
Тематик - бот помощник. Он поможет вам определиться с выбором во многих темах, в которых вы возможно не разбираетесь. 
Этот бот представлять возможность вам в выборе ответа на предложенные темы. 
Мы стараемся уточнить ваш выбор задавая вопросы с предложенными на них ответы по выбранной теме.
Так же вы можете узнать много интересных фактов о данной теме. 
*Наш бот не несет ответственности за ваш выбор и не несёт ни какого сексуального характера (18+)*.
            
*Желаем тебе удачи!*
            
*Здесь вы можете выполнить задачи как:*
            
1. Разобраться в темах исходя из своих предпочтений, отвечая на заданные вопросы.
2. Посмотреть краткую информацию многих первых 50-ти вещей.
3. Узнать много интересного.
4. Разобраться в своих предпочтениях.
5. Повеселиться!
            
Что-бы начать пользоваться ботом просто напишите команду из списка ниже.
            
*Список команд:*
            
/start - запуск бота
/quest - начать квест
/info - краткая информации о вещах
/help - Помощь
            
*Разработчики:*
            
- @DanilaDemchenko - Данила Демченко
- @daniilkiin - Данил Лаптев
            
*Если Бот вам не отвечает, перезапустите его командой /start или обратитесь к разработчикам данного бота.*
            
*Удачи!*''', parse_mode='Markdown')
        print(message.from_user.id, message.text)

    elif message.text == '/quest':

        keyboard = types.InlineKeyboardMarkup()

        file_themes = open('themes_example.json', 'r+', encoding='utf-8')
        full_theme = json.load(file_themes)
        for theme in list(full_theme.keys()):
            button_theme = types.InlineKeyboardButton(text=theme, callback_data='theme_'+theme)
            keyboard.add(button_theme)

        bot.send_message(message.from_user.id, '*Выберите тему:*', parse_mode='Markdown', reply_markup=keyboard)
        print(message.from_user.id, message.text)

    elif message.text == '/info':

        keyboard = types.InlineKeyboardMarkup()

        themes_buttons = [
            types.InlineKeyboardButton(text='Спорт', callback_data='info_Спорт'),
            types.InlineKeyboardButton(text='Видео игры', callback_data='info_Видео игры'),
            types.InlineKeyboardButton(text='Транспорт', callback_data='info_Транспорт')
        ]
        for i in range(len(themes_buttons)):
            keyboard.add(themes_buttons[i])
        bot.send_message(message.from_user.id, '*Выберите интерисующую вас тему:*', parse_mode='Markdown', reply_markup=keyboard)
        print(message.from_user.id, message.text)

    elif message.text == '/help':
        bot.send_message(message.from_user.id, text='''
        Если Бот вам не отвечает, перезапустите его командой /start или обратитесь к разработчикам данного бота!
        
        *Разработчики:*
        -@DanilaDemchenko - Данила Демченко
        -@daniilkiin - Данил Лаптев''', parse_mode='Markdown')
        print(message.from_user.id, message.text)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global page, active_theme, active_info, limit, active_question, active_otvets

    # Начало работы команды /quest

    if call.data.startswith('theme'):
        active_theme = call.data.split('_')[1]
        keyboard = types.InlineKeyboardMarkup()

        file_themes = open('themes_example.json', 'r+', encoding='utf-8')
        full_theme = json.load(file_themes)
        for questions in list(full_theme['theme']['question'].keys()):
            button_questions = types.InlineKeyboardButton(text=questions, callback_data='question_'+questions)
            keyboard.add(button_questions)

        if call.data.startswith('theme'):
            active_theme = call.data.split('_')[1]
            keyboard = types.InlineKeyboardMarkup()

            file_themes = open('themes_example.json', 'r+', encoding='utf-8')
            full_theme = json.load(file_themes)
            for questions in list(full_theme['Теннис']['question'].keys()):
                button_questions = types.InlineKeyboardButton(text=questions, callback_data='question_' + questions)
                keyboard.add(button_questions)

            bot.send_message(call.from_user.id, '*Выберите вопрос:*', parse_mode='Markdown', reply_markup=keyboard)

    elif call.data.startswith('question'):
        active_question = call.data.split('_')[1]
        keyboard = types.InlineKeyboardMarkup()

        file_themes = open('themes_example.json', 'r+', encoding='utf-8')
        full_theme = json.load(file_themes)
        for otvets in full_theme[active_theme]['question'][active_question]['otvets'].keys():
            button_otvets = types.InlineKeyboardButton(text=otvets, callback_data='otvets_' + otvets)
            keyboard.add(button_otvets)

        bot.send_message(call.from_user.id, '*Выберите  ответ:*', parse_mode='Markdown', reply_markup=keyboard)

    elif call.data.startswith('otvets'):
        active_otvets = call.data.split('_')[1]

        file_themes = open('themes_example.json', 'r+', encoding='utf-8')
        full_theme = json.load(file_themes)
        if 'question' in full_theme[active_theme]['question'][active_question]['otvets'][active_otvets]:
            active_question = full_theme[active_theme]['question'][active_question]['otvets'][active_otvets]['question']
            otvets = full_theme[active_theme]['question'][active_question]['otvets'].keys()
            keyboard = types.InlineKeyboardMarkup()

            for otvet in otvets:
                button_otvet = types.InlineKeyboardButton(text=otvet, callback_data='otvets_' + otvet)
                keyboard.add(button_otvet)
            bot.send_message(call.from_user.id, active_question, parse_mode='Markdown', reply_markup=keyboard)

    # Начало работы команды /info

    elif call.data.startswith('info'):
        active_info = call.data.split('_')[1]
        keyboard = types.InlineKeyboardMarkup()

        if active_info == 'Спорт':
            keyboard = types.InlineKeyboardMarkup()
            for i in range(page * limit - limit, min(len(buttons_sport), page * limit)):
                keyboard.add(buttons_sport[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='info_Вернуться к предыдущей странице'))
            if page * limit < len(buttons_sport):
                keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='info_Перейти на следующую страницу'))
            bot.send_message(call.from_user.id, '*50 видов спорта! Выберите интерисующий вид спорта:*', parse_mode='Markdown', reply_markup=keyboard)
        elif active_info == 'Перейти на следующую страницу':
            keyboard = types.InlineKeyboardMarkup()
            page += 1
            for i in range(page * limit - limit, min(len(buttons_sport), page * limit)):
                keyboard.add(buttons_sport[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='info_Вернуться к предыдущей странице'))
            if page * limit < len(buttons_sport):
                keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='info_Перейти на следующую страницу'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*50 видов спорта! Выберите интерисующий вид спорта:*', parse_mode='Markdown', reply_markup=keyboard)
        elif active_info == 'Вернуться к предыдущей странице':
            keyboard = types.InlineKeyboardMarkup()
            page -= 1
            for i in range(page * limit - limit, min(len(buttons_sport), page * limit)):
                keyboard.add(buttons_sport[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='info_Вернуться к предыдущей странице'))
            keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='info_Перейти на следующую страницу'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*50 видов спорта! Выберите интерисующий вид спорта:*', parse_mode='Markdown', reply_markup=keyboard)
        else:
            for button_sport in buttons_sport:
                if call.data == button_sport.callback_data:
                    file = open('info_sport.json', 'r+', encoding='utf-8')
                    info_sport = json.load(file)
                    for sport in info_sport:
                        if sport['Наименование'] == call.data.split('_')[1]:
                            url_sport = sport['Ссылка на информацию']
                            response = requests.get(url_sport)
                            soup = BeautifulSoup(response.text, 'lxml')
                            mini_info_sport = soup.select('div.mw-content-ltr.mw-parser-output > p')
                            name_sport = soup.find('span', class_='mw-page-title-main')
                            bot.send_message(call.from_user.id, text=('Название спорта: ' + name_sport.text))
                            bot.send_message(call.from_user.id, text=('Мини информация: ' + mini_info_sport[0].text))
                            bot.send_message(call.from_user.id, text=sport['Ссылка на информацию'])
            keyboard = types.InlineKeyboardMarkup()
            for i in range(page * limit - limit, min(len(buttons_sport), page * limit)):
                keyboard.add(buttons_sport[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='info_Вернуться к предыдущей странице'))
            if page * limit < len(buttons_sport):
                keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='info_Перейти на следующую страницу'))
            bot.send_message(call.from_user.id, '*50 видов спорта! Выберите интерисующий вид спорта:*', parse_mode='Markdown', reply_markup=keyboard)

        if active_info == 'Видео игры':
            keyboard = types.InlineKeyboardMarkup()
            for i in range(page * limit - limit, min(len(buttons_game), page * limit)):
                keyboard.add(buttons_game[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='info_Вернуться к предыдущей странице'))
            if page * limit < len(buttons_game):
                keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='info_Перейти на следующую страницу'))
            bot.send_message(call.from_user.id, '*50 видео игр! Выберите интерисующую вас игру:*', parse_mode='Markdown', reply_markup=keyboard)
        elif active_info == 'Перейти на следующую страницу':
                keyboard = types.InlineKeyboardMarkup()
                page += 1
                for i in range(page * limit - limit, min(len(buttons_game), page * limit)):
                    keyboard.add(buttons_game[i])
                if page != 1:
                    keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='info_Вернуться к предыдущей странице'))
                if page * limit < len(buttons_game):
                    keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='info_Перейти на следующую страницу'))
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*50 видео игр! Выберите интерисующую вас игру:*', parse_mode='Markdown', reply_markup=keyboard)
        elif active_info == 'Вернуться к предыдущей странице':
                keyboard = types.InlineKeyboardMarkup()
                page -= 1
                for i in range(page * limit - limit, min(len(buttons_game), page * limit)):
                    keyboard.add(buttons_game[i])
                if page != 1:
                    keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='info_Вернуться к предыдущей странице'))
                keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу',callback_data='info_Перейти на следующую страницу'))
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*50 видео игр! Выберите интерисующую вас игру:*', parse_mode='Markdown', reply_markup=keyboard)
        else:
            for button_game in buttons_game:
                if call.data == button_game.callback_data:
                    file = open('info_game.json', 'r+', encoding='utf-8')
                    info_game = json.load(file)
                    for game in info_game:
                        if game['Наименование'] == call.data.split('_')[1]:
                            url_game = game['Ссылка на информацию']
                            response = requests.get(url_game)
                            soup = BeautifulSoup(response.text, 'lxml')
                            mini_info_game = soup.select('div.mw-content-ltr.mw-parser-output > p')
                            name_game = soup.find('h1', class_='firstHeading mw-first-heading')
                            bot.send_message(call.from_user.id, text=('Название игры: ' + name_game.text))
                            bot.send_message(call.from_user.id, text=('Мини информация: ' + mini_info_game[0].text))
                            bot.send_message(call.from_user.id, text=game['Ссылка на информацию'])
            keyboard = types.InlineKeyboardMarkup()
            page += 1
            for i in range(page * limit - limit, min(len(buttons_game), page * limit)):
                keyboard.add(buttons_game[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='info_Вернуться к предыдущей странице'))
            if page * limit < len(buttons_game):
                keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='info_Перейти на следующую страницу'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*50 видео игр! Выберите интерисующую вас игру:*', parse_mode='Markdown', reply_markup=keyboard)

        if active_info == 'Транспорт':
            keyboard = types.InlineKeyboardMarkup()
            for i in range(page * limit - limit, min(len(buttons_auto), page * limit)):
                keyboard.add(buttons_auto[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='info_Вернуться к предыдущей странице'))
            if page * limit < len(buttons_auto):
                keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='info_Перейти на следующую страницу'))
            bot.send_message(call.from_user.id, '*50 модель машин! Выберите интерисующую вас модель машины:*', parse_mode='Markdown', reply_markup=keyboard)
        elif active_info == 'Перейти на следующую страницу':
            keyboard = types.InlineKeyboardMarkup()
            page += 1
            for i in range(page * limit - limit, min(len(buttons_auto), page * limit)):
                keyboard.add(buttons_auto[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='info_Вернуться к предыдущей странице'))
            if page * limit < len(buttons_auto):
                keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='info_Перейти на следующую страницу'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*50 модель машин! Выберите интерисующую вас модель машины:*', parse_mode='Markdown', reply_markup=keyboard)
        elif active_info == 'Вернуться к предыдущей странице':
            keyboard = types.InlineKeyboardMarkup()
            page -= 1
            for i in range(page * limit - limit, min(len(buttons_auto), page * limit)):
                keyboard.add(buttons_auto[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='info_Вернуться к предыдущей странице'))
            keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='info_Перейти на следующую страницу'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*50 машин! Выберите интерисующую вас модель машины:*', parse_mode='Markdown', reply_markup=keyboard)
        else:
            for button_auto in buttons_auto:
                if call.data == button_auto.callback_data:
                    file = open('info_transport.json', 'r+', encoding='utf-8')
                    info_transport = json.load(file)
                    for auto in info_transport:
                        if auto['Наименование'] == call.data:
                            url_auto = auto['Ссылка на информацию']
                            response = requests.get(url_auto)
                            soup = BeautifulSoup(response.text, 'lxml')
                            mini_info_auto = soup.select('div.mw-content-ltr.mw-parser-output > p')
                            name_auto = soup.find('h1', class_='firstHeading mw-first-heading')
                            bot.send_message(call.from_user.id, text=('Название игры: ' + name_auto.text))
                            bot.send_message(call.from_user.id, text=('Мини информация: ' + mini_info_auto[0].text))
                            bot.send_message(call.from_user.id, text=auto['Ссылка на информацию'])
            keyboard = types.InlineKeyboardMarkup()
            page += 1
            for i in range(page * limit - limit, min(len(buttons_auto), page * limit)):
                keyboard.add(buttons_auto[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='info_Вернуться к предыдущей странице'))
            if page * limit < len(buttons_auto):
                keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='info_Перейти на следующую страницу'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*50 модель машин! Выберите интерисующую вас модель машины:*', parse_mode='Markdown', reply_markup=keyboard)

bot.polling(none_stop = True, interval = 0)