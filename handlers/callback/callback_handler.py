from main import *
from aiogram import types


###Оставить заявку на объявлении

@dp.callback_query_handler(lambda call: 'requests_an_' in call.data)
async def requests_an_user(call: types.CallbackQuery):
    #тут будет то, куда будет идти заявка
    await call.message.answer(text="Заявка отправлена")

###Пользователь активирует и деактивирует объявления
@dp.callback_query_handler(lambda call: 'rent_stop_start_an_' in call.data)
async def stop_start_an_rent_user(call: types.CallbackQuery):
    print(call.data.split('_')[-1])
    db.confirm_announcements_rent_user(call.data.split('_')[-1], not db.start_my_announcements_rent(call.data.split('_')[-1]))
    await call.message.edit_text(text="☑️")


@dp.callback_query_handler(lambda call: 'stop_start_an_' in call.data)
async def stop_start_an_sell_user(call: types.CallbackQuery):
    print(call.data.split('_')[-1])
    db.confirm_announcements_sell_user(call.data.split('_')[-1], not db.start_my_announcements_sell(call.data.split('_')[-1]))
    await call.message.edit_text(text="☑️")

#Пользователь удаляет объявления

@dp.callback_query_handler(lambda call: 'dell_an_' in call.data)
async def user_an_sell_dell(call: types.CallbackQuery):
    #пока не буду делать функцию удаления
    await call.message.edit_text(text="☑️Удалено")

######Админ удаляет объявления
@dp.callback_query_handler(lambda call: 'dell_rent_admin_an_' in call.data)
async def admin_an_rent_dell(call: types.CallbackQuery):
    db.dell_an_rent_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️Отклонено")

@dp.callback_query_handler(lambda call: 'an_admin_dell_' in call.data)
async def admin_an_sell_dell(call: types.CallbackQuery):
    db.dell_an_sell_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️Отклонено")

#######Админ одобряет объявления
@dp.callback_query_handler(lambda call: 'seeel_admin_start_an_' in call.data)
async def admin_start_an_sell(call: types.CallbackQuery):
    print('sell', call.data.split('_')[-1])
    db.confirm_announcements_sell_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️Одобрено️")

@dp.callback_query_handler(lambda call: 'rent_admin_start_an_' in call.data)
async def admin_start_an_rent(call: types.CallbackQuery):
    print('rent', call.data.split('_')[-1])
    db.confirm_announcements_rent_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️Одобрено")
