from main import db, bot
from keyboards.default.markup import *
from keyboards.inline.inline_keyboards import *

data_placed = {
    False: 'Агент',
    True: 'Собственник',
}

data_allow = {
    True: 'Остановить',
    False: 'Активировать',
}


async def give_keybord(message: types.Message):
    await message.reply(text='Правила размещения и конфедициальность', reply_markup=keyboard_rule_konfendentsialnost)


# main_user_funk_ --- Когда смотришь свое
async def show_all_my_sell(message: types.Message):
    if db.show_all_my_announcements_sell(message.from_user.id):
        for un in db.show_all_my_announcements_sell(message.from_user.id):
            id_an, price, number_of_rooms, street, rent_description, phone, placed, photo, date_time, allow, _, _ = un
            await message.answer_photo(photo=photo)
            await message.answer(text=f'Цена: {price}\nКолличество комнат: {number_of_rooms}\nАдрес: {street}\nОписание: {rent_description}'
                                         f'\nНомер телефона: {phone}\nКто сдает: {data_placed.get(placed)}\nДата публикации: {str(date_time)[0:-7]}', reply_markup=await keyboards_announcements(id_an, allow=data_allow.get(allow)))
    else:
        await message.answer(text='Вы еще не создали объявлений по продаже')


async def show_all_my_rent(message: types.Message):
    if db.show_all_my_announcements_rent(message.from_user.id):
        for un in db.show_all_my_announcements_rent(message.from_user.id):
            id_an, price, number_of_rooms, street, rent_description, phone, placed, photo, date_time, allow, _, _ = un
            await message.answer_photo(photo=photo)
            await message.answer(text=f'Стоимость аренды: {price}\nТип комнаты: {number_of_rooms}\nАдрес: {street}\nОписание: {rent_description}'
                                         f'\nНомер телефона: {phone}\nКто сдает: {data_placed.get(placed)}\nДата публикации: {str(date_time)[0:-7]}',
                                 reply_markup=await keyboards_announcements_rent(id_an, allow=data_allow.get(allow)))
    else:
        await message.answer(text='Вы еще не создали объявлений по аренде')


# main_user_funk_ --- Когда смотришь чужое
async def show_all_rent(message: types.Message):
    if db.show_all_announcements_rent():
        for un in db.show_all_announcements_rent():
            id_an, price, number_of_rooms, street, rent_description, phone, placed, photo, date_time, _, _, _ = un
            await message.answer_photo(photo=photo)
            await message.answer(text=f'Стоимость аренды: {price}\nКолличество комнат: {number_of_rooms}\nАдрес: {street}\nОписание: {rent_description}'
                                         f'\nНомер телефона: {phone}\nКто сдает: {data_placed.get(placed)}\nДата публикации: {str(date_time)[0:-7]}',
                                 reply_markup=await requests_keyboards_announcements(id_an))
    else:
        await message.answer(text='Обьявлений на аренду нет')



async def show_all_sell(message: types.Message):
    if db.show_all_announcements_sell():
        for un in db.show_all_announcements_sell():
            id_an, price, number_of_rooms, street, rent_description, phone, placed, photo, date_time, _, _, _ = un
            await message.answer_photo(photo=photo)
            await message.answer(text=f'Цена: {price}\nКолличество комнат: {number_of_rooms}\nАдрес: {street}\nОписание: {rent_description}'
                     f'\nНомер телефона: {phone}\nКто сдает: {data_placed.get(placed)}\nДата публикации: {str(date_time)[0:-7]}',
                 reply_markup=await sell_requests_keyboards_announcements(id_an))
    else:
        await message.answer(text='Обьявлений на сдачу нет')


async def rental_requests(message: types.Message):
    if db.show_request_rent(message.from_user.id):
        for unp in db.show_request_rent(message.from_user.id):
            for un in db.show_all_my_announcements_rent_request(unp[2]):
                await message.answer(text=f'📍Имя: {unp[1]}\nНомер телефона: {unp[0]}\n\nОбъявление:\n{un[3]}\n{un[4]}')
    else:
        await message.answer(text='Запросов не продажу нет')

async def purchasing_request(message: types.Message):
    if db.show_request_sell(message.from_user.id):
        for unp in db.show_request_sell(message.from_user.id):
            for un in db.show_all_my_announcements_sell_request(unp[2]):
                await message.answer(text=f'📍Имя: {unp[1]}\nНомер телефона: {unp[0]}\n\nОбъявление:\n{un[3]}\n{un[4]}')
    else:
        await message.answer(text='Запросов не продажу нет')
# second_user_funk

async def konfendentsialnost(message: types.Message):
    with open('utils/konfendentsialnost', 'r', encoding='UTF-8') as term_text:
        await message.answer(text=term_text.read())


async def rule(message: types.Message):
    with open('utils/rule', 'r', encoding='UTF-8') as term_text:
        await message.answer(text=term_text.read())


async def term(message: types.Message):
    with open('utils/term', 'r', encoding='UTF-8') as term_text:
        await message.answer(text=term_text.read())


async def dell_up(message: types.Message):
    await message.reply(text='Создание объявления', reply_markup=await make_choice_announcements())






# admin
async def confirmation_of_sales(message: types.Message):
    if db.admin_all_announcements_sell():
        for un in db.admin_all_announcements_sell():
            id_an, price, number_of_rooms, street, rent_description, phone, placed, photo, date_time, _, _, _ = un
            await message.answer_photo(photo=photo)
            await message.answer(
                text=f'Цена: {price}\nКолличество комнат: {number_of_rooms}\nАдрес: {street}\nОписание: {rent_description}'
                     f'\nНомер телефона: {phone}\nКто сдает: {data_placed.get(placed)}\nДата публикации: {str(date_time)[0:-7]}',
                reply_markup=await sell_admin_keyboards_announcements(id_an))
    else:
        await message.answer(text='Обьявлений для подтверждений на аренду нет')
        # db.confirm_announcements_sell_admin()


async def confirmation_of_rent(message: types.Message):
    if db.admin_all_announcements_rent():
        for un in db.admin_all_announcements_rent():
            id_an, price, number_of_rooms, street, rent_description, phone, placed, photo, date_time, _, _, _ = un
            await message.answer_photo(photo=photo)
            await message.answer(
                text=f'Стоимость аренды: {price}\nКолличество комнат: {number_of_rooms}\nАдрес: {street}\nОписание: {rent_description}'
                     f'\nНомер телефона: {phone}\nКто сдает: {data_placed.get(placed)}\nДата публикации: {str(date_time)[0:-7]}',
                reply_markup=await rent_admin_keyboards_announcements(id_an))
    else:
        await message.answer(text='Обьявлений для подтверждений на сдачу нет')
    # db.confirm_announcements_rent_admin()
