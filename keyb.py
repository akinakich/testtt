from imports import *

def get_menu():
	buttons1 = [
	[
		types.InlineKeyboardButton(text="К080ВТ", callback_data="К080ВТ"),
		types.InlineKeyboardButton(text="А507ВТ", callback_data="А507ВТ"),
		types.InlineKeyboardButton(text="М197АЕ", callback_data="М197АЕ"),
	],
	]
	keyboard1 = types.InlineKeyboardMarkup(inline_keyboard=buttons1)
	return keyboard1

def get_menu1():
	buttons1 = [
	[
		types.InlineKeyboardButton(text="🧮 Произвести рассчёт", callback_data="ras"),
		types.InlineKeyboardButton(text='❌Не-а', callback_data='dvas'),
	],
	]
	keyboard1 = types.InlineKeyboardMarkup(inline_keyboard=buttons1)
	return keyboard1