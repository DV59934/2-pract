import requests
import telebot
from telebot import types
import random
from collections import defaultdict

token = '8172132829:AAF3lyYCqqm4KUfgz09VMNWM837dd16Oy-s'
bot = telebot.TeleBot(token)

caught_pokemons = defaultdict(dict)


def pokeball():
    return "https://i.pinimg.com/736x/e2/7b/7d/e27b7d18b01ae4765133f4aec4aaf61d.jpg"


def get_random_pokemon():
    pokemon_id = random.randint(1, 151)
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    data = response.json()
    return {
        'name': data['name'],
        'image': data['sprites']['front_default'],
        'id': pokemon_id,
        'height': data['height'],
        'weight': data['weight'],
        'types': [t['type']['name'] for t in data['types']],
        'mood': get_random_mood(),
        'hunger': random.randint(0, 100)  # Добавляем уровень сытости
    }


def get_random_mood():
    moods = [
        "Радость", "Грусть", "Умиротворение", "Спокойствие",
        "Тревожность", "Злость", "Брезгливость", "Апатия",
        "Ностальгия", "Влюбленность", "Страх", "Зависть", "Стыд"
    ]
    return random.choice(moods)

def get_drink():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    return keyboard

def get_food_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Яблоко", "Орех", "Ягода")
    keyboard.row("Приманка", "Корм для покемонов", "Суши")
    keyboard.row("Не кормить", "Назад")
    return keyboard


keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row("Кинь покебол!")
keyboard.row("Поймать покемона!")
keyboard.row("Мой покемон")
keyboard.row("Узнай настроение своего покемона")
keyboard.row("Покормить покемона")
keyboard.row("Напоить покемона")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Привет! Я Покемон-бот!\n"
                     "Выбери действие:",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Кинь покебол!")
def send_pokeball(message):
    pokeball_url = pokeball()
    bot.send_photo(message.chat.id, pokeball_url, caption="Покебол летит!")


@bot.message_handler(func=lambda message: message.text == "Поймать покемона!")
def send_pokemon(message):
    user_id = message.from_user.id

    if user_id in caught_pokemons:
        bot.send_message(message.chat.id,
                         f"У тебя уже есть покемон! Это {caught_pokemons[user_id]['name'].capitalize()}.")
        return

    try:
        pokemon = get_random_pokemon()
        caught_pokemons[user_id] = pokemon

        caption = (f"Вы поймали: {pokemon['name'].capitalize()}!\n"
                   f"ID: {pokemon['id']}\n"
                   f"Тип: {', '.join(pokemon['types']).capitalize()}\n"
                   f"Рост: {pokemon['height'] / 10} м\n"
                   f"Вес: {pokemon['weight'] / 10} кг\n")

        bot.send_photo(message.chat.id, pokemon['image'], caption=caption)
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, "Не удалось поймать покемона, попробуйте ещё раз!")


@bot.message_handler(func=lambda message: message.text == "Мой покемон")
def show_my_pokemon(message):
    user_id = message.from_user.id

    if user_id not in caught_pokemons:
        bot.send_message(message.chat.id, "У тебя ещё нет покемона! Нажми 'Поймать покемона!'")
        return

    pokemon = caught_pokemons[user_id]
    caption = (f"Твой покемон: {pokemon['name'].capitalize()}!\n"
               f"ID: {pokemon['id']}\n"
               f"Тип: {', '.join(pokemon['types']).capitalize()}\n"
               f"Рост: {pokemon['height'] / 10} м\n"
               f"Вес: {pokemon['weight'] / 10} кг\n")

    bot.send_photo(message.chat.id, pokemon['image'], caption=caption)


@bot.message_handler(func=lambda message: message.text == "Узнай настроение своего покемона")
def send_mood(message):
    user_id = message.from_user.id

    if user_id not in caught_pokemons:
        bot.send_message(message.chat.id, "У тебя ещё нет покемона! Нажми 'Поймать покемона!'")
        return

    pokemon = caught_pokemons[user_id]
    bot.send_message(message.chat.id,
                     f"Настроение твоего покемона {pokemon['name'].capitalize()}: {pokemon['mood']}")


@bot.message_handler(func=lambda message: message.text == "Покормить покемона")
def send_food_menu(message):
    user_id = message.from_user.id

    if user_id not in caught_pokemons:
        bot.send_message(message.chat.id, "У тебя ещё нет покемона! Нажми 'Поймать покемона!'")
        return

    bot.send_message(message.chat.id,
                     "Выбери чем покормить покемона:",
                     reply_markup=get_food_keyboard())

@bot.message_handler(func=lambda message: message.text == "Напоить покемона")
def send_drink(message):
    user_id = message.from_user.id

    if user_id not in caught_pokemons:
        bot.send_message(message.chat.id, "У тебя ещё нет покемона! Нажми 'Поймать покемона!'")
        return
    bot.send_message(message.chat.id,
                     f"Ты напоил покемона!",
                     reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text in ["Яблоко", "Орех", "Ягода",
                                                           "Приманка", "Корм для покемонов",
                                                           "Суши", "Не кормить", "Назад"])
def handle_food_choice(message):
    user_id = message.from_user.id
    pokemon = caught_pokemons.get(user_id)

    if not pokemon:
        bot.send_message(message.chat.id, "У тебя нет покемона!")
        return

    if message.text == "Назад":
        bot.send_message(message.chat.id, "Главное меню:", reply_markup=keyboard)
        return
    elif message.text == "Не кормить":
        bot.send_message(message.chat.id, "Ты решил не кормить покемона.", reply_markup=keyboard)
        return
    bot.send_message(message.chat.id,
    f"Ты покормил {pokemon['name'].capitalize()} {message.text.lower()}\n",
    reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id,
                     "Используй кнопки:\n"
                     "'Кинь покебол!'\n"
                     "'Поймать покемона!'\n"
                     "'Мой покемон'\n"
                     "'Узнай настроение своего покемона'\n"
                     "'Покормить покемона'",
                     "'Напоить покемона'",
                     reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
