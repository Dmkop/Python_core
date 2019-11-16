#!/usr/bin/python3.6

import telebot
import requests
from telebot.types import Message
from pprint import pprint
from datetime import datetime

TOKEN = '755209205:AAEuhzhXN0-hU-8K0DYXfs2woNU1qj7p4G0'
YEAR = datetime.now().year
MONTH = datetime.now().month
DAY = datetime.now().day
HOUR = datetime.now().hour

def privat_url():
	BASE_URL = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={DAY}.{MONTH}.{YEAR}'
	data = requests.get(BASE_URL)
	return data.json()['exchangeRate']


exchange_data = privat_url()
bot = telebot.TeleBot(TOKEN)
pprint(exchange_data)
#pprint(old_exchange_data)

@bot.message_handler(commands = ['start'])
def start(message: Message):
	with open('/home/dmkop/python_projects/SoftServe/My_project/Telebot/start', mode = 'r') as information:
		txt_inf = information.read()
		bot.reply_to(message, txt_inf)


@bot.message_handler(commands = ['help'])
def help_data(message: Message):
	with open('/home/dmkop/python_projects/SoftServe/My_project/Telebot/help', mode = 'r') as help:
		txt_help = help.read()
		bot.reply_to(message, txt_help)


@bot.message_handler(commands = ['info'])
def info_data(message: Message):
	with open('/home/dmkop/python_projects/SoftServe/My_project/Telebot/info', mode = 'r') as information:
		txt_inf = information.read()
		bot.reply_to(message, txt_inf)


@bot.message_handler(content_types = ['text'])
@bot.edited_message_handler(content_types = ['text'])
def currency_code(message: Message):
	for item in range(1, len(exchange_data)):

		if message.text.upper() == exchange_data[item]['currency']:

			if message.text.upper() == 'EUR' or message.text.upper() == 'USD' or message.text.upper() == 'CHF' or message.text.upper() == 'CZK':
				bot.reply_to(message, 'The purchase rate equel: {purchase}\n' 
				' and the selling rate equel: {sale}'.format(purchase = exchange_data[item]['purchaseRate'], 
				sale = exchange_data[item]['saleRate']))
				return

			elif message.text.upper() == 'CZK' or message.text.upper() == 'GBR' or message.text.upper() == 'PLZ' or message.text.upper() == 'RUB':
				bot.reply_to(message, 'The purchase rate equel: {purchase}\n' 
				' and the selling rate equel: {sale}'.format(purchase = exchange_data[item]['purchaseRate'], 
				sale = exchange_data[item]['saleRate']))
				return

			else:
				bot.reply_to(message, 'The purchase rate at the Ukrainian National Bank equal: {purchase:.2f}\n '
				'and the selling rate at the Ukrainian National Bank equal: {sale:.2f}'.format(purchase = exchange_data[item]['purchaseRateNB'], 
				sale = exchange_data[item]['saleRateNB']))
				return

	return bot.reply_to(message, "I can't handle this data yet")

bot.polling(timeout=60)