from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import telebot
import hashlib
import base64

bot = telebot.TeleBot("5995779364:AAGDnl_Wk1UDWiJVyXDOb6KGJ9raTJf7RvM")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup(row_width=2)
    itembtn6 = InlineKeyboardButton('تشفير Base16', callback_data='base16_encode')
    itembtn7 = InlineKeyboardButton('فك تشفير Base16', callback_data='base16_decode')
    itembtn8 = InlineKeyboardButton('تشفير Base32', callback_data='base32_encode')
    itembtn9 = InlineKeyboardButton('فك تشفير Base32', callback_data='base32_decode')
    markup.add(itembtn6, itembtn7, itembtn8, itembtn9)
    bot.send_message(message.chat.id, "مرحبًا بك في روبوت التشفير / فك التشفير. الرجاء تحديد خيار: @hussien_pyrogram", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    
    
    if call.data == 'base16_encode':
        bot.send_message(call.message.chat.id, "الرجاء إدخال النص الذي تريد تشفيره باستخدام Base16:")
        bot.register_next_step_handler(call.message, base16_encode)
    elif call.data == 'base16_decode':
        bot.send_message(call.message.chat.id, "الرجاء إدخال النص الذي تريد فك تشفيره باستخدام Base16:")
        bot.register_next_step_handler(call.message, base16_decode)
    elif call.data == 'base32_encode':
        bot.send_message(call.message.chat.id, "الرجاء إدخال النص الذي تريد تشفيره باستخدام Base32:")
        bot.register_next_step_handler(call.message, base32_encode)
    elif call.data == 'base32_decode':
        bot.send_message(call.message.chat.id, "الرجاء إدخال النص الذي تريد فك تشفيره باستخدام Base32:")
        bot.register_next_step_handler(call.message, base32_decode)


def base16_encode(message):
    text = message.text
    encoded_text = base64.b16encode(text.encode('utf-8')).decode('utf-8')
    bot.send_message(message.chat.id, f"Encoded text: {encoded_text}")

def base16_decode(message):
    text = message.text
    decoded_text = base64.b16decode(text.encode('utf-8')).decode('utf-8')
    bot.send_message(message.chat.id, f"Decoded text: {decoded_text}")

def base32_encode(message):
    text = message.text
    encoded_text = base64.b32encode(text.encode('utf-8')).decode('utf-8')
    bot.send_message(message.chat.id, f"Encoded text: {encoded_text}")

def base32_decode(message):
    text = message.text
    decoded_text = base64.b32decode(text.encode('utf-8')).decode('utf-8')
    bot.send_message(message.chat.id, f"Decoded text: {decoded_text}")


bot.polling()
