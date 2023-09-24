from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def markup_inline_choose_a_subject():
    markup = InlineKeyboardMarkup(row_width=4)
    button1 = InlineKeyboardButton(text="Алгебра", callback_data="Алгебра_sub")
    button2 = InlineKeyboardButton(text="Биология", callback_data="Биология_sub")
    button3 = InlineKeyboardButton(text="География", callback_data="География_sub")
    button4 = InlineKeyboardButton(text="Геометрия", callback_data="Геометрия_sub")
    button5 = InlineKeyboardButton(text="Иностранный язык", callback_data="Иностранный язык_sub")
    button6 = InlineKeyboardButton(text="Информатика", callback_data="Информатика_sub")
    button7 = InlineKeyboardButton(text="История", callback_data="История_sub")
    button8 = InlineKeyboardButton(text="Литература", callback_data="Литература_sub")
    button9 = InlineKeyboardButton(text="Обществознание", callback_data="Обществознание_sub")
    button10 = InlineKeyboardButton(text="Русский язык", callback_data="Русский язык_sub")
    button11 = InlineKeyboardButton(text="Физика", callback_data="Физика_sub")
    button12 = InlineKeyboardButton(text="Химия", callback_data="Химия_sub")
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
               button12)
    return markup


def markup_button_start():
    markup = ReplyKeyboardMarkup(row_width=2)
    button1 = KeyboardButton('Внести дз')
    button2 = KeyboardButton('Я что то сделал')
    button3 = KeyboardButton('Показать доступное дз')
    button4 = KeyboardButton('Отмена')
    markup.add(button1, button2, button3, button4)
    return markup


def markup_inline_choose_a_day():
    markup = InlineKeyboardMarkup(row_width=3)
    button1 = InlineKeyboardButton(text="Понедельник", callback_data="Понедельник_day")
    button2 = InlineKeyboardButton(text="Вторник", callback_data="Вторник_day")
    button3 = InlineKeyboardButton(text="Среда", callback_data="Среда_day")
    button4 = InlineKeyboardButton(text="Четверг", callback_data="Четверг_day")
    button5 = InlineKeyboardButton(text="Пятница", callback_data="Пятница_day")
    button6 = InlineKeyboardButton(text="Суббота", callback_data="Суббота_day")
    markup.add(button1, button2, button3, button4, button5, button6)
    return markup