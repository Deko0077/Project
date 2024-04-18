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

buttons_sport = [
            types.InlineKeyboardButton(text='Биатлон', callback_data='Биатлон'),
            types.InlineKeyboardButton(text='Бобслей', callback_data='Бобслей'),
            types.InlineKeyboardButton(text='Горнолыжный спорт', callback_data='Горнолыжный спорт'),
            types.InlineKeyboardButton(text='Кёрлинг', callback_data='Кёрлинг'),
            types.InlineKeyboardButton(text='Лыжное двоеборье', callback_data='Лыжное двоеборье'),
            types.InlineKeyboardButton(text='Лыжные гонки', callback_data='Лыжные гонки'),
            types.InlineKeyboardButton(text='Прыжки на лыжах', callback_data='Прыжки на лыжах'),
            types.InlineKeyboardButton(text='Санный спорт', callback_data='Санный спорт'),
            types.InlineKeyboardButton(text='Скелетон', callback_data='Скелетон'),
            types.InlineKeyboardButton(text='Сноуборд', callback_data='Сноуборд'),
            types.InlineKeyboardButton(text='Фигурное катание', callback_data='Фигурное катание'),
            types.InlineKeyboardButton(text='Фристайл', callback_data='Фристайл'),
            types.InlineKeyboardButton(text='Хоккей', callback_data='Хоккей'),
            types.InlineKeyboardButton(text='Шорт - трек', callback_data='Шорт - трек'),
            types.InlineKeyboardButton(text='Баскетбол', callback_data='Баскетбол'),
            types.InlineKeyboardButton(text='Бейсбол', callback_data='Бейсбол'),
            types.InlineKeyboardButton(text='Бокс', callback_data='Бокс'),
            types.InlineKeyboardButton(text='Вело спорт', callback_data='Вело спорт'),
            types.InlineKeyboardButton(text='Водное поло', callback_data='Водное поло'),
            types.InlineKeyboardButton(text='Волейбол', callback_data='Волейбол'),
            types.InlineKeyboardButton(text='Гандбол', callback_data='Гандбол'),
            types.InlineKeyboardButton(text='Гольф', callback_data='Гольф'),
            types.InlineKeyboardButton(text='Гребля на байдарках', callback_data='Гребля на байдарках'),
            types.InlineKeyboardButton(text='Гребный слалом', callback_data='Гребный слалом'),
            types.InlineKeyboardButton(text='Гребной спорт', callback_data='Гребной спорт'),
            types.InlineKeyboardButton(text='Дзюдо', callback_data='Дзюдо'),
            types.InlineKeyboardButton(text='Бадминтон', callback_data='Бадминтон'),
            types.InlineKeyboardButton(text='Каратэ', callback_data='Каратэ'),
            types.InlineKeyboardButton(text='Конный спорт', callback_data='Конный спорт'),
            types.InlineKeyboardButton(text='Лёгкая атлетика', callback_data='Лёгкая атлетика'),
            types.InlineKeyboardButton(text='Настольный теннис', callback_data='Настольный теннис'),
            types.InlineKeyboardButton(text='Парусный спорт', callback_data='Парусный спорт'),
            types.InlineKeyboardButton(text='Плавание', callback_data='Плавание'),
            types.InlineKeyboardButton(text='Пляжный волейбол', callback_data='Пляжный волейбол'),
            types.InlineKeyboardButton(text='Прыжки в воду', callback_data='Прыжки в воду'),
            types.InlineKeyboardButton(text='Прыжки на батуте', callback_data='Прыжки на батуте'),
            types.InlineKeyboardButton(text='Регби', callback_data='Регби'),
            types.InlineKeyboardButton(text='Сёрфинг', callback_data='Сёрфинг'),
            types.InlineKeyboardButton(text='Скалолазание', callback_data='Скалолазание'),
            types.InlineKeyboardButton(text='Скейтбординг', callback_data='Скейтбординг'),
            types.InlineKeyboardButton(text='Современное пятиборье', callback_data='Современное пятиборье'),
            types.InlineKeyboardButton(text='Софтбол', callback_data='Софтбол'),
            types.InlineKeyboardButton(text='Стрельба', callback_data='Стрельба'),
            types.InlineKeyboardButton(text='Стрельба из лука', callback_data='Стрельба из лука'),
            types.InlineKeyboardButton(text='Теннис', callback_data='Теннис'),
            types.InlineKeyboardButton(text='Триатлон', callback_data='Триатлон'),
            types.InlineKeyboardButton(text='Тхэквондо', callback_data='Тхэквондо'),
            types.InlineKeyboardButton(text='Тяжёлая атлетика', callback_data='Тяжёлая атлетика'),
            types.InlineKeyboardButton(text='Фехтование', callback_data='Фехтование'),
            types.InlineKeyboardButton(text='Футбол', callback_data='Футбол')
        ]

buttons_game = [
            types.InlineKeyboardButton(text='CS2', callback_data='CS2'),
            types.InlineKeyboardButton(text='Valorant', callback_data='Valorant'),
            types.InlineKeyboardButton(text='Undertale', callback_data='Undertale'),
            types.InlineKeyboardButton(text='Deltarune', callback_data='Deltarune'),
            types.InlineKeyboardButton(text='Minecraft', callback_data='Minecraft'),
            types.InlineKeyboardButton(text='Terraria', callback_data='Terraria'),
            types.InlineKeyboardButton(text='Grand The Auto V', callback_data='Grand The Auto V'),
            types.InlineKeyboardButton(text='Geometry Dash', callback_data='Geometry Dash'),
            types.InlineKeyboardButton(text='Brawl Stars', callback_data='Brawl Stars'),
            types.InlineKeyboardButton(text='PUBG: Battlegrounds', callback_data='PUBG: Battlegrounds'),
            types.InlineKeyboardButton(text='Cyberpunk 2077', callback_data='Cyberpunk 2077'),
            types.InlineKeyboardButton(text='Standoff2', callback_data='Standoff2'),
            types.InlineKeyboardButton(text='Forza Horizon 5', callback_data='Forza Horizon 5'),
            types.InlineKeyboardButton(text='Forza Horizon 4', callback_data='Forza Horizon 4'),
            types.InlineKeyboardButton(text='Horizon Zero Dawn', callback_data='Horizon Zero Dawn'),
            types.InlineKeyboardButton(text='Davil May Cry 5', callback_data='Davil May Cry 5'),
            types.InlineKeyboardButton(text='Cuphead', callback_data='Cuphead'),
            types.InlineKeyboardButton(text='Goat Simulator', callback_data='Goat Simulator'),
            types.InlineKeyboardButton(text='FIFA', callback_data='FIFA'),
            types.InlineKeyboardButton(text='Five Nights at Freddys', callback_data='Five Nights at Freddys'),
            types.InlineKeyboardButton(text='Apex Legends', callback_data='Apex Legends'),
            types.InlineKeyboardButton(text='Fall Guys', callback_data='Fall Guys'),
            types.InlineKeyboardButton(text='Rocket League', callback_data='Rocket League'),
            types.InlineKeyboardButton(text='Among Us', callback_data='Among Us'),
            types.InlineKeyboardButton(text='Poppy Playtime', callback_data='Poppy Playtime'),
            types.InlineKeyboardButton(text='S.T.A.L.K.E.R', callback_data='S.T.A.L.K.E.R'),
            types.InlineKeyboardButton(text='SCP: Secret Laboratory', callback_data='SCP: Secret Laboratory'),
            types.InlineKeyboardButton(text='eFootbal™', callback_data='eFootbal™'),
            types.InlineKeyboardButton(text='The Witcher', callback_data='The Witcher'),
            types.InlineKeyboardButton(text='Diablo', callback_data='Diablo'),
            types.InlineKeyboardButton(text='DOOM', callback_data='DOOM'),
            types.InlineKeyboardButton(text='Mortal Combat', callback_data='Mortal Combat'),
            types.InlineKeyboardButton(text='Takken', callback_data='Takken'),
            types.InlineKeyboardButton(text='The Last of Us', callback_data='The Last of Us'),
            types.InlineKeyboardButton(text='The Walking Dead', callback_data='The Walking Dead'),
            types.InlineKeyboardButton(text='Resident Evil', callback_data='Resident Evil'),
            types.InlineKeyboardButton(text='Dying Light', callback_data='Dying Light'),
            types.InlineKeyboardButton(text='Unrecord', callback_data='Unrecord'),
            types.InlineKeyboardButton(text='Gran Turismo', callback_data='Gran Turismo'),
            types.InlineKeyboardButton(text='Смута', callback_data='Смута'),
            types.InlineKeyboardButton(text='Hpgwards Legacy', callback_data='Hpgwards Legacy'),
            types.InlineKeyboardButton(text='Elden Ring', callback_data='Elden Ring'),
            types.InlineKeyboardButton(text='The elder scrolls V Skyrim', callback_data='The elder scrolls V Skyrim'),
            types.InlineKeyboardButton(text='Final Fantasy', callback_data='Final Fantasy'),
            types.InlineKeyboardButton(text='The Legend of Zelda', callback_data='The Legend of Zelda'),
            types.InlineKeyboardButton(text='Genshin Inpact', callback_data='Genshin Inpact'),
            types.InlineKeyboardButton(text='Marvels Spider Man', callback_data='Marvels Spider Man'),
            types.InlineKeyboardButton(text='Dota 2', callback_data='Dota 2'),
            types.InlineKeyboardButton(text='Hollow Knight', callback_data='Hollow Knight'),
            types.InlineKeyboardButton(text='Call f Duty: Warzon', callback_data='Call f Duty: Warzon')
]


buttons_auto = [
            types.InlineKeyboardButton(text='Audi A4', callback_data='Audi A4'),
            types.InlineKeyboardButton(text='Audi S5', callback_data='Audi S5'),
            types.InlineKeyboardButton(text='Audi RS6', callback_data='Audi RS6'),
            types.InlineKeyboardButton(text='Audi A7 Sportback', callback_data='Audi A7 Sportback'),
            types.InlineKeyboardButton(text='Audi E-Tron', callback_data='Audi E-Tron'),
            types.InlineKeyboardButton(text='BMW M8', callback_data='BMW M8'),
            types.InlineKeyboardButton(text='BMW 4', callback_data='BMW 4'),
            types.InlineKeyboardButton(text='BMW X5', callback_data='BMW X5'),
            types.InlineKeyboardButton(text='BMW X7', callback_data='BMW X7'),
            types.InlineKeyboardButton(text='BMW 8 Кабриолет', callback_data='BMW 8 Кабриолет'),
            types.InlineKeyboardButton(text='Mercedec-Benz AMG GT', callback_data='Mercedec-Benz AMG GT'),
            types.InlineKeyboardButton(text='Mercedec-Benz CLS', callback_data='Mercedec-Benz CLS'),
            types.InlineKeyboardButton(text='Mercedec-Benz A', callback_data='Mercedec-Benz A'),
            types.InlineKeyboardButton(text='Mercedec-Benz G AMG', callback_data='Mercedec-Benz G AMG'),
            types.InlineKeyboardButton(text='Mercedec-Benz GLA', callback_data='Mercedec-Benz GLA'),
            types.InlineKeyboardButton(text='Ford Mustag', callback_data='Ford Mustag'),
            types.InlineKeyboardButton(text='Ford Fiesta', callback_data='Ford Fiesta'),
            types.InlineKeyboardButton(text='Ford Puma', callback_data='Ford Puma'),
            types.InlineKeyboardButton(text='Ford Ranger Raptor', callback_data='Ford Ranger Raptor'),
            types.InlineKeyboardButton(text='Ford Mustang Mach-E', callback_data='Ford Mustang Mach-E'),
            types.InlineKeyboardButton(text='Nissan Z', callback_data='Nissan Z'),
            types.InlineKeyboardButton(text='Nissan GT-R', callback_data='Nissan GT-R'),
            types.InlineKeyboardButton(text='Nissan Juke', callback_data='Nissan Juke'),
            types.InlineKeyboardButton(text='Nissan Navara', callback_data='Nissan Navara'),
            types.InlineKeyboardButton(text='Nissan Murano', callback_data='Nissan Murano'),
            types.InlineKeyboardButton(text='Tesla Model 3', callback_data='Tesla Model 3'),
            types.InlineKeyboardButton(text='Tesla Model S', callback_data='Tesla Model S'),
            types.InlineKeyboardButton(text='Tesla Model X', callback_data='Tesla Model X'),
            types.InlineKeyboardButton(text='Tesla Cybertruck', callback_data='Tesla Cybertruck'),
            types.InlineKeyboardButton(text='Lamborghini Urus S', callback_data='Lamborghini Urus S'),
            types.InlineKeyboardButton(text='Lamborghini Huracan Steratto', callback_data='Lamborghini Huracan Steratto'),
            types.InlineKeyboardButton(text='Lamborghini Huracan Tecnica', callback_data='Lamborghini Huracan Tecnica'),
            types.InlineKeyboardButton(text='Lamborghini Urus Performante', callback_data='Lamborghini Urus Performante'),
            types.InlineKeyboardButton(text='Lamborghini Huracan EVO Sryder', callback_data='Lamborghini Huracan EVO Sryder'),
            types.InlineKeyboardButton(text='Ferrari Purosangue', callback_data='Ferrari Purosangue'),
            types.InlineKeyboardButton(text='Ferrari 812 Superfast', callback_data='Ferrari 812 Superfast'),
            types.InlineKeyboardButton(text='Ferrari Roma', callback_data='Ferrari Roma'),
            types.InlineKeyboardButton(text='Ferrari SF90 Stradale', callback_data='Ferrari SF90 Stradale'),
            types.InlineKeyboardButton(text='Ferrari 812 GTS', callback_data='Ferrari 812 GTS'),
            types.InlineKeyboardButton(text='LADA Nila Travel', callback_data='LADA Nila Travel'),
            types.InlineKeyboardButton(text='LADA Vesta', callback_data='LADA Vesta'),
            types.InlineKeyboardButton(text='LADA Granta Cross', callback_data='LADA Granta Cross'),
            types.InlineKeyboardButton(text='LADA Granta Sport', callback_data='LADA Granta Sport'),
            types.InlineKeyboardButton(text='LADA Vesta Cross', callback_data='LADA Vesta Cross'),
            types.InlineKeyboardButton(text='Opel Crossland', callback_data='Opel Crossland'),
            types.InlineKeyboardButton(text='Opel Corsa', callback_data='Opel Corsa'),
            types.InlineKeyboardButton(text='Opel Astra', callback_data='Opel Astra'),
            types.InlineKeyboardButton(text='Opel Insignia', callback_data='Opel Insignia'),
            types.InlineKeyboardButton(text='Opel Mokka', callback_data='Opel Mokka'),
            types.InlineKeyboardButton(text='Bentley Continental GT', callback_data='Bentley Continental GT')
]


@bot.message_handler(content_types=['text'])
def get_message(message):

    if message.text == '/start':

        bot.set_my_commands(
            commands=[
                types.BotCommand('/start', 'Запуск бота'),
                types.BotCommand('/startquest', 'Начать квест'),
                types.BotCommand('/information', 'Информация'),
                types.BotCommand('/help', 'Помощь')
            ],
            scope=types.BotCommandScopeChat(message.chat.id)
        )

        bot.send_message(message.from_user.id, text='''
*Привет!*
            
Тематик - бот помощник. Он поможет вам определиться с выбором во многих темах, в которых вы возможно не разбираетесь. 
Этот бот представлять возможность вам в выборе ответа на предложенные темы. 
Мы стараемся уточнить ваш выбор задавая вопросы с предложанными на них ответы по выбранной теме.
Так же вы можете  узнать много интерестных фактов о данной теме. 
*Наш бот не несет ответственности за ваш выбор и не несёт ни какого сексуального характера (18+)*.
            
*Желаем тебе удачи!*
            
*Здесь вы можете выполнить задачи как:*
            
1. Разобраться в темах исходя из своих предпочтений, отвечая на заданные вопросы.
2. Посмотреть краткую информацию многих первых 50-ти вещей.
3. Узнать много интересного.
4. Разобраться в своих предпчтениях.
5. Повесильться!
            
Чтобы начать пользоваться ботов просто напишите команду из списка ниже.
            
*Список команд:*
            
/start - запуск бота
/startquest - начать квест
/information - крткая информации о вещах
/help - Помощь
            
*Разработчики:*
            
- @DekoSans - Данила Демченко
- @daniilkiin - Данил Лаптев
            
*Если Бот вам не отвечает, перезапустите его командой /start или обратитесь к разработчикам данного бота.*
            
*Удачи!*''', parse_mode='Markdown')
        print(message.from_user.id, message.text)

    elif message.text == '/startquest':

        keyboard = types.InlineKeyboardMarkup()

        button1 = types.InlineKeyboardButton(text='Спорт', callback_data='Спорт')
        button2 = types.InlineKeyboardButton(text='Видео игры', callback_data='Видео игры')
        button3 = types.InlineKeyboardButton(text='Транспорт', callback_data='Транспорт')


        keyboard.add(button1, button2, button3)
        bot.send_message(message.from_user.id, '*Выберите тему:*', parse_mode='Markdown', reply_markup=keyboard)
        print(message.from_user.id, message.text)

    elif message.text == '/information':

        keyboard = types.InlineKeyboardMarkup()

        themes_buttons = [
            types.InlineKeyboardButton(text='Спорт', callback_data='theme_Спорт'),
            types.InlineKeyboardButton(text='Видео игры', callback_data='theme_Видео игры'),
            types.InlineKeyboardButton(text='Транспорт', callback_data='theme_Транспорт')
        ]
        for i in range(len(themes_buttons)):
            keyboard.add(themes_buttons[i])
        bot.send_message(message.from_user.id, '*Выберите интерисующую вас тему:*', parse_mode='Markdown', reply_markup=keyboard)
        print(message.from_user.id, message.text)

    elif message.text == '/help':
        bot.send_message(message.from_user.id, text='''
        Если Бот вам не отвечает, перезапустите его командой /start или обратитесь к разработчикам данного бота.
        
        *Разработчики:*
        -@DanilaDemchenko - Данила Демченко
        -@daniilkiin - Данил Лаптев''', parse_mode='Markdown')
        print(message.from_user.id, message.text)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global page, active_theme, limit

    if call.data.startswith('theme'):
        active_theme = call.data.split('_')[1]

    if active_theme == 'Спорт':
        for button in buttons_sport:
            if call.data == button.callback_data:
                file = open('info_sport.json', 'r', encoding='utf-8')
                info_sport = json.load(file)
                for sport in info_sport:
                    if sport['Наименование'] == call.data:
                        bot.send_message(call.from_user.id, text=sport['Наименование'] + ':')
                        
                        bot.send_message(call.from_user.id, text=sport['Ссылка на информацию'])
        if call.data == 'Перейти на следующую страницу':
            keyboard = types.InlineKeyboardMarkup()
            page += 1
            for i in range(page * limit - limit, min(len(buttons_sport), page * limit)):
                keyboard.add(buttons_sport[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='Вернуться к предыдущей странице'))
            if page * limit < len(buttons_sport):
                keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='Перейти на следующую страницу'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*50 видов спорта! Выберите интерисующий вид спорта:*', parse_mode='Markdown', reply_markup=keyboard)
        elif call.data == 'Вернуться к предыдущей странице':
            keyboard = types.InlineKeyboardMarkup()
            page -= 1
            for i in range(page * limit - limit, min(len(buttons_sport), page * limit)):
                keyboard.add(buttons_sport[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='Вернуться к предыдущей странице'))
            keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='Перейти на следующую страницу'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*50 видов спорта! Выберите интерисующий вид спорта:*', parse_mode='Markdown', reply_markup=keyboard)
        else:
            keyboard = types.InlineKeyboardMarkup()
            for i in range(limit):
                keyboard.add(buttons_sport[i])
            keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='Перейти на следующую страницу'),)
            bot.send_message(call.from_user.id, '*50 видов спорта! Выберите интерисующий вид спорта:*', parse_mode='Markdown', reply_markup=keyboard)


    if active_theme == 'Видео игры':
        for button in buttons_game:
            if call.data == button.callback_data:
                file = open('info_game.json', 'r', encoding='utf-8')
                info_game = json.load(file)
                for game in info_game:
                    if game['Наименование'] == call.data:
                        bot.send_message(call.from_user.id, text=game['Наименование'] + ':')

                        bot.send_message(call.from_user.id, text=game['Ссылка на информацию'])
        if call.data == 'Перейти на следующую страницу':
            keyboard = types.InlineKeyboardMarkup()
            page += 1
            for i in range(page * limit - limit, min(len(buttons_game), page * limit)):
                keyboard.add(buttons_game[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='Вернуться к предыдущей странице'))
            if page * limit < len(buttons_game):
                keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='Перейти на следующую страницу'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*50 видео игр! Выберите интерисующую вас игру:*', parse_mode='Markdown', reply_markup=keyboard)
        elif call.data == 'Вернуться к предыдущей странице':
            keyboard = types.InlineKeyboardMarkup()
            page -= 1
            for i in range(page * limit - limit, min(len(buttons_game), page * limit)):
                keyboard.add(buttons_game[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='Вернуться к предыдущей странице'))
            keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу',callback_data='Перейти на следующую страницу'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*50 видео игр! Выберите интерисующую вас игру:*', parse_mode='Markdown', reply_markup=keyboard)
        else:
            keyboard = types.InlineKeyboardMarkup()
            for i in range(limit):
                keyboard.add(buttons_game[i])
            keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='Перейти на следующую страницу'),)
            bot.send_message(call.from_user.id, '*50 видео игр! Выберите интерисующую вас игру:*', parse_mode='Markdown', reply_markup=keyboard)


    if active_theme == 'Транспорт':
        for button in buttons_auto:
            if call.data == button.callback_data:
                file = open('info_transport.json', 'r', encoding='utf-8')
                info_transport = json.load(file)
                for auto in info_transport:
                    if auto['Наименование'] == call.data:
                        bot.send_message(call.from_user.id, text=auto['Наименование'] + ':')

                        bot.send_message(call.from_user.id, text=auto['Ссылка на информацию'])
        if call.data == 'Перейти на следующую страницу':
            keyboard = types.InlineKeyboardMarkup()
            page += 1
            for i in range(page * limit - limit, min(len(buttons_auto), page * limit)):
                keyboard.add(buttons_auto[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='Вернуться к предыдущей странице'))
            if page * limit < len(buttons_auto):
                keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='Перейти на следующую страницу'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*50 модель машин! Выберите интерисующую вас модель машины:*', parse_mode='Markdown', reply_markup=keyboard)
        elif call.data == 'Вернуться к предыдущей странице':
            keyboard = types.InlineKeyboardMarkup()
            page -= 1
            for i in range(page * limit - limit, min(len(buttons_auto), page * limit)):
                keyboard.add(buttons_auto[i])
            if page != 1:
                keyboard.add(types.InlineKeyboardButton(text='Вернуться к предыдущей странице', callback_data='Вернуться к предыдущей странице'))
            keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='Перейти на следующую страницу'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*50 машин! Выберите интерисующую вас модель машины:*', parse_mode='Markdown', reply_markup=keyboard)
        else:
            keyboard = types.InlineKeyboardMarkup()
            for i in range(limit):
                keyboard.add(buttons_auto[i])
            keyboard.add(types.InlineKeyboardButton(text='Перейти на следующую страницу', callback_data='Перейти на следующую страницу'),)
            bot.send_message(call.from_user.id, '*50 модель машин! Выберите интерисующую вас модель машины:*', parse_mode='Markdown', reply_markup=keyboard)
bot.polling(none_stop = True, interval = 0)

