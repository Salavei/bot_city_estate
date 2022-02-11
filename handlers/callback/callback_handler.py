from main import *
from aiogram import types


###Оставить заявку на объявлении

@dp.callback_query_handler(lambda call: 'soell_requests_an_' in call.data)
async def requests_an_user_soell(call: types.CallbackQuery):
    db.add_request_sell(id_an_sell=call.data.split('_')[-1],
                        name_request=db.take_my_info(call.from_user.id)[0])
    await call.message.answer(text="Заявка отправлена")


@dp.callback_query_handler(lambda call: 'rient_requests_an_' in call.data)
async def requests_an_user_rent(call: types.CallbackQuery):
    db.add_request_rent(id_an_rent=call.data.split('_')[-1],
                        name_request=db.take_my_info(call.from_user.id)[0])
    await call.message.answer(text="Заявка отправлена")


###Пользователь активирует и деактивирует объявления
@dp.callback_query_handler(lambda call: 'rent_stop_start_an_' in call.data)
async def stop_start_an_rent_user(call: types.CallbackQuery):
    db.confirm_announcements_rent_user(call.data.split('_')[-1],
                                       not db.start_my_announcements_rent(call.data.split('_')[-1]))
    await call.message.edit_text(text="☑️")


@dp.callback_query_handler(lambda call: 'stop_start_an_' in call.data)
async def stop_start_an_sell_user(call: types.CallbackQuery):
    db.confirm_announcements_sell_user(call.data.split('_')[-1],
                                       not db.start_my_announcements_sell(call.data.split('_')[-1]))
    await call.message.edit_text(text="☑️")


# Пользователь удаляет объявления

@dp.callback_query_handler(lambda call: 'ddd_rent_dell_an_' in call.data)
async def user_an_rent_dell(call: types.CallbackQuery):
    db.dell_an_rent_user(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️Удалено")


@dp.callback_query_handler(lambda call: 'ssssssdell_an_' in call.data)
async def user_an_sell_dell_sell(call: types.CallbackQuery):
    db.dell_an_sell_user(call.data.split('_')[-1])
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
    db.confirm_announcements_sell_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️Одобрено️")


@dp.callback_query_handler(lambda call: 'rent_admin_start_an_' in call.data)
async def admin_start_an_rent(call: types.CallbackQuery):
    db.confirm_announcements_rent_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️Одобрено")
