from aiogram import types
from main import db
from keyboards.default.markup import keyboards_create, keyboard_rule_konfendentsialnost
from keyboards.inline.inline_keyboards import keyboards_announcements

data_placed = {
    True: 'Агент',
    False: 'Собственник',
}

data_allow = {
    True: 'Остановить',
    False: 'Активировать',
}

async def give_keybord(message: types.Message):
    await message.reply(text='Правила размещения и конфедициальность', reply_markup=keyboard_rule_konfendentsialnost)

# main_user_funk_ --- Когда смотришь свое
async def show_all_my_rent(message: types.Message):
    if db.show_all_my_announcements_sell(message.from_user.id):
        for un in db.show_all_my_announcements_sell(message.from_user.id):
            id_an, price, number_of_rooms, street, rent_description, phone, placed, photo, date_time, allow, _, _ = un
            await message.answer(
                text=f'\nСтоимость аренды:{price}\nКолличество комнат:{number_of_rooms}\nАдрес:{street}\nОписание:{rent_description}'
                     f'\nНомер телефона:{phone}\nКто сдает:{data_placed.get(placed)}\nФотография:{photo}\nДата публикации:{date_time}', reply_markup=await keyboards_announcements(id_an, data_allow.get(allow)))
    else:
        await message.answer(text='Обьявлений на сдачу нет')

# main_user_funk_ --- Когда смотришь чужое
async def show_all_rent(message: types.Message):
    if db.show_all_announcements_rent():
        for un in db.show_all_announcements_rent():
            _, price, number_of_rooms, street, rent_description, phone, placed, photo, date_time, _, _, _ = un
            await message.answer(
                text=f'\nСтоимость аренды:{price}\nКолличество комнат:{number_of_rooms}\nАдрес:{street}\nОписание:{rent_description}'
                     f'\nНомер телефона:{phone}\nКто сдает:{data_placed.get(placed)}\nФотография:{photo}\nДата публикации:{date_time}')
    else:
        await message.answer(text='Обьявлений на сдачу нет')


async def show_all_sell(message: types.Message):
    if db.show_all_announcements_sell():
        for un in db.show_all_announcements_sell():
            _, price, number_of_rooms, street, rent_description, phone, placed, photo, date_time, _, _, _ = un
            await message.answer(
                text=f'Цена:{price}\nКолличество комнат:{number_of_rooms}\nАдрес:{street}\nОписание:{rent_description}'
                     f'\nНомер телефона:{phone}\nКто сдает:{data_placed.get(placed)}\nФотография:{photo}\nДата публикации:{date_time}')
    else:
        await message.answer(text='Обьявлений на аренду нет')

async def rental_requests(): pass


async def purchasing_request(): pass


# second_user_funk

async def konfendentsialnost(message: types.Message):
    await message.answer(text='Политики размещения и конфедициальность: Тут скоро будет текст')


async def rule(message: types.Message):
    await message.answer(
        text='1)Размещать существующее 2)За публикуемые обьявления администрации не несет отвутственность')


async def term(message: types.Message):
    await message.answer(text='Сроки размещения зависят от администратора')


async def dell_up(message: types.Message):
    await message.reply(text='Создание объявления', reply_markup=keyboards_create)


# admin

async def confirmation_of_sales(message: types.Message):
    db.confirm_announcements_sell_admin()


async def confirmation_of_rent():
    db.confirm_announcements_rent_admin()
