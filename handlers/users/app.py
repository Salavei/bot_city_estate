from main import *
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.funk_async import *


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not db.check_subscriber(message.from_user.id):
        db.add_subscriber(message.from_user.id)
    await message.answer(f'Привет, быстрее начни мной пользоваться!',
                         reply_markup=keyboard)


async def error(message: types.Message):
    await message.delete()


@dp.message_handler(content_types=['text'])
async def command_start_text(message: types.Message):
    data = {
        'Правила размещения и конфедициальность': give_keybord,
        'Сдается': show_all_rent,
        'Заявки на аренду': rental_requests,
        'Продается': show_all_sell,
        'Мои объявления продажи': show_all_my_sell,
        'Мои объявления аренды': show_all_my_rent,
        'Заявки на покупку': purchasing_request,
        'Политика конфеденциальности': konfendentsialnost,
        'Правила размещения': rule,
        'Сроки размещения': term,
        'Создать объявление': dell_up,
        '🔙': bot_start,

    }
    data_admin = {
        'Подтверждение Продажи': confirmation_of_sales,
        'Подтверждение Аренды': confirmation_of_rent,
    }
    await data.get(message.text, error)(message)
    await data_admin.get(message.text, error)(message)
