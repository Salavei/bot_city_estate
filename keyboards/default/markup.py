from aiogram.types import KeyboardButton
from aiogram import types

# user_button
btn_rule_konfendentsialnost = KeyboardButton("Правила размещения и конфедициальность")
btn_konfendentsialnost = KeyboardButton("Политика конфеденциальности")
btn_rule = KeyboardButton("Правила размещения")
btn_term = KeyboardButton("Сроки размещения")
btn_dell_up = KeyboardButton("Создать объявление")
btn_back = KeyboardButton("🔙")

keyboard_rule_konfendentsialnost = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_rule_konfendentsialnost.add(btn_konfendentsialnost, btn_rule, btn_term, btn_dell_up, btn_back)
#user_button_dell_up
btn_create_an = KeyboardButton('Создать объявление')
btn_back_create_an = KeyboardButton("🔙")
keyboards_create = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboards_create.add(btn_create_an, btn_back_create_an)
# main_button
btn_is_given = KeyboardButton("Сдается")
btn_requisition_arend = KeyboardButton("Заявки на аренду")
btn_sell = KeyboardButton("Продается")
btn_requisition_buy = KeyboardButton("Заявки на покупку")

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(btn_rule_konfendentsialnost, btn_is_given, btn_requisition_arend, btn_sell, btn_requisition_buy)

# Button_Admin
btn_confirming_sell = KeyboardButton("Подтверждение Продажи")
btn_confirming_arend = KeyboardButton("Подтверждение Аренды")

keyboard_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_admin.add(btn_confirming_sell, btn_confirming_arend)
