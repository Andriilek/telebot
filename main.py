import telebot
import config
import sqlite3
from datetime import datetime

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
global receipt_number


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Это наш удобный чат бот!"
                     .format(message.from_user, bot.get_me(), parse_mod='html'))
    start_page(message)
    get_user_id(message)


def start_page(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Одноразки")
    item2 = types.KeyboardButton("Жидкости")
    item3 = types.KeyboardButton("Pod'ы")
    item4 = types.KeyboardButton("Снюс")
    item5 = types.KeyboardButton("Корзина")

    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, "Главное меню"
                     .format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def order(call):
    if call.data == "order_change":
        order_change(call)
    elif call.data == "order_update":
        receipt_message_update(call)
    elif call.data == "order_cancel":
        order_cancel(call)
    elif call.data == "delete_order":
        delete_order(call)
    elif call.data == "order_delete_list":
        order_delete_list(call)
    elif call.data == "order_change_date_and_time":
        order_change_date_and_time(call)


@bot.message_handler(content_types=['text'])
def check(message):
    if message.chat.type == 'private':
        if message.text == 'Одноразки':
            odnorazki(message)
        elif message.text == 'Жидкости':
            liquids(message)
        elif message.text == "Pod'ы":
            pod(message)
        elif message.text == "Снюс":
            snus(message)
        elif message.text == "Elf bar":
            elf_bar(message)
        elif message.text == "Bmor Saturn":
            bmor(message)
        elif message.text == "Главное меню":
            start_page(message)
        elif message.text == "800 тяг":
            elf_800(message)
        elif message.text == "1500 тяг":
            elf_1500(message)
        elif message.text == "2000 тяг":
            elf_2000(message)
        elif message.text == "По крепости":
            sort_by_strength(message)
        elif message.text == "По цене":
            sort_by_cost(message)
        elif message.text == "По объему":
            sort_by_volume(message)
        elif message.text == "Siberia 43 мг":
            tabacco(message)
        elif message.text == "Candy 80 мг":
            candy_80(message)
        elif message.text == "Faff 75 мг":
            faff_75(message)
        elif message.text == "Dzen 50 мг":
            dzen_baroco(message)
        elif message.text == "Яблоки в никотине 50 мг":
            apple_nic(message)
        elif message.text == "Offroad 45 мг":
            tabacco(message)
        elif message.text == "Thunder 42 мг":
            tabacco(message)
        elif message.text == "Baron 40 мг":
            dzen_baroco(message)
        elif message.text == "Hugo Vapor":
            hugo_vapor(message)
        elif message.text == "Joytech Vaal":
            joytech_vaal(message)
        elif message.text == "Nova 65 мг 10/10":
            ger_nova(message)
        elif message.text == "Nova 15мл 135 грн":
            ger_nova(message)
        elif message.text == "3Ger 15мл 150 грн":
            ger_nova(message)
        elif message.text == "3ger 50 мг 9/10":
            ger_nova(message)
        elif message.text == "Flamingo 15 мл 150 грн":
            marvel_flam(message)
        elif message.text == "Flamingo 50 мг 5/10":
            marvel_flam(message)
        elif message.text == "Marvelouse 50 мг 5/10":
            marvel_flam(message)
        elif message.text == "Marvelose 15мл 150 грн":
            marvel_flam(message)
        elif message.text == "Boneshake 15мл 140 грн":
            bon_sol_wes(message)
        elif message.text == "WES 15мл 135 грн":
            bon_sol_wes(message)
        elif message.text == "Сольник 15мл 125 грн":
            bon_sol_wes(message)
        elif message.text == "Boneshake 50 мг 8/10":
            bon_sol_wes(message)
        elif message.text == "Сольник 40 мг 6/10":
            bon_sol_wes(message)
        elif message.text == "WES 50 мг 6/10":
            bon_sol_wes(message)
        elif message.text == "Alchemist 10мл 120 грн":
            mntn_alch(message)
        elif message.text == "Montana 10мл 110 грн":
            mntn_alch(message)
        elif message.text == "Alchemist 50 мг (10мл) 8/10":
            mntn_alch(message)
        elif message.text == "Montana 50 мг (10мл) 7/10":
            mntn_alch(message)
        elif message.text == "Elf bar pod":
            elf_bar_pod(message)
        elif message.text == "Elf bar rf350":
            elf_bar_pod_all(message)
        elif message.text == "Elf bar mate500":
            elf_bar_pod_all(message)
        elif message.text == "Juul":
            juul(message)
        elif message.text == "Ovns W01":
            ovns_w01(message)
        elif message.text == "Minifit":
            minifit(message)
        elif message.text == "Glim Innokin":
            glim_innokin(message)
        elif message.text == "Drag Nano 2":
            drag_nano_2(message)
        elif message.text == "Отмена":
            minifit(message)
        elif message.text == "Eleaf Iorn lite":
            eleaf_iorn_lite(message)
        elif message.text == "10 мл - маленькая баночка":
            mntn_alch(message)
        elif message.text == "15 мл - средняя баночка":
            av_bottle(message)
        elif message.text == "Заказать":
            make_order(message)
        elif message.text == "Заказать Elf bar 1500":
            cost: int = 250
            product_name = "Elf bar 1500"
            get_product_flavor(message, product_name, cost)
        elif message.text == "Заказать Minifit":
            cost: int = 350
            product_name = "Minifit"
            get_product_flavor(message, product_name, cost)
        elif message.text == "Заказать Drag Nano 2":
            cost: int = 745
            product_name = "Drag Nano 2"
            get_product_flavor(message, product_name, cost)
        elif message.text == "Заказать Glim Innokin":
            cost: int = 420
            product_name = "Glim Innokin"
            get_product_flavor(message, product_name, cost)
        elif message.text == "Заказать Ovns W01":
            cost: int = 310
            product_name = "Ovns"
            get_product_flavor(message, product_name, cost)
        elif message.text == "Заказать Elf bar 800":
            cost: int = 200
            product_name = "Elf bar 800"
            get_product_flavor(message, product_name, cost)
        elif message.text == "Заказать Elf bar 2000":
            cost: int = 290
            product_name = "Elf bar 2000"
            get_product_flavor(message, product_name, cost)
        elif message.text == "Заказать Bmor 1600":
            cost: int = 240
            product_name = "Bmore 1600"
            get_product_flavor(message, product_name, cost)
        elif message.text == "Заказать Hugo Vapor 2200":
            cost: int = 275
            product_name = "Hugo Vapor 2200"
            get_product_flavor(message, product_name, cost)
        elif message.text == "Заказать Eleaf Iorn Lite":
            cost: int = 380
            product_name = "Pod система Eleaf Iorn Lite"
            get_product_flavor(message, product_name, cost)
        elif message.text == "Заказать JUUL":
            cost: int = 345
            product_name = "JUUL"
            get_product_flavor(message, product_name, cost)
        elif message.text == "Встреча в Запорожье":
            data_location_check(message)
        elif message.text == "Доставка Новой Почтой":
            post(message)
        elif message.text == "Корзина":
            basket_check(message)
        elif message.text == "Использовать предадущую дату и место":
            show_check(message, admin_id=1032474256)
        elif message.text == "Изменить дату и место":
            get_location(message)
        elif message.text == "Отмена":
            delete()
            start_page(message)
        elif message.text == "Нет, ввести другие":
            get_post_name(message)
        elif message.text == "Да, использовать их":
            show_check(message, 1)


def order_change_date_and_time(call):
    get_location(call.message)


# def delete_list(call):
#   inline = types.InlineKeyboardMarkup()

#    connect = sqlite3.connect('orders.db')
#   cursor = connect.cursor()
#  order_list = cursor.execute("SELECT OrderList FROM Orders WHERE ReceiptNumber = ?", (receipt_number,))
# order_number = cursor.execute("SELECT OrderNumber FROM Orders WHERE ReceiptNumber = ?", (receipt_number,))
# list_orders = []
#   order_number = []
#
#   for name in enumerate(order_list):
#      list_orders.append(name[0])
#
#   for i in list_orders:
#      inline.add(types.InlineKeyboardButton(text=i, callback_data="Кнопка "))
#
# bot.edit_message_text(text="Нажмите на товар который хотите удалить из корзины", chat_id=call.message.chat.id,
#                         message_id=call.message.message_id, reply_markup=inline)


def order_delete_list(call):
    inline = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="Да, уверен(а)", callback_data="delete_order")
    item2 = types.InlineKeyboardButton(text="Отмена", callback_data="order_update")
    inline.add(item1, item2)
    bot.edit_message_text(text="Вы уверены что хотите отменить заказ?", chat_id=call.message.chat.id,
                          message_id=call.message.message_id, reply_markup=inline)


def delete_order(call):
    connect = sqlite3.connect('orders.db')
    cursor = connect.cursor()
    cursor.execute("DELETE FROM Orders WHERE ReceiptNumber = ?", (receipt_number,))
    connect.commit()
    cursor.execute("DELETE FROM Delivery WHERE ReceiptNumber = ?", (receipt_number,))
    connect.commit()
    cursor.execute("UPDATE Receipt SET Status = 'Отменен' WHERE ReceiptNumber = ?", (receipt_number,))
    connect.commit()
    get_user_id(message=call.message)
    start_page(message=call.message)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


def receipt_message_update(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    show_check(message=call.message, admin_id=1)


def order_cancel(call):
    inline = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="Да, уверен(а)", callback_data="delete_order")
    item2 = types.InlineKeyboardButton(text="Отмена", callback_data="order_update")
    inline.add(item1, item2)
    bot.edit_message_text(text="Вы уверены что хотите отменить заказ?", chat_id=call.message.chat.id,
                          message_id=call.message.message_id, reply_markup=inline)


def order_change(call):
    inline = types.InlineKeyboardMarkup()
    #    item1 = types.InlineKeyboardButton(text="Удалить товар", callback_data="delete_list")
    item2 = types.InlineKeyboardButton(text="Изменить место или дату", callback_data="order_change_date_and_time")
    item3 = types.InlineKeyboardButton(text="Назад", callback_data="order_update")
    inline.add(item2, item3)
    bot.edit_message_text(text=call.message.html_text, chat_id=call.message.chat.id,
                          message_id=call.message.message_id, parse_mode='html', reply_markup=inline)


def delete():
    connect = sqlite3.connect('orders.db')
    cursor = connect.cursor()
    cursor.execute("DELETE FROM Orders WHERE OrderNumber = (SELECT OrderNumber From Orders "
                   "ORDER BY OrderNumber DESC LIMIT 1)")
    connect.commit()


def post(message):
    answer = message.text
    if answer == "Отмена":
        delete()
        start_page(message)
    else:
        connect = sqlite3.connect('orders.db')
        cursor = connect.cursor()
        city = cursor.execute("SELECT City FROM Delivery WHERE ReceiptNumber = ?", (receipt_number,)).fetchone()
        post_name = cursor.execute("SELECT PostName FROM Delivery WHERE ReceiptNumber = ?",
                                   (receipt_number,)).fetchone()
        post_number = cursor.execute("SELECT PostNumber FROM Delivery WHERE ReceiptNumber = ?",
                                     (receipt_number,)).fetchone()
        rec_phone = cursor.execute("SELECT RecPhone FROM Delivery WHERE ReceiptNumber = ?",
                                   (receipt_number,)).fetchone()
        rec_name = cursor.execute("SELECT RecName FROM Delivery WHERE ReceiptNumber = ?", (receipt_number,)).fetchone()
        rec_surn = cursor.execute("SELECT RecSurn FROM Delivery WHERE ReceiptNumber = ?", (receipt_number,)).fetchone()
        city = city[0]
        post_name = post_name[0]
        post_number = post_number[0]
        rec_surn = rec_surn[0]
        rec_name = rec_name[0]
        rec_phone = rec_phone[0]
        if city and post_number and post_name and rec_phone and rec_name and rec_surn is None:
            get_post_name(message)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Да, использовать их")
            item2 = types.KeyboardButton("Нет, ввести другие")
            item3 = types.KeyboardButton("Отмена")
            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, "Использовать предадущие данные?")
            bot.send_message(message.chat.id, f"Имя: {rec_name}\n"
                                              f"Фамилия: {rec_surn}\n"
                                              f"Номер телефона: {rec_phone}\n"
                                              f"Город: {city}\n"
                                              f"Название почты: {post_name}\n"
                                              f"Номер отделения: {post_number}\n", reply_markup=markup)


def get_post_name(message):
    answer = message.text
    if answer == "Отмена":
        delete()
        start_page(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Отмена")
        markup.add(item1)
        msg = bot.send_message(message.chat.id, "Введите название почты.", reply_markup=markup)
        bot.register_next_step_handler(msg, get_city_name)


def get_city_name(message):
    answer = message.text
    if answer == "Отмена":
        delete()
        start_page(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Отмена")
        markup.add(item1)
        connect = sqlite3.connect('orders.db')
        cursor = connect.cursor()
        cursor.execute("INSERT INTO Delivery(PostName, ReceiptNumber) VALUES(?,?)", (answer, receipt_number,))
        connect.commit()
        msg = bot.send_message(message.chat.id, "Введите название вашего города.", reply_markup=markup)
        bot.register_next_step_handler(msg, get_post_number)


def get_post_number(message):
    answer = message.text
    if answer == "Отмена":
        delete()
        start_page(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Отмена")
        markup.add(item1)
        connect = sqlite3.connect('orders.db')
        cursor = connect.cursor()
        cursor.execute("UPDATE Delivery SET City = ? WHERE ReceiptNumber = ?", (answer, receipt_number,))
        connect.commit()
        msg = bot.send_message(message.chat.id, "Введите номер(индекс) отделения.", reply_markup=markup)
        bot.register_next_step_handler(msg, get_rec_name)


def get_rec_name(message):
    answer = message.text
    if answer == "Отмена":
        delete()
        start_page(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Отмена")
        markup.add(item1)
        connect = sqlite3.connect('orders.db')
        cursor = connect.cursor()
        cursor.execute("UPDATE Delivery SET PostNumber = ? WHERE ReceiptNumber = ?", (answer, receipt_number,))
        connect.commit()
        msg = bot.send_message(message.chat.id, "Введите имя получателя", reply_markup=markup)
        bot.register_next_step_handler(msg, get_rec_surn)


def get_rec_surn(message):
    answer = message.text
    if answer == "Отмена":
        delete()
        start_page(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Отмена")
        markup.add(item1)
        connect = sqlite3.connect('orders.db')
        cursor = connect.cursor()
        cursor.execute("UPDATE Delivery SET RecName = ? WHERE ReceiptNumber = ?", (answer, receipt_number,))
        connect.commit()
        msg = bot.send_message(message.chat.id, "Введите фамилию получателя", reply_markup=markup)
        bot.register_next_step_handler(msg, get_rec_phone)


def get_rec_phone(message):
    answer = message.text
    if answer == "Отмена":
        delete()
        start_page(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Отмена")
        markup.add(item1)
        connect = sqlite3.connect('orders.db')
        cursor = connect.cursor()
        cursor.execute("UPDATE Delivery SET RecSurn = ? WHERE ReceiptNumber = ?", (answer, receipt_number,))
        connect.commit()
        msg = bot.send_message(message.chat.id, "Введиет номер телефона.", reply_markup=markup)
        bot.register_next_step_handler(msg, get_rec_phone_s)


def get_rec_phone_s(message):
    answer = message.text
    if answer == "Отмена":
        delete()
        start_page(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Отмена")
        markup.add(item1)
        connect = sqlite3.connect('orders.db')
        cursor = connect.cursor()
        cursor.execute("UPDATE Delivery SET RecPhone = ? WHERE ReceiptNumber = ?", (answer, receipt_number,))
        connect.commit()
        show_check(message, 1)


def data_location_check(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Использовать предадущую дату и место")
    item2 = types.KeyboardButton("Изменить дату и место")
    item3 = types.KeyboardButton("Отмена")
    markup.add(item1, item2, item3)

    answer = message.text
    if answer == "Отмена":
        delete()
        start_page(message)
    else:
        connect = sqlite3.connect('orders.db')
        cursor = connect.cursor()
        test_location = cursor.execute("SELECT Location  From Delivery WHERE ReceiptNumber = ?",
                                       (receipt_number,)).fetchone()
        test_time = cursor.execute("SELECT Time  From Delivery WHERE ReceiptNumber = ?",
                                   (receipt_number,)).fetchone()
        if test_location and test_time is not None:
            test_time = test_time[0]
            test_location = test_location[0]
            bot.send_message(message.chat.id, f'Хотите использовать предадущие данные? \n{test_location}, {test_time}',
                             reply_markup=markup)
        else:
            get_location(message)


def get_location(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Отмена")
    markup.add(item1)
    msg = bot.send_message(message.chat.id, "Личная встреча возможна на любой остановке на проспекте,"
                                            "космосе, песках. На Шевченковском только на остановках от"
                                            " Лахти до Иванова и Красной. Напишите боту название остановки"
                                            " или место, в свободной форме. Если подходящего района в списки"
                                            " нету напишите ему @odnorazkizp_zakaz", reply_markup=markup)
    bot.register_next_step_handler(msg, data_time)


def data_time(message):
    answer = message.text
    if answer == "Отмена":
        delete()
        start_page(message)
    else:
        connect = sqlite3.connect('orders.db')
        cursor = connect.cursor()
        test = cursor.execute("SELECT DeliveryNum From Delivery WHERE ReceiptNumber = ?", (receipt_number,)).fetchone()
        if test is None:
            cursor = connect.cursor()
            cursor.execute("INSERT INTO Delivery(ReceiptNumber, Location) VALUES(?, ?)", (receipt_number, answer))
            connect.commit()
        else:
            cursor = connect.cursor()
            cursor.execute("UPDATE Delivery SET ReceiptNumber = ?, Location = ?", (receipt_number, answer))
            connect.commit()

        msg = bot.send_message(message.chat.id, "Напишите дату и желаемое время. В свободной форме.")
        bot.register_next_step_handler(msg, meeting_check)


def meeting_check(message):
    admin_id = 1032474256
    answer = message.text
    if answer == "Отмена":
        delete()
        start_page(message)
    else:
        connect = sqlite3.connect('orders.db')
        cursor = connect.cursor()
        cursor.execute("UPDATE Delivery SET Time = ?", (answer,))
        connect.commit()

        bot.send_message(admin_id, "Есть новый заказ!")
        show_check(message, admin_id)


def show_check(message, admin_id):
    inline = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="Отменить заказ", callback_data="order_cancel")
    item2 = types.InlineKeyboardButton(text="Изменить заказ", callback_data="order_change")
    item3 = types.InlineKeyboardButton(text="Обновить", callback_data="order_update")
    inline.add(item1, item2, item3)

    connect = sqlite3.connect('orders.db')
    cursor = connect.cursor()

    order_list = cursor.execute("SELECT OrderList From Orders WHERE ReceiptNumber = ?", (receipt_number,)).fetchall()
    location = cursor.execute("SELECT Location From Delivery WHERE ReceiptNumber = ?", (receipt_number,)).fetchone()
    time = cursor.execute("SELECT Time From Delivery WHERE ReceiptNumber = ?", (receipt_number,)).fetchone()
    summa = cursor.execute("SELECT SUM(Cost) FROM Orders WHERE ReceiptNumber = ?", (receipt_number,)).fetchone()
    status = cursor.execute("SELECT Status FROM Receipt WHERE ReceiptNumber = ?", (receipt_number,)).fetchone()

    city = cursor.execute("SELECT City FROM Delivery WHERE ReceiptNumber = ?", (receipt_number,)).fetchone()
    post_name = cursor.execute("SELECT PostName FROM Delivery WHERE ReceiptNumber = ?",
                               (receipt_number,)).fetchone()
    post_number = cursor.execute("SELECT PostNumber FROM Delivery WHERE ReceiptNumber = ?",
                                 (receipt_number,)).fetchone()
    rec_phone = cursor.execute("SELECT RecPhone FROM Delivery WHERE ReceiptNumber = ?",
                               (receipt_number,)).fetchone()
    rec_name = cursor.execute("SELECT RecName FROM Delivery WHERE ReceiptNumber = ?", (receipt_number,)).fetchone()
    rec_surn = cursor.execute("SELECT RecSurn FROM Delivery WHERE ReceiptNumber = ?", (receipt_number,)).fetchone()

    status = status[0]
    summa = summa[0]
    location = location[0]
    time = time[0]

    city = city[0]
    post_name = post_name[0]
    post_number = post_number[0]
    rec_surn = rec_surn[0]
    rec_name = rec_name[0]
    rec_phone = rec_phone[0]
    username = message.from_user.username

    cursor.execute("UPDATE Receipt SET TotalSum = ? WHERE ReceiptNumber = ?", (summa, receipt_number,))
    connect.commit()

    list_orders = []
    for index, name in enumerate(order_list):
        list_orders.append(name[0])
    nl = '\n'

    if status == "Ожидает оплаты":
        if location is not None:
            msg = bot.send_message(message.chat.id, f"<u><b>Ваш заказ № : {receipt_number} \n</b></u>"
                                                    f"<u><b>Заказ:</b></u>\n"
                                                    f"\n"
                                                    f"{nl.join(list_orders)} \n"
                                                    f"\n"
                                                    f"______________________________\n"
                                                    f"<u><b>Данные о доставке:</b></u>\n"
                                                    f"\n"
                                                    f"{username}\n"
                                                    f"<b>Место встречи(приблизительное):</b> {location} \n"
                                                    f"<b>Дата и врем(приблизительное):</b> {time} \n"
                                                    f"<b>Сумма к оплате:</b> {summa} \n"
                                                    f"<b>Статус:</b> {status} \n"
                                                    f"______________________________\n"
                                                    f"\n"
                                                    f"Оплатите {summa} грн на карту монобанк 5375411406552831 "
                                                    "или приватбанк 5168745114324525\n"
                                                    f"Для связи с продавцом пишите - @odnorazkizp_zakaz",
                                   reply_markup=inline, parse_mode='html')
            if admin_id == 1032474256:
                bot.forward_message(admin_id, message.chat.id, msg.message_id)
        elif location is None:
            msg = bot.send_message(message.chat.id, f"<u><b>Ваш заказ № : {receipt_number} \n</b></u>"
                                                    f"<u><b>Заказ:</b></u>\n"
                                                    f"\n"
                                                    f"{nl.join(list_orders)} \n"
                                                    f"\n"
                                                    f"______________________________\n"
                                                    f"<u><b>Данные о доставке</b></u>\n"
                                                    f"\n"
                                                    f"{username}\n"
                                                    f"<b>Населенный пункт: </b> {city} \n"
                                                    f"<b>Название почты: </b> {post_name} \n"
                                                    f"<b>Номер отделения(индекс): </b> {post_number} \n"
                                                    f"<b>Имя получателя: </b> {rec_name} \n"
                                                    f"<b>Фамилия получателя: {rec_surn}</b> \n"
                                                    f"<b>Номер телефона получателя: {rec_phone}</b>\n"
                                                    f"<b>Сумма к оплате: {summa}</b>\n"
                                                    f"<b>Статус заказа: {status}</b>\n"
                                                    f"______________________________\n"
                                                    f"\n"
                                                    f"Оплатите {summa} грн на карту монобанк 5375411406552831 "
                                                    "или приватбанк 5168745114324525\n"
                                                    f"Для связи с продавцом пишите - @odnorazkizp_zakaz",
                                   reply_markup=inline, parse_mode='html')

            if admin_id == 1032474256:
                bot.forward_message(admin_id, message.chat.id, msg.message_id)
    elif status == "Оплачено и подтверждено":
        if location is not None:
            bot.send_message(message.chat.id, f"<u><b>Ваш заказ № : {receipt_number} \n</b></u>"
                                              f"<u><b>Заказ:</b></u>\n"
                                              f"\n"
                                              f"{nl.join(list_orders)} \n"
                                              f"\n"
                                              f"______________________________\n"
                                              f"<u><b>Данные о доставке:</b></u>\n"
                                              f"\n"
                                              f"{username}\n"
                                              f"<b>Место встречи(приблизительное):</b> {location} \n"
                                              f"<b>Дата и врем(приблизительное):</b> {time} \n"
                                              f"<b>Сумма к оплате:</b> {summa} \n"
                                              f"<b>Статус:</b> {status} \n"
                                              f"______________________________\n"
                                              f"\n"
                                              f"Оплата успешно прошла. Спасибо за покупку. Продавец "
                                              f"@odnorazkizp_zakaz скоро свяжется с вами.\n",
                             reply_markup=inline, parse_mode='html')

        elif location is None:
            bot.send_message(message.chat.id, f"<u><b>Ваш заказ № : {receipt_number} \n</b></u>"
                                              f"<u><b>Заказ:</b></u>\n"
                                              f"\n"
                                              f"{nl.join(list_orders)} \n"
                                              f"\n"
                                              f"______________________________\n"
                                              f"<u><b>Данные о доставке</b></u>\n"
                                              f"\n"
                                              f"{username}\n"
                                              f"<b>Населенный пункт: </b> {city} \n"
                                              f"<b>Название почты: </b> {post_name} \n"
                                              f"<b>Номер отделения(индекс): </b> {post_number} \n"
                                              f"<b>Имя получателя: </b> {rec_name} \n"
                                              f"<b>Фамилия получателя: {rec_surn}</b> \n"
                                              f"<b>Номер телефона получателя: {rec_phone}</b>"
                                              f"<b>Статус заказа: {status}</b>"
                                              f"______________________________\n"
                                              f"\n"
                                              f"Оплата успешно прошла. Спасибо за покупку. Продавец "
                                              f"@odnorazkizp_zakaz скоро свяжется с вами.\n",
                             reply_markup=inline, parse_mode='html')
    start_page(message)


def basket_check(message):
    global receipt_number
    connect = sqlite3.connect('orders.db')
    cursor = connect.cursor()
    check_sum = cursor.execute('SELECT TotalSum FROM Receipt WHERE ReceiptNumber = ?', (receipt_number,)).fetchone()
    check_sum = check_sum[0]
    if check_sum > 0:
        show_check(message, admin_id=1)
    else:
        bot.send_message(message.chat.id, "Ваша корзина пуста")


def get_user_id(message):
    global receipt_number
    user_id = message.from_user.id
    user_name = message.from_user.username
    connect = sqlite3.connect('orders.db')
    cursor = connect.cursor()
    status = cursor.execute("SELECT Status FROM Receipt WHERE userID = ? ORDER BY ReceiptNumber DESC LIMIT 1",
                            (user_id,)).fetchone()
    status = status[0]

    if status == "Выполнен" or status == "Отменен" or status is None:
        cursor.execute("INSERT INTO Receipt(UserID, UserName, TotalSum, Status) values(?,?,?,'Ожидает оплаты')",
                       (user_id, user_name, 0))
        connect.commit()
        receipt_number = cursor.execute("SELECT ReceiptNumber FROM Receipt WHERE Receipt.UserID = ? ORDER BY "
                                        "ReceiptNumber DESC LIMIT 1", (user_id,)).fetchone()
        receipt_number = receipt_number[0]
    else:
        receipt_number = cursor.execute("SELECT ReceiptNumber FROM Receipt WHERE Receipt.UserID = ? ORDER BY "
                                        "ReceiptNumber DESC LIMIT 1", (user_id,)).fetchone()
        receipt_number = receipt_number[0]


def get_product_flavor(message, product_name, cost):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Отмена")
    markup.add(item1)
    connect = sqlite3.connect('orders.db')
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Orders(ReceiptNumber, OrderList, Data) VALUES(?, ?, ?)",
                   (receipt_number, product_name, datetime.now()))
    connect.commit()
    msg = bot.send_message(message.chat.id, "Напишите вкус или цвет, который хотите купить.", reply_markup=markup)
    bot.register_next_step_handler(msg, get_product_number, cost)


def get_product_number(message, cost):
    answer = message.text
    if answer == "Отмена":
        delete()
        start_page(message)
    else:
        connect = sqlite3.connect('orders.db')
        cursor = connect.cursor()
        cursor.execute("UPDATE Orders SET OrderList = (OrderList || ' ' ||?) WHERE ReceiptNumber = ? AND OrderNumber = "
                       "(SELECT orderNumber From orders ORDER BY orderNumber DESC LIMIT 1)", (answer, receipt_number,))
        cursor.close()
        connect.commit()

        msg = bot.send_message(message.chat.id, "Напишите количество.")
        bot.register_next_step_handler(msg, get_delivery_check, cost)


def get_delivery_check(message, cost):
    answer = message.text
    if answer == "Отмена":
        delete()
        start_page(message)
    elif answer.isdigit():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Встреча в Запорожье")
        item2 = types.KeyboardButton("Доставка Новой Почтой")
        item3 = types.KeyboardButton("Главное меню")
        markup.add(item1, item2, item3)

        summa: int = cost * int(answer)

        connect = sqlite3.connect('orders.db')
        cursor = connect.cursor()
        cursor.execute("UPDATE Orders SET OrderList = (OrderList || ' ' || ? || 'шт'), cost = ? "
                       "WHERE ReceiptNumber = ? AND OrderNumber = "
                       "(SELECT orderNumber From orders ORDER BY orderNumber DESC LIMIT 1)",
                       (answer, summa, receipt_number,))
        connect.commit()

        bot.send_message(message.chat.id, "Выберите способ доставки.", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Введите число цифрой.")
        get_product_number(message, cost)


def make_order(message):
    bot.send_message(message.chat.id, "Для заказа пишите ему @odnorazkizp_zakaz.")


def snus(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Siberia 43 мг")
    item2 = types.KeyboardButton("Faff 75 мг")
    item3 = types.KeyboardButton("Candy 80 мг")
    item4 = types.KeyboardButton("Offroad 45 мг")
    item5 = types.KeyboardButton("Thunder 42 мг")
    item6 = types.KeyboardButton("Dzen 50 мг")
    item7 = types.KeyboardButton("Baron 40 мг")
    item8 = types.KeyboardButton("Яблоки в никотине 50 мг")
    item9 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
    bot.send_message(message.chat.id, "Выбери производителя который интересует.\n"
                                      "После этого вы сможешь выбрать вкус и крепость.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)


def tabacco(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Классический табачный снюс.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001349174922, message_id=12)


def candy_80(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Хороший бестабачный снюс с отличными вкусами.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001349174922, message_id=13)


def faff_75(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Качественный крепкий бестабачный снюс.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001349174922, message_id=14)


def dzen_baroco(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Хороший бестабачный снюс. Альтернатива Velo.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001349174922, message_id=15)


def apple_nic(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Отличная альтернатива снюсу.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001349174922, message_id=16)


def pod(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Elf bar pod")
    item2 = types.KeyboardButton("Juul")
    item3 = types.KeyboardButton("Ovns W01")
    item4 = types.KeyboardButton("Eleaf Iorn lite")
    item5 = types.KeyboardButton("Minifit")
    item6 = types.KeyboardButton("Glim Innokin")
    item7 = types.KeyboardButton("Drag Nano 2")
    item8 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
    bot.send_message(message.chat.id, "Выбери производителя который вас интересует.\n"
                                      "После этого вы сможешь выбрать цвет и модель.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)


def elf_bar_pod(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Elf bar rf350")
    item2 = types.KeyboardButton("Elf bar mate500")
    item3 = types.KeyboardButton("Заказать")
    item4 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Выбери модель которая интересует. Потом вы сможете выбрать "
                                      "цвет.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)


def elf_bar_pod_all(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Качественные Pod системы от известного бренда.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=331)


def drag_nano_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать Drag Nano 2")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Всеми известный девайс от амереканской компании.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=344)


def glim_innokin(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать Glim Innokin")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Всеми известный девайс от амереканской компании.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=350)


def juul(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать JUUL")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Всеми известный девайс от амереканской компании.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=320)


def minifit(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать Minifit")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Одна из лучших Pod систем в своей ценовой категории.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=351)


def ovns_w01(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать Ovns W01")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Отличная замена для Juul.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=330)


def eleaf_iorn_lite(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать Eleaf Iorn Lite")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Выбери производителя который интересует. Потом вы сможете выбрать "
                                      "цвет и модель.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=333)


def odnorazki(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Elf bar")
    item2 = types.KeyboardButton("Bmor Saturn")
    item3 = types.KeyboardButton("Hugo Vapor")
    item4 = types.KeyboardButton("Joytech Vaal")
    item5 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, "Выберите производителя который вас интересует.\n"
                                      "Потом вы сможешь выбрать количество тяг и вкус.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)


def bmor(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать Bmor 1600")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Качественная одноразка от американского "
                                      "производителя с большим аккамулятором и объемом жидкости чем Elf bar 1500.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=327)


def joytech_vaal(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "В пути. Доступен только предзаказ.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    # bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=327)


def hugo_vapor(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать Hugo Vapor 2200")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Уникальная одноразка 2 в 1. С каждной стороны по вкусу.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=323)


def elf_bar(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("800 тяг")
    item2 = types.KeyboardButton("1500 тяг")
    item3 = types.KeyboardButton("2000 тяг")
    item4 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Выбирете количество тяг.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)


def elf_2000(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать Elf bar 2000")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id,
                     "Отличная вкусопередача, компактность и цена. Цена за 1 тягу самая низкая из всех Elf bar.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=307)


def elf_1500(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать Elf bar 1500")
    item2 = types.KeyboardButton("Главное меню")
    item3 = types.KeyboardButton("Корзина")

    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Отличная вкусопередача, компактность и цена. Хватит до 5 дней.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=293)


def elf_800(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать Elf bar 800")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id,
                     "Отличная вкусопередача, компактность и цена. Оптимальное сочетание цены - качества.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=241)


def liquids(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("По крепости")
    item2 = types.KeyboardButton("По цене")
    item3 = types.KeyboardButton("По объему")
    item4 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Выберете критерий по которому хотите найти жидкость".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)


def sort_by_strength(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Nova 65 мг 10/10")
    item2 = types.KeyboardButton("3ger 50 мг 9/10")
    item3 = types.KeyboardButton("Boneshake 50 мг 8/10")
    item4 = types.KeyboardButton("Alchemist 50 мг (10мл) 8/10")
    item5 = types.KeyboardButton("Montana 50 мг (10мл) 7/10")
    item6 = types.KeyboardButton("WES 50 мг 6/10")
    item7 = types.KeyboardButton("Сольник 40 мг 6/10")
    item8 = types.KeyboardButton("Flamingo 50 мг 5/10")
    item9 = types.KeyboardButton("Marvelouse 50 мг 5/10")
    item10 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
    bot.send_message(message.chat.id, "Крепось - очень субъективный параметр. Чем она больше ,тем сильнее тх."
                                      " Но каждый ощущает его по разному, цифры основаны на оценках клиентов которые"
                                      " пробовали данные жидкости,"
                                      " а не на количестве никотина.".format(message.from_user, bot.get_me(),
                                                                             parse_mod='Markdown'), reply_markup=markup)


def sort_by_cost(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Montana 10мл 110 грн")
    item2 = types.KeyboardButton("Alchemist 10мл 120 грн")
    item3 = types.KeyboardButton("Сольник 15мл 125 грн")
    item4 = types.KeyboardButton("WES 15мл 135 грн")
    item5 = types.KeyboardButton("Nova 15мл 135 грн")
    item6 = types.KeyboardButton("Boneshake 15мл 140 грн")
    item7 = types.KeyboardButton("Marvelose 15мл 150 грн")
    item8 = types.KeyboardButton("Flamingo 15 мл 150 грн")
    item9 = types.KeyboardButton("3Ger 15мл 150 грн")
    item10 = types.KeyboardButton("3Ger 30мл 260 грн")
    item11 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
    bot.send_message(message.chat.id, "Не забывайте о том, что почти всегда цена = качество."
                     .format(message.from_user, bot.get_me(), parse_mod='Markdown'), reply_markup=markup)


def sort_by_volume(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("10 мл - маленькая баночка")
    item2 = types.KeyboardButton("15 мл - средняя баночка")
    item3 = types.KeyboardButton("30 мл - большая баночка")
    item4 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Чем больше баночка, тем "
                                      "дешевле стоит 1 мл жидкости.".format(message.from_user,
                                                                            bot.get_me(), parse_mod='Markdown'),
                     reply_markup=markup)


def ger_nova(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Крепкие жидкости.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=221)


def marvel_flam(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Малайзийские жидкости.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=224)


def bon_sol_wes(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Бютжетные жидкости.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=213)


def mntn_alch(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать")
    item2 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Маленькие баночки жижи.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=226)


def av_bottle(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("3Ger 50мг 150грн")
    item2 = types.KeyboardButton("Nova 65мг 135грн")
    item3 = types.KeyboardButton("Boneshake 50мг 140грн")
    item4 = types.KeyboardButton("Marvelose 50мг 150грн")
    item5 = types.KeyboardButton("Flamingo 50мг 150грн")
    item6 = types.KeyboardButton("Сольник 40мг 125грн")
    item7 = types.KeyboardButton("WES 50мг 135грн")
    item8 = types.KeyboardButton("Flip 50мг 120грн")
    item9 = types.KeyboardButton("Заказать")
    item10 = types.KeyboardButton("Главное меню")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
    bot.send_message(message.chat.id, "Средние баночки жижи.".
                     format(message.from_user, bot.get_me(), parse_mod='html'), reply_markup=markup)
    bot.forward_message(message.chat.id, from_chat_id=-1001403302025, message_id=226)


bot.polling(non_stop=True)
