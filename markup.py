from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, \
    InlineKeyboardMarkup, InlineKeyboardButton

""" Кнопки """

btnMain = KeyboardButton('Главное меню')
btnNaProvSklad = KeyboardButton('На проверку АРМ Склад')
btnVopr = KeyboardButton('🤙 ОТЧЕТЫ')
btnContact = KeyboardButton('КОНТАКТЫ')
btnInfo = KeyboardButton('⁉️ ИНФО ⁉️')
btnOtclSklad = KeyboardButton('Отклоненные АРМ Склад')
btnRuk = KeyboardButton('Для руководства')
btnRukandUse = KeyboardButton('Для пользователей')
btnNaProvVRK1 = KeyboardButton('На проверку ВРК-1')
btnOtclVRK1 = KeyboardButton('Отклоненные ВРК-1')
btnASUVRK = KeyboardButton('АРМ СКЛАД АСУ')
btnVRK1 = KeyboardButton('АРМ СКЛАД ВРК-1')
btnVCHD = KeyboardButton('АРМ СКЛАД ВЧДЭ')
btnAdmin = KeyboardButton('АДМИНКА')
btnLogi = KeyboardButton('ЛОГИ')
# btnSend = KeyboardButton('ДА')
# btnNotSend = KeyboardButton('НЕТ')
btnInfoReport = KeyboardButton('Информация об отчетах')
btnMoney = KeyboardButton('Стоимость формирования отчета')

""" Меню """

infoMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfoReport, btnMoney, btnMain)
# Меню отчетов
main_report = ReplyKeyboardMarkup(resize_keyboard=True).add(btnASUVRK, btnVRK1, btnVCHD, btnMain)
main_ASU = ReplyKeyboardMarkup(resize_keyboard=True).add(btnNaProvSklad, btnOtclSklad, btnMain)
main_AdminMENU = ReplyKeyboardMarkup(resize_keyboard=True).add(btnLogi, btnMain)
# Меню Арм склад
sklad = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRuk, btnRukandUse, btnMain)
# send = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSend, btnNotSend, btnMain)
# Главное меню
main = ReplyKeyboardMarkup(resize_keyboard=True).add(btnVopr, btnInfo)
main_Admin = ReplyKeyboardMarkup(resize_keyboard=True).add(btnVopr, btnInfo, btnAdmin)

""" Оконная кнопка """
# markup = InlineKeyboardMarkup()
# booton1 = InlineKeyboardButton("👍Сайт СНТ Дубрава", url='yandex.ru')
# markup.add(booton1)