import telebot

bot = telebot.TeleBot("1083239056:AAHazdekMaGQZ5uReSWKh2J412g8378da-E")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, hoототлотолтлотлw are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()