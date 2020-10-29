import telebot as tb

token =  '***'
bot = tb.TeleBot(token)

array = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
result = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
table_one = array[0] + '  |  ' + array[1] + '  |  ' + array[2]
table_two = '  ' + array[3] + '  |  ' + array[4] + '  |  ' + array[5]
table_three = '  ' + array[6] + '  |  ' + array[7] + '  |  ' + array[8]
# ✕ 

keyboard = tb.types.ReplyKeyboardMarkup()
keyboard.add('0', '1', '2')
keyboard.add('3', '4', '5')
keyboard.add('6', '7', '8')

winner = [['00', '10', '20'], ['30', '40', '50'], 
['60', '70', '80'], ['00', '30', '60'], ['10', '40', '70'], 
['20', '50', '80'], ['00', '40', '80'], ['20', '40', '60']]

loser = [['01', '11', '21'], ['31', '41', '51'], 
['61', '71', '81'], ['01', '31', '61'], ['11', '41', '71'], 
['21', '51', '81'], ['01', '41', '81'], ['21', '41', '61']]

def win(array):
	for i in winner:
		if all(j in array for j in i):
			return True
	return False  

def lose(array):
	for i in loser:
		if all(j in array for j in i):
			return True
	return False

@bot.message_handler(commands=['start'])
def start_message(message):
	global array
	global result
	array = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
	result = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
	bot.send_message(message.chat.id, 'Играем')
	bot.send_message(message.chat.id, 
		'Начинаем игру:' + '\n\n' + '  ' + table_one + '\n' + 
		'---- + --- + ----' + '\n' + table_two + '\n' + 
		'---- + --- + ----' + '\n' + table_three + '\n\n'
		+ 'Делай первый ход!', reply_markup=keyboard)

@bot.message_handler(content_types='text')
def table_return(message):
	global result
	global array
	if len(result[int(message.text)]) == 2:
		bot.send_message(message.chat.id, 
			'Это поле уже занято, выберите другое')
	else:
		result[int(message.text)] += '0'
		array[int(message.text)] = '✕'
		table_one = array[0] + '  |  ' + array[1] + '  |  ' + array[2]
		table_two = '  ' + array[3] + '  |  ' + array[4] + '  |  ' + array[5]
		table_three = '  ' + array[6] + '  |  ' + array[7] + '  |  ' + array[8]
		counter = 0
		for i in result:
			if len(i) == 2:
				counter += 1
		if win(result):
			bot.send_message(message.chat.id, 
			'Вы сделали ход:' + '\n\n' + '  ' + table_one + '\n' + 
			'---- + --- + ----' + '\n' + table_two + '\n' + 
			'---- + --- + ----' + '\n' + table_three)
			bot.send_message(message.chat.id, 'Вы выиграли!')
			array = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
			result = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
			bot.send_message(message.chat.id, 
					'Хотите сыграть снова? Нажимай команду /start!')
		elif counter == 9:
			bot.send_message(message.chat.id, 
			'Вы сделали ход:' + '\n\n' + '  ' + table_one + '\n' + 
			'---- + --- + ----' + '\n' + table_two + '\n' + 
			'---- + --- + ----' + '\n' + table_three)
			bot.send_message(message.chat.id, 'Ничья!')
			array = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
			result = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
			bot.send_message(message.chat.id, 
					'Хотите сыграть снова? Нажимай команду /start!')
		else:
			count = 0
			while count < 9:
				if array[count] == '*':
					array[count] = 'O'
					result[count] += '1'
					break
				count += 1
			table_one = array[0] + '  |  ' + array[1] + '  |  ' + array[2]
			table_two = '  ' + array[3] + '  |  ' + array[4] + '  |  ' + array[5]
			table_three = '  ' + array[6] + '  |  ' + array[7] + '  |  ' + array[8]
			bot.send_message(message.chat.id, 
			'Вы сделали ход:' + '\n\n' + '  ' + table_one + '\n' + 
			'---- + --- + ----' + '\n' + table_two + '\n' + 
			'---- + --- + ----' + '\n' + table_three)
			if lose(result):
				bot.send_message(message.chat.id, 'Вы проиграли!')
				array = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
				result = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
				bot.send_message(message.chat.id, 
					'Хотите сыграть снова? Нажимайте команду /start!')
			else:
				bot.send_message(message.chat.id, 
				'Я тоже сделал ход:' + '\n\n' + '  ' + table_one + 
				'\n' + '---- + --- + ----' + '\n' + table_two + '\n' 
				+ '---- + --- + ----' + '\n' + table_three + 
				'\n\n' + 'Продолжай!', reply_markup=keyboard)

bot.polling(none_stop=True)
