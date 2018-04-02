import telebot
# import os
import time
import subprocess
import config

TOKEN = config.TOKEN
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['run'])
def run_command(message):
    # pop_instance = subprocess.Popen(message.text[5:])
    # time.sleep(0.5)
    # pop_instance.kill()
    # output = pop_instance.stdout()
    output = subprocess.check_output(message.text[5:], shell=True, timeout=0.5)
    # output = message.text.split(' ')[1]
    bot.send_message(message.chat.id, output)
    print('handle ' + message.text[5:] + ' success!')

if __name__ == '__main__':
    bot.polling()

