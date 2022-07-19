import logging
import sqlite3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from collections import deque
import markup as nav
from head import TOKEN_CKR
import datetime


def list_X():
    result_list = []
    with open('no_list.txt', 'r', encoding='utf-8') as f:
        list_x = f.readlines()
        for i in range(len(list_x)):
            x = list_x[i].strip().split(' -')
            result_list.append(x[0])
    result_list = set(result_list)
    return result_list


def sql_select(teleid):
    """
    Подключаемся к БД и выбираем данные по ruk запросившего отчет.
    Ищет в БД ruk и возвращает кортеж строки
    """
    con = sqlite3.connect('ASU.sqlite')
    sql = "SELECT * FROM ASUSKLAD WHERE TeleID = ?"
    data = (teleid,)
    with con:
        result = con.execute(sql, data)
        for result_tuple in result:
            return result_tuple


def sql_select_otchet(name):
    """

    """
    con = sqlite3.connect('ASU.sqlite')
    sql = "SELECT * FROM OTCHET WHERE name = ?"
    data = (name,)
    with con:
        result = con.execute(sql, data)
        for result_tuple in result:
            return result_tuple


def logs(x):
    with open('log.txt', 'a+', encoding='utf-8') as f:
        print(datetime.datetime.now(), 'Запрос отчета - ', x.text.lower(), '-', x.from_user.first_name, x.from_user.id, x.chat,
              file=f, end='\n')


def select_logs():
    with open('log.txt', 'r', encoding='utf-8') as f:
        result_logs = []
        for row in deque(f, 10):
            result_logs.append(row.strip())
        return result_logs


bot = Bot(token=TOKEN_CKR)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
list_priv = ['привет', 'здрасте', 'хай', 'здравствуйте', 'ghbdtn']


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    if msg.from_user.id == 725455605:
        await bot.send_message(msg.from_user.id, '👋 Приветствую О ВЕЛИКИЙ СОЗДАТЕЛЬ!!! Что пожелаете мой ГОСПОДИН?',
                               reply_markup=nav.main)
    else:
        await bot.send_message(msg.from_user.id, '👋 Привет {0.first_name}'.format(msg.from_user),
                               reply_markup=nav.main)


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() in list_priv:
        if msg.from_user.id == 725455605:
            await bot.send_message(msg.from_user.id, '👋 Приветствую О ВЕЛИКИЙ СОЗДАТЕЛЬ!!! Что пожелаете мой ГОСПОДИН?',
                                   reply_markup=nav.main_Admin)
        else:
            await bot.send_message(msg.from_user.id, '👋 Привет {0.first_name}'.format(msg.from_user),
                                   reply_markup=nav.main)
    elif msg.text == '🤙 ОТЧЕТЫ':
        await bot.send_message(msg.from_user.id, 'Переходим в раздел ОТЧЕТЫ', reply_markup=nav.main_report)
    elif msg.text == '⁉️ ИНФО ⁉️':
        await msg.reply('Переходим к ⁉️ИНФО ⁉️', reply_markup=nav.infoMenu)
    elif msg.text == 'Главное меню':
        if msg.from_user.id == 725455605:
            await msg.answer('Переходим в Главное меню', reply_markup=nav.main_Admin)
        else:
            await msg.answer('Переходим в Главное меню', reply_markup=nav.main)
    elif msg.text == 'АДМИНКА':
        await msg.answer('Слушаю Вас СОЗДАТЕЛЬ!', reply_markup=nav.main_AdminMENU)
    elif msg.text == 'ЛОГИ':
        for i in select_logs():
            await msg.answer(i)
    elif msg.text == 'АРМ СКЛАД АСУ':
        await bot.send_message(msg.from_user.id, 'Переходим в раздел ОТЧЕТЫ АСУ ВРК', reply_markup=nav.main_ASU)
    elif msg.text == 'На проверку АРМ Склад':
        await msg.answer('Выбери вид отчета', reply_markup=nav.sklad)
    elif msg.text == 'Отклоненные АРМ Склад':
        await msg.answer('Извините! Данный отчет находится в разработке!')
    elif msg.text == 'Для руководства':
        asuvrk = AS.ASUVRK(sql_select(msg.from_user.id)[0], sql_select_otchet('АРМ СКЛАД АСУ')[1])
        data = msg.text
        asuvrk.ruk_count_neprov(data)
        await msg.answer('Отчет сформирован!')
        logs(msg)
    elif msg.text == 'Для пользователей':
        asuvrk = AS.ASUVRK(sql_select(msg.from_user.id)[0], sql_select_otchet('АРМ СКЛАД АСУ')[1])
        data = msg.text
        for j in asuvrk.ruk_count_neprov(data):
            await msg.answer(j)
        logs(msg)
    elif msg.text == 'Бартковская':
        if msg.from_user.id == 725455605 or msg.from_user.id == 5339196113:
            await msg.answer(m.mail_bart())
            logs(msg)
            await bot.send_message(msg.from_user.id, '👋 Создан отчет Бартковской')
        else:
            await msg.answer(f'{msg.from_user} для Вас данный отчет недоступен')
    elif msg.text == 'Стоимость формирования отчета':
        await msg.answer(f'{msg.from_user.first_name}, раздел находится в разработке!')
    else:
        if msg.text.lower() not in list_X() and msg.from_user.id == 725455605:
            await msg.reply('Услыште создателя!!! И Вы будете услышаны!')
            logs(msg)
        elif msg.text.lower() not in list_X():
            logs(msg)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
