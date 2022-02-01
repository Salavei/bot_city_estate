from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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


async def admin_keyboards_announcements(id_an) -> InlineKeyboardMarkup:
    """Одобрить и Отклонить объявления для админа"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'✅ Одобрить', callback_data=f'admin_start_an_{id_an}'),
                InlineKeyboardButton('❌ Отклонить', callback_data=f'admin_dell_an_{id_an}'),
            ]
        ]
    )
    return keyboard
