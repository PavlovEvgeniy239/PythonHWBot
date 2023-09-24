from aiogram import types
from create_bot import bot
from Keyboards import buttons
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from DataBase import home_work_db

class States(StatesGroup):
    state_chose_a_sub = State()
    state_chose_a_day = State()
    state_write_home_work = State()
    state_chose_delete_home_work = State()

async def close(m: types.Message, state: FSMContext):
    await state.reset_state()


async def process_start_command(m: types.Message):
    my_chat_id = m.from_user.id
    my_text = "Привет, это дз бот."
    await bot.send_message(chat_id=my_chat_id, text=my_text, reply_markup=buttons.markup_button_start())


async def process_help_command(m: types.Message):
    my_chat_id = m.from_user.id
    my_text = 'круто, ты решил сделать дз'
    await bot.send_message(chat_id=my_chat_id, text=my_text, reply_markup=buttons.markup_button_start())


async def chose_a_sub(m: types.Message):
    my_chat_id = m.from_user.id
    my_text = "Выбери предмет"
    await bot.send_message(chat_id=my_chat_id, text=my_text, reply_markup=buttons.markup_inline_choose_a_subject())
    await States.state_chose_a_sub.set()


async def chose_a_day(call: types.CallbackQuery, state: FSMContext):
    my_chat_id = call.from_user.id
    subject = call.data[:-4]
    await bot.send_message(chat_id=my_chat_id, text= 'Выбери день, на который ты хочешь добавить дз по предмету '+ subject, reply_markup=buttons.markup_inline_choose_a_day())
    async with state.proxy() as data:
        data['state_chose_a_sub'] = subject
    await States.state_chose_a_day.set()


async def write_your_home_work(call: types.CallbackQuery, state: FSMContext):
    my_chat_id = call.from_user.id
    day = call.data[:-4]
    await bot.send_message(chat_id=my_chat_id, text= 'Напиши дз, которое ты хочешь внести на день ' + day)
    async with state.proxy() as data:
        data['state_chose_a_day'] = day
    await States.state_write_home_work.set()


async def accept_homework(m: types.Message, state: FSMContext):
    my_chat_id = m.from_user.id
    my_text = m.text
    async with state.proxy() as data:
        data['state_write_home_work'] = my_text
    async with state.proxy() as data:
        await home_work_db.sql_add_row(data)
    await bot.send_message(chat_id=my_chat_id, text='Дз успешно добавлено!')
    await state.reset_state()



async def show_all_home_work(m: types.Message):
    my_chat_id = m.from_user.id
    my_text = await home_work_db.sql_show_all_table()
    for task in my_text:
        await bot.send_message(chat_id=my_chat_id, text=f'{task[0]}\n {task[1]} {task[2]}\n {task[3]}')


async def chose_delete_home_work(m: types.Message):
    my_chat_id = m.from_user.id
    await bot.send_message(chat_id=my_chat_id, text='Отправь номер выполненного дз')
    my_text = await home_work_db.sql_show_all_table()
    for task in my_text:
        await bot.send_message(chat_id=my_chat_id, text=f'{task[0]}\n {task[1]} {task[2]}\n {task[3]}')
    await States.state_chose_delete_home_work.set()


async def delete_home_work(m: types.Message, state: FSMContext):
    my_chat_id = m.from_user.id
    my_text = m.text
    my_id = await home_work_db.take_id_from_table()
    if my_text.isdigit():
        k = my_text+","
        if k in str(my_id):
            await home_work_db.delete_from_table(my_text)
            await bot.send_message(chat_id=my_chat_id, text='Дз успешно удалено, продолжайте в том же духе')
            await state.reset_state()
        else:
            await bot.send_message(chat_id=my_chat_id, text='Введено число не из диапозона, попробуй ещё раз')
    else:
        await bot.send_message(chat_id=my_chat_id, text='Введён неверный формат номера, попробуй ещё раз')


async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    print(msg)
    print(msg.entities[0].url)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(close, text='Отмена', state="*")
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(chose_a_sub, text='Внести дз')
    dp.register_callback_query_handler(chose_a_day, lambda call: call.data[-3:] == 'sub', state=States.state_chose_a_sub)
    dp.register_callback_query_handler(write_your_home_work, lambda call: call.data[-3:] == 'day', state=States.state_chose_a_day)
    dp.register_message_handler(accept_homework, state=States.state_write_home_work)
    dp.register_message_handler(show_all_home_work, text='Показать доступное дз')
    dp.register_message_handler(chose_delete_home_work, text='Я что то сделал')
    dp.register_message_handler(delete_home_work, state=States.state_chose_delete_home_work)
    dp.register_message_handler(echo_message)
