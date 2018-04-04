#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot
from telebot import types
import time
import subprocess
import config
import api
from apscheduler.schedulers.background import BackgroundScheduler

TOKEN = config.TOKEN
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "This bot helps you monitor supervisord status")


@bot.message_handler(commands=['run'])
def run_command(message):
    """
    Run command read from telegram messgae /run *
    """
    # pop_instance = subprocess.Popen(message.text[5:])
    # time.sleep(0.5)
    # pop_instance.kill()
    # output = pop_instance.stdout()
    output = subprocess.check_output(message.text[5:], shell=True, timeout=0.5)
    # output = message.text.split(' ')[1]
    bot.send_message(message.chat.id, output)
    print('handle ' + message.text[5:] + ' success!')


@bot.message_handler(commands=['getAllProcessInfo'])
def get_all_process_info(message):
    name = api.getAllProcessInfo()[0]['name']
    statename = api.getAllProcessInfo()[0]['statename']
    # description = api.getAllProcessInfo()[0]['description']
    bot.reply_to(message, name + '    ' + statename)


@bot.message_handler(commands=['getProcessInfo'])
def get_process_info(message):
    try:
        process_name = message.text[16:]
    except:
        bot.reply_to(message, 'Error')
    if process_name == '':
        bot.reply_to(message, 'Error! Please provide valid process name.')
    else:
        try:
            api_data = api.getProcessInfo(process_name)
        except:
            bot.reply_to(message, 'Error! Please provide valid process name.')
            return 
        name = api_data['name']
        statename = api_data['statename']
        description = api_data['description']
        bot.reply_to(message, name + '    ' + statename + '\n' + description)


if __name__ == '__main__':

    scheduler = BackgroundScheduler()
    scheduler.add_job(bot_warn,'interval', minutes=1)
    scheduler.start()
    bot.polling(none_stop=True)

