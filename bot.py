import telebot as tb
token = '***'

bot = tb.TeleBot(token)

keyboard = tb.types.ReplyKeyboardMarkup(False, True)
keyboard.row('Я?', 'Я..', 'Давай по новой')

keyboard_new = tb.types.ReplyKeyboardMarkup(False, True)
keyboard_new.row('Не хрень!', 'Згода, хрень..', 'Давай по новой')

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, '''
    Реши загадку Жака Фреско. Хто?''', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def messages(message):
	if message.text.lower() == 'дороу':
		bot.reply_to(message, 'Йооой')
		bot.send_sticker(message.chat.id,
			'CAACAgIAAxkBAAI_4l-YihSgfBbRtIesssE6ujM0A4O5AAInAAOX09Ahyt4tLlthDkIbBA')
	elif message.text == 'Не хрень!':
		bot.send_sticker(message.chat.id, 
			'CAACAgIAAxkBAAI_31-YiXvZ2SPPEJJhMsbfLyHkDxbIAAImAAOX09Ah_-hnXcm5zBAbBA')
		bot.send_message(message.chat.id, 
			'Тогда решай загадку. Хто?')
	elif message.text == 'Згода, хрень..':
		bot.send_sticker(message.chat.id,
			'CAACAgIAAxkBAAI_5V-YisJSuwKUHA8KoJrs_zx7UNStAAIRAAOX09AhSvjoaMmb-CsbBA')
		bot.send_message(message.chat.id, 
			'''Понимаааааю... Исправляйся. Вопрос тот же. Хто?''')
	elif message.text == 'Давай по новой':
		start_message(message)
	else:
		bot.send_message(message.chat.id, 'Хрень пишешь',
			reply_markup=keyboard_new)


bot.polling(none_stop=True)
