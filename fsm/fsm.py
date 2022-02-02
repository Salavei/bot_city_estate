from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from main import *
import datetime
from keyboards.inline.inline_keyboards import *


class FSMrequest_sell(StatesGroup):
    name_request = State()
    number_request = State()


@dp.callback_query_handler(lambda c: 'soell_requests_an_' in c.data)
async def request_sell_start(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['id_an_sell'] = callback_query.data.split('_')[-1]
    await FSMrequest_sell.name_request.set()
    await callback_query.message.edit_text('Введите Ваше имя:')


@dp.message_handler(state=FSMrequest_sell.name_request)
async def request_sell_load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMrequest_sell.next()
    await message.answer('☎️ Номер телефона:')


@dp.message_handler(lambda message: not message.text[1:].isdigit(), state=FSMrequest_sell.number_request)
async def request_sell_load_phone_invalid(message: types.Message):
    return await message.reply("⚠️ Номер должен быть формата: +375297642930!!")


@dp.message_handler(lambda message: message.text[1:].isdigit(), state=FSMrequest_sell.number_request)
async def request_sell_load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await message.answer('✅ Заявка оставлена')
    db.add_request_sell(data['id_an_sell'], data['phone'], data['name'])
    await state.finish()




class FSMrequest_rent(StatesGroup):
    name_request = State()
    number_request = State()


@dp.callback_query_handler(lambda c: 'rient_requests_an_' in c.data)
async def request_rent_start(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['id_an_rent'] = callback_query.data.split('_')[-1]
    await FSMrequest_rent.name_request.set()
    await callback_query.message.edit_text('Введите Ваше имя:')


@dp.message_handler(state=FSMrequest_rent.name_request)
async def request_rent_load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMrequest_rent.next()
    await message.answer('☎️ Номер телефона:')


@dp.message_handler(lambda message: not message.text[1:].isdigit(), state=FSMrequest_rent.number_request)
async def request_rent_load_phone_invalid(message: types.Message):
    return await message.reply("⚠️ Номер должен быть формата: +375297642930!!")


@dp.message_handler(lambda message: message.text[1:].isdigit(), state=FSMrequest_rent.number_request)
async def request_rent_load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await message.answer('✅ Заявка оставлена')
    db.add_request_rent(data['id_an_rent'], data['phone'], data['name'])
    await state.finish()


class FSMsell(StatesGroup):
    price = State()
    number_of_rooms = State()
    street = State()
    rent_description = State()
    phone = State()
    placed = State()
    photo = State()
    print('Start sell')


@dp.callback_query_handler(lambda c: 'sell' in c.data)
async def sell_start(callback_query: types.CallbackQuery):
    await FSMsell.price.set()
    await callback_query.message.edit_text('Введите стоимость:')


@dp.message_handler(state=FSMsell.price)
async def write_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await FSMsell.next()
    await message.answer('Введие колличество комнат:')


@dp.message_handler(state=FSMsell.number_of_rooms)
async def write_number_of_rooms(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_of_rooms'] = message.text
    await FSMsell.next()
    await message.answer('Введите район и адрес:')


@dp.message_handler(state=FSMsell.street)
async def write_street(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['street'] = message.text
    await FSMsell.next()
    await message.answer('Описание:')


@dp.message_handler(state=FSMsell.rent_description)
async def write_rent_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['rent_description'] = message.text
    await FSMsell.next()
    await message.answer('Ваш номер телефона:')


@dp.message_handler(lambda message: not message.text[1:].isdigit(), state=FSMsell.phone)
async def write_phone_invalid(message: types.Message):
    return await message.answer("⚠️ Номер должен быть формата: +375297642930!!")


@dp.message_handler(lambda message: message.text[1:].isdigit(), state=FSMsell.phone)
async def write_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await FSMsell.next()
    await message.answer('Выберите кто выкладывает объявление:', reply_markup=await choice_seller())


@dp.callback_query_handler(lambda call: "owner" or "agent" in call.data, state=FSMsell.placed)
async def write_placed(call: types.CallbackQuery, state: FSMContext):
    choice = {
        'owner': True,
        'agent': False,
    }
    async with state.proxy() as data:
        data['placed'] = choice.get(call.data)
    await FSMrent.next()
    await call.message.answer('Загрузите фото квартиры:')


@dp.message_handler(content_types=['photo'], state=FSMsell.photo)
async def write_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMsell.next()
    await message.answer('✅ Обьявление добавлено')
    db.add_announcements_sell(data['price'], data['number_of_rooms'], data['street'], data['rent_description'],
                              data['phone'], data['photo'], placed=data['placed'],
                              date_time=str(datetime.datetime.now()),
                              tg_id=message.from_user.id, )
    await state.finish()


class FSMrent(StatesGroup):
    price = State()
    number_of_rooms = State()
    street = State()
    rent_description = State()
    phone = State()
    placed = State()
    photo = State()
    print('Start rent')


@dp.callback_query_handler(lambda c: 'rent_create' in c.data)
async def rent_start(callback_query: types.CallbackQuery):
    await FSMrent.price.set()
    await callback_query.message.edit_text('Введите стоимость:')


@dp.message_handler(state=FSMrent.price)
async def rent_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await FSMrent.next()
    await message.answer('Тип комнаты(проходная, отдельная, подселение):')


@dp.message_handler(state=FSMrent.number_of_rooms)
async def rent_number_of_rooms(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_of_rooms'] = message.text
    await FSMrent.next()
    await message.answer('Введите район и адрес:')


@dp.message_handler(state=FSMrent.street)
async def rent_street(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['street'] = message.text
    await FSMrent.next()
    await message.answer('Описание:')


@dp.message_handler(state=FSMrent.rent_description)
async def rent_rent_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['rent_description'] = message.text
    await FSMrent.next()
    await message.answer('Ваш номер телефона:')


@dp.message_handler(lambda message: not message.text[1:].isdigit(), state=FSMrent.phone)
async def rent_phone_invalid(message: types.Message):
    return await message.answer("⚠️ Номер должен быть формата: +375297642930!!")


@dp.message_handler(lambda message: message.text[1:].isdigit(), state=FSMrent.phone)
async def rent_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await FSMrent.next()
    await message.answer('Выберите кто выкладывает объявление:', reply_markup=await choice_seller())


@dp.callback_query_handler(lambda call: "owner" or "agent" in call.data, state=FSMrent.placed)
async def rent_placed(call: types.CallbackQuery, state: FSMContext):
    choice = {
        'owner': True,
        'agent': False,
    }
    async with state.proxy() as data:
        data['placed'] = choice.get(call.data)
    await FSMrent.next()
    await call.message.answer('Загрузите фото комнаты:')


@dp.message_handler(content_types=['photo'], state=FSMrent.photo)
async def rent_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMrent.next()
    await message.answer('✅ Обьявление добавлено')
    db.add_announcements_rent(data['price'], data['number_of_rooms'], data['street'], data['rent_description'],
                              data['phone'], data['photo'], placed=data['placed'],
                              date_time=str(datetime.datetime.now()),
                              tg_id=message.from_user.id, )
    await state.finish()
