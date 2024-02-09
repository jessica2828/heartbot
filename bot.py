from typing import Final
import os
import telebot
from telebot import types

# BOT_TOKEN = os.environ.get('BOT_TOKEN')

BOT_TOKEN: Final = '6523328797:AAExFPVaC6qcwOAZW2gXBY40fUFyt32_MPs'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Big at Heart! I am HeartBot, how can I help you today?\n\nPlease click on the menu to see the available commands and their functions.")

@bot.message_handler(commands=['enrol'])
def name_handler(message):
    text = "Please enter your first name:"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, age_handler)

def age_handler(message):
    text = "Please enter your last name: "                
    sent_msg = bot.send_message(
        message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_msg, gender_handler)
    
def gender_handler(message):
    name = message.text
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)  # Create a ReplyKeyboardMarkup
    markup.add(types.KeyboardButton('Male'), types.KeyboardButton('Female'))
    bot.send_message(message.chat.id, f"Hi {name}, welcome to Big at Heart. Please select your gender below to continue: ", reply_markup=markup)


@bot.message_handler(commands=['attendance'])
def attendance_handler(message):
    text = "Your attendance for this volunteering session has been marked. Thank you for volunteering with Big at Heart."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    # bot.register_next_step_handler(sent_msg, age_handler)

events = [
    {
        'name': 'Big At Heart Event 1',
        'date': '1 to 7 February 2024',
        'time': '9am-4pm',
        'location': 'National University of Singapore',
        'roles': 'Volunteers',
        'requirements': '\n- Must be 18 and above\n- Must have prior experience working with children',
        'responsibilities': '\n- Tutor students from disadvantaged backgrounds'
    },
    {
        'name': 'Big At Heart Event 2',
        'date': '14 February 2024',
        'time': '1.30pm-3.30pm',
        'location': 'Nanyang Technological University',
        'roles': 'Volunteers, Drivers',
        'requirements': '\n- Must be 18 and above\n- Must not have any health conditions',
        'responsibilities': '\n-Collect food donations, sort and pack items, and deliver to HDB blocks'
    }
]

# Define the message for the /events command
def get_events_message():
    message = "Here are the volunteering events available at Big at Heart:\n\n"
    for event in events:
        message += f"📅 Event: {event['name']}\n"
        message += f"   Date: {event['date']}\n"
        message += f"   Time: {event['time']}\n"
        message += f"   Location: {event['location']}\n"
        message += f"   Roles: {event['roles']}\n"
        message += f"   Requirements: {event['requirements']}\n"
        message += f"   Responsibilities: {event['responsibilities']}\n\n"
    return message

# Define a message handler for the /events command
@bot.message_handler(commands=['events'])
def send_events(message):
    bot.reply_to(message, get_events_message(), parse_mode='Markdown')


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()