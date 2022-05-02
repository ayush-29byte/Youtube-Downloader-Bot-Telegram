#packages required
import telebot
import requests
import os
import json, youtube_dl

token = os.version['5389927031:AAEUaJ7ZzKgYHjyCSSDlTfmEm2ioKmdrI64'] #enter your unique telegram bot token

#initializing the downloader

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

#initializing the bot

bot = telebot.TeleBot(token)
x = bot.get_me()
print(x)

#commands and handling of the bot

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome user")

#youtube link

@bot.message_handler(commands=['ytdl'])
def down(msg):
    args = msg.text.split()[1]
    try:
        with ydl:
            result = ydl.extract_info(args, download=False)

        if 'entries' in result:
            video = result['entries'][0]
        else:
            video=result

        for i in video['formats']:
            link = '<a href=\"' + i['url'] + '\">' + 'link' + '</a>'

            if i.get('format_note'):
                bot.reply_to(msg, 'Quality- ' + i['format_note'] + ': ' + link, parse_mode='HTML')
            else:
                bot.reply_to(msg, link, parse_mode='HTML', disable_notification=True)
    except:
        bot.reply_to(msg, 'This can\'t be downloaded by me :(')

#start the bot
bot.polling()