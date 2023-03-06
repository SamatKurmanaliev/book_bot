import polka
import telebot
import wikipedia
from gtts import gTTS


LANGUAGE_CODE='ru'
count=0
bot = telebot.TeleBot("5811096072:AAHmXceu0-rikQ_4lAiBTn8E9Yv26jZcMIs", parse_mode=None)
wikipedia.set_lang(LANGUAGE_CODE)
dictt={'привет':'Привет',
'как это работает?':"введите название книги и я дам информацию об этой книге",
'как тебя зовут?':'александрия',
'где ты?':'у тебя на компе',
}
@bot.message_handler(commands=['start', 'help',])
def send_welcome(message):
	bot.reply_to(message, "Привет я бот, введите название книги")

@bot.message_handler()
def echo_all(message):
	flag=0
	if message.text.lower() in dictt.keys():
		tts=gTTS(dictt[message.text],lang=LANGUAGE_CODE)
		tts.save('sample.mp3')
		audio=open('sample.mp3','rb')
		bot.send_audio(message.chat.id,audio)
		flag=1
	for book in polka.books():
		assert isinstance(book, polka.Book)
		if book.title.lower()==message.text.lower():
			bot.send_message(message.chat.id,f'{book.description}. Это произведение: {book.questions[0].answer}. Год издания: {book.year.start}')
			flag=1
			break
	if flag==0:
		bot.send_message(message.chat.id,'мы не нашли информацию об этой книге')
		
	
print('Бот стартует!')
bot.infinity_polling()
