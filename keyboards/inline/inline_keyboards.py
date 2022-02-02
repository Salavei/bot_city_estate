from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def keyboards_announcements_rent(id_an, allow) -> InlineKeyboardMarkup:
    """Остановка/Активация и Удаления объявлений для пользователя"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'{allow}', callback_data=f'rent_stop_start_an_{id_an}'),
                InlineKeyboardButton('❌ Удалить', callback_data=f'rent_dell_an_{id_an}'),
            ]
        ]
    )
    return keyboard



async def keyboards_announcements(id_an, allow) -> InlineKeyboardMarkup:
    """Остановка/Активация и Удаления объявлений для пользователя"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'{allow}', callback_data=f'stop_start_an_{id_an}'),
                InlineKeyboardButton('❌ Удалить', callback_data=f'dell_an_{id_an}'),
            ]
        ]
    )
    return keyboard


async def requests_keyboards_announcements(id_an) -> InlineKeyboardMarkup:
    """Оставить заявку на объявлении аренды"""
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'Оставить заявку', callback_data=f'rient_requests_an_{id_an}'),
            ]
        ]
    )
    return keyboard

async def sell_requests_keyboards_announcements(id_an) -> InlineKeyboardMarkup:
    """Оставить заявку на объявлении продажи"""
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'Оставить заявку', callback_data=f'soell_requests_an_{id_an}'),
            ]
        ]
    )
    return keyboard

async def make_choice_announcements(*args) -> InlineKeyboardMarkup:
    """инлайн при создании объявления"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton('Продажа', callback_data='sell'),
                InlineKeyboardButton('Аренда', callback_data='rent_create'),
            ]
        ]
    )
    return keyboard

async def choice_seller(*args) -> InlineKeyboardMarkup:
    """инлайн при создании объявления"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton('Собственник', callback_data='owner'),
                InlineKeyboardButton('Агент', callback_data='agent'),
            ]
        ]
    )
    return keyboard

#admin keyboard

async def rent_admin_keyboards_announcements(id_an) -> InlineKeyboardMarkup:
    """Одобрить и Отклонить объявления для админа"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'✅ Одобрить', callback_data=f'rent_admin_start_an_{id_an}'),
                InlineKeyboardButton('❌ Отклонить', callback_data=f'dell_rent_admin_an_{id_an}'),
            ]
        ]
    )
    return keyboard

async def sell_admin_keyboards_announcements(id_an) -> InlineKeyboardMarkup:
    """Одобрить и Отклонить объявления для админа"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'✅ Одобрить', callback_data=f'seeel_admin_start_an_{id_an}'),
                InlineKeyboardButton('❌ Отклонить', callback_data=f'an_admin_dell_{id_an}'),
            ]
        ]
    )
    return keyboard
